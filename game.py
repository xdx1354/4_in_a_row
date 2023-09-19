import math
import sys

from gui import GUI as gui
import pygame
print('4 IN A ROW GAME')




gui = gui()




game_over = False
while not game_over:
    gui.startingScreen()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:                   # gdy wyjscie
                  sys.exit()
            else:
                pass
                # if :
                #     pygame.display.update()
                #     break
    pygame.display.update()
    # game_over = True










