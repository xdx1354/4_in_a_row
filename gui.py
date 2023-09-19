import math
import sys

import pygame
import os
from backend import Backend

class GUI(object):

    ROW_COUNT = 6
    COLUMN_COUNT = 7
    SQUARESIZE = 100    # wielkosc 100px
    TOKENS = [[]]




    def __init__(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'
        pygame.init()
        width = self.COLUMN_COUNT * self.SQUARESIZE
        height = (self.ROW_COUNT + 1) * self.SQUARESIZE
        self.TURN = 0
        self.backend = Backend(self.COLUMN_COUNT, self.ROW_COUNT)

        size = (width, height)
        self.SCREEN = pygame.display.set_mode(size)
        self.background = pygame.image.load(R"D:\Moje dokumenty\PROGRAMOWANIE\4_in_a_row\graphics\4inrow background.png")




    def draw_board(self):

        self.SCREEN.blit(self.background, (0,0))
        pygame.display.flip()


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


                    # check wincon
                    if self.backend.checkWinCon(self.TURN + 1):
                        print('Gracz ', self.TURN + 1, ' wygrywa!')
                        game_over = True

                    self.TURN += 1
                    self.TURN %= 2

        return True