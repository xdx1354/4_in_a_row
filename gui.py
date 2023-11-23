import math
import sys
import time

import pygame
import os
from backend import Backend
from button import Button
import pygame_menu

class GUI(object):

    ROW_COUNT = 6
    COLUMN_COUNT = 7
    SQUARESIZE = 100    # wielkosc 100px
    TOKENS = [[]]
    BLACK = (0,0,0)



    def __init__(self):
        self.SECOND_PLAYER = None
        self.FIRST_PLAYER = None
        os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'
        pygame.init()
        self.WIDTH = self.COLUMN_COUNT * self.SQUARESIZE
        self.HEIGHT = (self.ROW_COUNT + 1) * self.SQUARESIZE
        self.TURN = 0
        self.backend = Backend(self.COLUMN_COUNT, self.ROW_COUNT)


        self.FONT = pygame.font.SysFont("corbel", 20)

        size = (self.WIDTH, self.HEIGHT)
        self.SCREEN = pygame.display.set_mode(size)
        self.background = pygame.image.load(R".\graphics\4inrow background.png")
        self.clock = pygame.time.Clock()

        # GUI POSITIONING CONSTANTS
        self.MIDDLE_OF_SCREEN = (self.WIDTH/2, self.HEIGHT/2)

        self.navy_pixel = pygame_menu.themes.Theme(
            background_color=(30, 50, 70),
            title_font=pygame_menu.font.FONT_8BIT,
            title_font_size=40,
            title_font_color=(200, 200, 200),
            widget_font=pygame_menu.font.FONT_BEBAS,
            widget_font_size=30,
            widget_font_color=(255, 255, 255),
            widget_background_color=(50, 70, 90,0),
            selection_color=(200, 50, 50),
            # selection_effect=pygame_menu.widgets.effects.Shadow()
        )






    def draw_board(self):
        self.SCREEN.fill(self.BLACK)
        self.SCREEN.blit(self.background, (0,0))
        pygame.display.flip()


    def restart_game(self):
        self.TURN +=1               # zaczynac bedzie przeciwny gracz
        self.TURN %=2
        self.backend.clearTable()
        self.draw_board()
        self.boardScreen()


    def placeToken(self, col, token):
        col = self.backend.last_placed_token_pos[0]
        row = self.backend.last_placed_token_pos[1]
        screenPos = self.backend.tabPosToScreenPos(col, row)


        if token == 1:
            token_img = pygame.image.load(
                R".\graphics\green_token.png").convert_alpha()
            # self.TOKENS[xPos][yPos] = token_img
            self.SCREEN.blit(token_img, screenPos)
        else:
            token_img = pygame.image.load(
                R".\graphics\red_token.png").convert_alpha()
            # self.TOKENS[xPos][yPos] = token_img
            self.SCREEN.blit(token_img, screenPos)
        pygame.display.update()

    def boardScreen(self):
        self.vsScreen()
        self.backend.clearTable()
        self.draw_board()
        pygame.display.update()
        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    selection = int(math.floor(event.pos[0] / 100))
                    if self.TURN == 0:
                        if self.backend.move(1, selection):
                            self.placeToken(selection, self.TURN)
                            if self.backend.checkWinCon(self.TURN + 1):
                                if self.TURN + 1 == 1:
                                    winner = self.FIRST_PLAYER
                                    self.backend.updateRatings(1, self.FIRST_PLAYER[1], self.SECOND_PLAYER[1])
                                else:
                                    winner = self.SECOND_PLAYER
                                    self.backend.updateRatings(2, self.FIRST_PLAYER[1], self.SECOND_PLAYER[1])

                                print('Gracz ', winner[0], ' wygrywa!')
                                game_over = True
                                self.gameoverScreen(winner)  # Call gameoverScreen when game ends
                            self.TURN = 1  # Switch to the next player's turn
                    else:
                        if self.backend.move(2, selection):
                            self.placeToken(selection, self.TURN)
                            if self.backend.checkWinCon(self.TURN + 1):
                                if self.TURN + 1 == 1:
                                    winner = self.FIRST_PLAYER
                                else:
                                    winner = self.SECOND_PLAYER
                                print('Gracz ', winner[0], ' wygrywa!')
                                game_over = True
                                self.gameoverScreen(winner)  # Call gameoverScreen when game ends
                            self.TURN = 0  # Switch to the next player's turn

        self.clock.tick(15)  # Limit the frame rate


    """
    def startingScreen(self):

        background = (69,69,69)
        self.SCREEN.fill(background)
        startText = self.FONT.render("Click the screen to start", True, self.BLACK)
        # print( startText.get_width())
        self.SCREEN.blit(startText, (self.WIDTH/2 - startText.get_width()/2, self.HEIGHT/2 - startText.get_height()/2 ))

        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            btn = Button(self.SCREEN.get_width()/2 - 140/2, self.SCREEN.get_height()/2 - 100/2, 140, 100, (140, 40, 70), (140, 40, 140), self.SCREEN)
            btn.setText("START", "corbel", 15)
            if btn.isClicked():
                # print("BTN CLICKED")
                self.boardScreen()
                # break

            btn = Button(20, 20, 80, 30, (140, 40, 70), (140, 40, 140), self.SCREEN)
            btn.setText("TEST", "corbel", 10)
            if btn.isClicked():
                print("BTN clicked")
                # break

            pygame.display.update()
            self.clock.tick(15)
    """

    def gameoverScreen(self, winner):

        menu = pygame_menu.Menu('Game Over', self.WIDTH - 20, self.HEIGHT - 20, theme=self.navy_pixel)
        labelText = winner[0] + ' won!'
        menu.add.label(labelText, font_size=100,  font_color=(102, 0, 102), margin = (0,100))
        menu.add.button("PLAY AGAIN", lambda: self.restart_game())  # Add a button to restart the game
        menu.add.button('Back to Menu', lambda: self.newStartingScreen())  # Button to go back to the main menu

        menu.mainloop(self.SCREEN)  # Show the game over screen

        #


    def newStartingScreen(self):
        menu = pygame_menu.Menu('4 in a row', self.WIDTH - 20, self.HEIGHT - 20, theme=self.navy_pixel)


        # Add selectors for choosing players and keep references to them
        selector_player1 = menu.add.selector(title='Choose 1st player\t', items=self.backend.players)
        selector_player2 = menu.add.selector(title='Choose 2nd player\t', items=self.backend.players)

        self.FIRST_PLAYER = selector_player1.get_value()[0]
        self.SECOND_PLAYER = selector_player2.get_value()[0]

        # Add a button to start the game, passing the selectors' references to the start_game function
        menu.add.button('Start Game', lambda: self.start_game(selector_player1, selector_player2))
        menu.add.button('Add new player', lambda: self.addNewPlayerScreen())
        menu.add.button('LEADERBOARD', lambda: self.newLeaderboardScreen())
        menu.mainloop(self.SCREEN)

    def start_game(self, selector_player1, selector_player2):
        # Retrieve values from selectors passed as arguments
        self.FIRST_PLAYER = selector_player1.get_value()[0]
        self.SECOND_PLAYER = selector_player2.get_value()[0]


        if self.FIRST_PLAYER == self.SECOND_PLAYER:
            # Players are the same, show a prompt or message
            print("Please select different players!")
            # Add code to show a prompt (maybe with Pygame or any other UI method)
            # ...

            # Go back to the starting screen/menu
            self.newStartingScreen()
        else:
            print(f'Starting the game with Player 1: {self.FIRST_PLAYER} and Player 2: {self.SECOND_PLAYER}')
            self.boardScreen()

    def newLeaderboardScreen(self):
        self.backend.getDB()
        menu = pygame_menu.Menu('Leaderboard', self.WIDTH - 20, self.HEIGHT - 20, theme=self.navy_pixel)

        # Sort player data by rating (descending order)
        players_sorted = sorted(self.backend.playersDB, key=lambda x: int(x[2]), reverse=True)
        leaderboard_title = "Leaderboard"
        menu.add.label(leaderboard_title)

        for player in players_sorted:
            player_info = f"{player[0]} - Rating: {player[2]}"
            menu.add.label(player_info)
        menu.add.button('Back to Menu', self.newStartingScreen)
        menu.mainloop(self.SCREEN)

    def addNewPlayerScreen(self):

        newPlayerName = ""
        def get_name(val):
            nonlocal newPlayerName
            newPlayerName = val

        menu = pygame_menu.Menu('Add new player', self.WIDTH - 20, self.HEIGHT - 20, theme=self.navy_pixel)

        menu.add.text_input('Enter player\'s name: ', default='', onchange=get_name)



        menu.add.button('ADD', lambda: self.backend.addPlayer(newPlayerName))


        menu.add.button('Back to Menu', self.newStartingScreen)
        menu.mainloop(self.SCREEN)

    def vsScreen(self):
        # Get player information
        player1_name = self.FIRST_PLAYER[0]
        player2_name = self.SECOND_PLAYER[0]
        player1_rating = self.backend.getRatingFromID(self.FIRST_PLAYER[1])
        player2_rating = self.backend.getRatingFromID(self.SECOND_PLAYER[1])
        print(self.FIRST_PLAYER[1])

        # Display player information on the screen
        vs_font = pygame.font.SysFont('mypuma', 90)
        player_font = pygame.font.SysFont('consolas', 30)

        # Render VS text
        vs_text = vs_font.render("VS", True, (255, 255, 255))

        # Render player information
        player1_text = player_font.render(f"{player1_name} - Rating: {player1_rating}", True, (255, 255, 255))
        player2_text = player_font.render(f"{player2_name} - Rating: {player2_rating}", True, (255, 255, 255))

        # Clear the screen
        self.SCREEN.fill((30, 50, 70))

        # Calculate positions
        vs_text_rect = vs_text.get_rect(center=(self.WIDTH / 2, self.HEIGHT / 2))
        player1_text_rect = player1_text.get_rect(topleft=(20, 200))
        player2_text_rect = player2_text.get_rect(bottomright=(self.WIDTH - 20, self.HEIGHT - 200))

        # Display text on the screen
        self.SCREEN.blit(vs_text, vs_text_rect)
        self.SCREEN.blit(player1_text, player1_text_rect)
        self.SCREEN.blit(player2_text, player2_text_rect)

        # Update the display
        pygame.display.update()

        # Display for around 3 seconds
        pygame.time.wait(3000)

        # Clear the screen
        self.SCREEN.fill((30, 50, 70))
        pygame.display.update()