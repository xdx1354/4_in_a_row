import pygame
import os

class Table(object):

    ROW_COUNT = 6
    COLUMN_COUNT = 7
    SQUARESIZE = 100    # wielkosc 100px
    TOKENS = [[]]



    def __init__(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'
        pygame.init()
        width = self.COLUMN_COUNT * self.SQUARESIZE
        height = (self.ROW_COUNT + 1) * self.SQUARESIZE

        size = (width, height)
        self.SCREEN = pygame.display.set_mode(size)


        self.table = [[0 for i in range(self.COLUMN_COUNT)] for j in range(self.ROW_COUNT)]

## PYGAME FRONTEND AND GUI

    def draw_board(self):

        background = pygame.image.load(R"D:\Moje dokumenty\PROGRAMOWANIE\4_in_a_row\4inrow background.png")
        self.SCREEN.blit(background, (0,0))
        pygame.display.flip()

        """
        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT):
                pass   
        pass
        """



## CLI INTERFACE AND BACKEND
    def printTable(self):
        """
        # print('    ', end="")
        # for i in range(0,7):
        #     print(i, ' ', end="")
        # print("\n")
        # for i in range (0, 7):
        #     for j in range (0, 7):
        #         if j==0:
        #             print(i, '| ', end="")
        #             print(self.table[i][j], ' ', end="")
        #         else:
        #             print(self.table[i][j], ' ', end="")
        #     print('\n')
        """
        for i in range(0, 7):
            print(i,'|', end='')
        print()
        for i in range(0,6):
            print(self.table[i])

    def checkCol(self,col):
        if self.table[0][col] == 0:
            return True
        else:
            return False

    def findEmptyRow(self,col):
        for r in reversed(range(self.ROW_COUNT)):
            if self.table[r][col] == 0:
                return r

    def placeToken(self, col, token):
        xPos = int(self.findEmptyRow(col))
        yPos = int(col)
        self.table[xPos][yPos] = token                              # inserting
        xScreenPos = int(xPos*100)
        yScreenPos = int(yPos*100 + 100)
        screenPos = (xScreenPos, yScreenPos)

        if token == 1:
            token_img = pygame.image.load(R"D:\Moje dokumenty\PROGRAMOWANIE\4_in_a_row\green_token.png").convert_alpha()
            # self.TOKENS[xPos][yPos] = token_img
            token_img.blit(self.SCREEN, screenPos)
        else:
            token_img = pygame.image.load(R"D:\Moje dokumenty\PROGRAMOWANIE\4_in_a_row\red_token.png").convert_alpha()
            # self.TOKENS[xPos][yPos] = token_img
            token_img.blit(self.SCREEN, screenPos)

        pygame.display.update()

    def printAllTokens(self):
        for i in range(self.ROW_COUNT):
            for j in range(self.COLUMN_COUNT):
                self.TOKENS[i][j].blit(self.SCREEN, self.tabPosToScreenPos(j, i))


    def tabPosToScreenPos(self, x, y):
        xScreen = int (x*100)
        yScreen = int(y*100 + 100)
        return xScreen, yScreen

    def move(self, token, col):
        """
        :param token: its -1 if player's no2 and 1 if player's no1
        :param col: col picked by a player
        :return:
        """

        if self.checkCol(col):                  # sprawdzenie czy jest wolne miejsce w danej kolumnie
            self.placeToken(col, token)         # wstawienie tokena w pierwsze wolne pole od dołu
            return True                         # zakonczono sukcesem
        else:
            return False                        # zakonczono porażką

    def clearTable(self):
        rows, cols = (7, 7)
        self.table = [[0 for i in range(cols)] for j in range(rows)]

    def checkWinCon(self, token):

        # checking horizontal
        for c in range(self.COLUMN_COUNT-3):
            for r in range(self.ROW_COUNT):
                if self.table[r][c] == token and self.table[r][c+1] == token and self.table[r][c+2] == token and self.table[r][c+3] == token:
                    return True

        #checking vertical
        for r in range(self.ROW_COUNT-3):
            for c in range(self.COLUMN_COUNT):
                if self.table[r][c] == token and self.table[r+1][c] == token and self.table[r+2][c] == token and self.table[r+3][c] == token:
                    return True

        #checking positively sloped diagonals
        for c in range(self.COLUMN_COUNT-3):
            for r in range(3, self.ROW_COUNT):
                if self.table[r][c] == token and self.table[r-1][c+1] == token and self.table[r-2][c+2] == token and self.table[r-3][c+3] == token:
                    return True

        #checking negatively sloped diagonals
        for c in range(self.COLUMN_COUNT-3):
            for r in range(self.COLUMN_COUNT-3):
                if self.table[r][c] == token and self.table[r+1][c+1] == token and self.table[r+2][c+2] == token and self.table[r+3][c+3] == token:
                    return True


        """
        # POZIOM                    GITUWA
        i = 0
        for i in range(7):
            j = 0
            if self.table[i][j] == -1: # sprawdzam pierwszy element
                licznik = -1
            elif self.table[i][j] == 1:
                licznik = 1
            else:
                licznik = 0
            for j in range(1, 7):
                if licznik < 0 and self.table[i][j]==-1:
                    licznik -= 1
                elif licznik > 0 and self.table[i][j]==1:
                    licznik += 1
                else:
                    licznik = self.table[i][j]

                # sprawdzanie warunku
                if licznik == -4:
                    return -1
                elif licznik == 4:
                    return 1


        # PION                      GITUWA
        j = 0
        for j in range(7):                          # iterowanie w pionie
            i = 0  # sprawdzam pierwszy element
            if self.table[i][j] == -1:
                licznik = -1
            elif self.table[i][j] == 1:
                licznik = 1
            else:
                licznik = 0
            for i in range(1,7):
                # print('sprawdzam: ', i, " ", j)
                if licznik < 0 and self.table[i][j] == -1:
                    licznik -= 1
                elif licznik > 0 and self.table[i][j] == 1:
                    licznik += 1
                else:
                    licznik = self.table[i][j]
                    # sprawdzanie warunku
                if licznik == -4:
                    return -1
                elif licznik == 4:
                    return 1

        cols, rows = (7, 7)

        # Check main diagonals (top-left to bottom-right)
        for start_col in range(cols - 3):
            for start_row in range(rows - 3):
                if all(self.table[start_row + i][start_col + i] == 1 for i in range(4)):
                    return True
                if all(self.table[start_row - i][start_col + i] == -1 for i in range(4)):
                    return True

        # Check secondary diagonals (bottom-left to top-right)
        for start_col in range(cols - 3):
            for start_row in range(3, rows):
                if all(self.table[start_row - i][start_col + i] == 1 for i in range(4)):
                    return True
                if all(self.table[start_row - i][start_col + i] == -1 for i in range(4)):
                    return True




        return False

        #SKOS PRAWO DÓŁ
        start = 0
        for start in range(0,7):                    # iterowanie po poczatkowych gornych polach
            licznik = self.table[start][0]
            for i in range(start+1, 7):             # iterowanie na ukos
                for j in range (1, 7):
                    if i < 7 and j < 6:
                        if licznik < 0 and self.table[i][j]==-1:
                            licznik -= 1
                        elif licznik > 0 and self.table[i][j] == 1:
                            licznik += 1
                        else:
                            licznik = self.table[i][j]

                        # sprawdzanie warunku
                        if licznik == -4:
                            return -1
                        elif licznik == 4:
                           return 1

        #SKOS LEWO DÓŁ
        start = 6
        for start in range(6, -1, -1):  # iterowanie po poczatkowych gornych polach od konca
            licznik = self.table[start][0]
            for i in range(start - 1, -1, -1):  # iterowanie na ukos
                for j in range(1, 7):
                    if 7 > i >= 0 and 7 > j >= 0:
                        if licznik < 0 and self.table[i][j] == -1:
                            licznik -= 1
                        elif licznik > 0 and self.table[i][j] == 1:
                            licznik += 1
                        else:
                            licznik = self.table[i][j]

                        # sprawdzanie warunku
                        if licznik == -4:
                            return -1
                        elif licznik == 4:
                            return 1


            """
