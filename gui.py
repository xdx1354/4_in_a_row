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






    def draw_board(self):
        self.SCREEN.fill(self.BLACK)
        self.SCREEN.blit(self.background, (0,0))
        pygame.display.flip()


    def restart_game(self):
        self.draw_board()
        self.backend.clearTable()
        self.TURN +=1               # zaczynac bedzie przeciwny gracz
        self.TURN %=2

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
        self.draw_board()
        pygame.display.update()
        game_over = False
        while True and not game_over:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.TURN == 0:
                        again = 1
                        while again == 1:
                            selection = int(math.floor(event.pos[0] / 100))
                            if self.backend.move(1, int(selection)):
                                self.placeToken(selection, self.TURN)
                                again = 0
                            else:
                                print("Wybrana kolumna jest pelna, wybierz inna")
                                again = 1

                    else:
                        again = 1
                        while again == 1:

                            selection = int(math.floor(event.pos[0] / 100))
                            if self.backend.move(2, int(selection)):
                                again = 0
                                self.placeToken(selection, self.TURN)
                            else:
                                print("Wybrana kolumna jest pelna, wybierz inna")
                                again = 1
                                # TODO: FIX INFINITY LOOP!!!!!!!!!!


                    # check wincon
                    if self.backend.checkWinCon(self.TURN + 1):
                        print('Gracz ', self.TURN + 1, ' wygrywa!')
                        game_over = True

                    self.TURN += 1
                    self.TURN %= 2
            self.clock.tick(15)
        self.gameoverScreen()

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

    def gameoverScreen(self):
        background = (69, 69, 69)
        self.SCREEN.fill(background)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     self.boardScreen()

            btn = Button(20, 20, 80, 30, (140, 40, 70), (140, 40, 140), self.SCREEN)
            btn.setText("TEST", "corbel", 10)
            if btn.isClicked():
                self.backend.clearTable()
                self.draw_board()
                self.boardScreen()
                print("BTN clicked")

            pygame.display.update()
            self.clock.tick(15)

    def newStartingScreen(self):
        menu = pygame_menu.Menu('4 in a row', self.WIDTH - 20, self.HEIGHT - 20, theme=pygame_menu.themes.THEME_BLUE)


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
        menu = pygame_menu.Menu('Leaderboard', self.WIDTH - 20, self.HEIGHT - 20, theme=pygame_menu.themes.THEME_BLUE)

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

        menu = pygame_menu.Menu('Add new player', self.WIDTH - 20, self.HEIGHT - 20, theme=pygame_menu.themes.THEME_BLUE)

        menu.add.text_input('Enter player\'s name: ', default='', onchange=get_name)



        menu.add.button('ADD', lambda: self.backend.addPlayer(newPlayerName))


        menu.add.button('Back to Menu', self.newStartingScreen)
        menu.mainloop(self.SCREEN)

