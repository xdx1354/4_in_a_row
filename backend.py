

class Backend(object):
    def __init__(self, cols, rows):
        self.last_placed_token_pos = (-1, -1)
        self.COLUMN_COUNT = cols
        self.ROW_COUNT = rows
        self.table = [[0 for i in range(self.COLUMN_COUNT)] for j in range(self.ROW_COUNT)]

    def passTable(self):
        return self.table


    def printTable(self):
        """
        Printing on CLI the view of table. Used after next move.
        """
        for i in range(0, 7):
            print(i,'|', end='')
        print()
        for i in range(0,6):
            print(self.table[i])

    def checkCol(self,col):
        """
        Checking if column is not full
        :param col: colum where player wants to put the token
        :return: true: if not full, false: if full
        """
        if self.table[0][col] == 0:
            return True
        else:
            return False

    def findEmptyRow(self, col):
        """
        :param col: Column choosen by player.
        :return: first looking from bottom empty row. The token will be added to [return][col]
        """
        for r in reversed(range(self.ROW_COUNT)):
            if self.table[r][col] == 0:
                return r

    def placeToken(self, col, token):

        """
        :param col: col where the token will be dropped
        :param token: token of current player
        :return: no return
        Just placing a token into an array. Plain backend. Updating last_placed_token_pos field
        which will be accessed in gui
        """
        xPos = int(self.findEmptyRow(col))
        yPos = int(col)
        self.table[xPos][yPos] = token
        self.last_placed_token_pos = (xPos, yPos)


    def move(self, token, col):
        """
        :param token: its -1 if player's no2 and 1 if player's no1
        :param col: col picked by a player
        :return: true for successful move, false if no legal move can be made
        """

        if self.checkCol(col):                  # sprawdzenie czy jest wolne miejsce w danej kolumnie
            self.placeToken(col, token)         # wstawienie tokena w pierwsze wolne pole od dołu
            return True                         # zakonczono sukcesem
        else:
            return False                        # zakonczono porażką

    def clearTable(self):
        """
        clearing backend table
        :return: no return
        """
        self.table = [[0 for i in range(self.COLUMN_COUNT)] for j in range(self.ROW_COUNT)]

    def checkWinCon(self, token):
        """
        Works only for specific dimension of an array (7x6)
        :param token: currently dropped token
        :return: true: if win con found, false: if not
        """

        # checking horizontal
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(self.ROW_COUNT):
                if self.table[r][c] == token and self.table[r][c + 1] == token and self.table[r][c + 2] == token and \
                        self.table[r][c + 3] == token:
                    return True

        # checking vertical
        for r in range(self.ROW_COUNT - 3):
            for c in range(self.COLUMN_COUNT):
                if self.table[r][c] == token and self.table[r + 1][c] == token and self.table[r + 2][c] == token and \
                        self.table[r + 3][c] == token:
                    return True

        # checking positively sloped diagonals
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(3, self.ROW_COUNT):
                if self.table[r][c] == token and self.table[r - 1][c + 1] == token and self.table[r - 2][
                    c + 2] == token and self.table[r - 3][c + 3] == token:
                    return True

        # checking negatively sloped diagonals
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(self.COLUMN_COUNT - 3):
                if self.table[r][c] == token and self.table[r + 1][c + 1] == token and self.table[r + 2][
                    c + 2] == token and self.table[r + 3][c + 3] == token:
                    return True


    def tabPosToScreenPos(self, x, y):
        """
        :param x: table[x][y] first argument of position in table CLI
        :param y: table[x][y] second argument
        :return: transposed to position on screen. Screen is fixed to 700x700 [px]
        """
        xScreen = int (y*100 + 4)
        yScreen = int(x*100 + 108)
        return xScreen, yScreen