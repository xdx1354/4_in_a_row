import math
import sys

from gui import GUI as gui
import pygame
print('4 IN A ROW GAME')




gui = gui()
gui.draw_board()




game_over = False
while not game_over:

    for event in pygame.event.get():
            if event.type == pygame.QUIT:                   # gdy wyjscie
                  sys.exit()
            else:
                if gui.boardScreen():
                    pygame.display.update()
                    break
    game_over = True










