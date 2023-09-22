import math
import sys
import time

import pygame
import os
from backend import Backend
from button import Button

class GUI(object):

    ROW_COUNT = 6
    COLUMN_COUNT = 7
    SQUARESIZE = 100    # wielkosc 100px
    TOKENS = [[]]
    BLACK = (0,0,0)



    def __init__(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'
        pygame.init()
        self.WIDTH = self.COLUMN_COUNT * self.SQUARESIZE
        self.HEIGHT = (self.ROW_COUNT + 1) * self.SQUARESIZE
        self.TURN = 0
        self.backend = Backend(self.COLUMN_COUNT, self.ROW_COUNT)
        self.FONT = pygame.font.SysFont("corbel", 20)

        size = (self.WIDTH, self.HEIGHT)
        self.SCREEN = pygame.display.set_mode(size)
        self.background = pygame.image.load(R"D:\Moje dokumenty\PROGRAMOWANIE\4_in_a_row\graphics\4inrow background.png")
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
                R"D:\Moje dokumenty\PROGRAMOWANIE\4_in_a_row\graphics\green_token.png").convert_alpha()
            # self.TOKENS[xPos][yPos] = token_img
            self.SCREEN.blit(token_img, screenPos)
        else:
            token_img = pygame.image.load(
                R"D:\Moje dokumenty\PROGRAMOWANIE\4_in_a_row\graphics\red_token.png").convert_alpha()
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



