import math
import sys

from gui import GUI as gui
import pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
# Other game constants like colors, board size, etc.

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('4 in a Row Game')




gui = gui()




game_over = False
while not game_over:
    gui.newStartingScreen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                   # gdy wyjscie
            sys.exit()
        pygame.display.update()











