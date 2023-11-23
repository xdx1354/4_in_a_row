import random

from database import DataBase as DB
from elo_algorithm import Elo_algorithm as elo

class Backend(object):
    def __init__(self, cols, rows):

        self.last_placed_token_pos = (-1, -1)
        self.COLUMN_COUNT = cols
        self.ROW_COUNT = rows
        self.table = [[0 for i in range(self.COLUMN_COUNT)] for j in range(self.ROW_COUNT)]
        self.winner = -1
        self.db = DB()
        self.playersDB = self.getDB()
        self.players = self.getPlayers()
        self.current_player1 = ''
        self.current_player2 = ''

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
                    self.winner = token
                    return True

        # checking vertical
        for r in range(self.ROW_COUNT - 3):
            for c in range(self.COLUMN_COUNT):
                if self.table[r][c] == token and self.table[r + 1][c] == token and self.table[r + 2][c] == token and \
                        self.table[r + 3][c] == token:
                    self.winner = token
                    return True

        # checking positively sloped diagonals
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(3, self.ROW_COUNT):
                if self.table[r][c] == token and self.table[r - 1][c + 1] == token and self.table[r - 2][
                    c + 2] == token and self.table[r - 3][c + 3] == token:
                    self.winner = token
                    return True

        # checking negatively sloped diagonals
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(self.ROW_COUNT - 3):
                if self.table[r][c] == token and self.table[r + 1][c + 1] == token and self.table[r + 2][
                    c + 2] == token and self.table[r + 3][c + 3] == token:
                    self.winner = token
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

    def getDB(self):
       return self.db.getPlayersDB()

    def getPlayers(self):
        return self.db.getPlayersTuple()

    def addPlayer(self, playerName):
        """
        Adds a new player with specific  name, generates new ID, sets initial value of rating to 1000
        :param playerName: dictionary containg inputs  containing player name
        :return:
        """
        print("Printing name",playerName)
        rawName = playerName
        self.playersDB.append((rawName, int(self.generateID()), int(1000)))

        # push to database
        print(self.playersDB)
        self.db.saveDB(self.playersDB)

    def generateID(self):
        return int(self.playersDB[len(self.playersDB) - 1][1]) + 1

    def getNameFromID(self, playersID):
        for i in range(len(self.playersDB)):
            if int(self.playersDB[i][1]) == playersID:
                return self.playersDB[i][0]

    def getRatingFromID(self, playersID):
        for i in range(len(self.playersDB)):
            if int(self.playersDB[i][1]) == int(playersID):
                return self.playersDB[i][2]
    def getRandomColor(self):
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    def setRating(self, playersID, newRating):
        for i in range(len(self.playersDB)):
            if int(self.playersDB[i][1]) == int(playersID):
                self.playersDB[i][2] = int(newRating)
                self.db.saveDB(self.playersDB)
                break

    def updateRatings(self, whoWon, p1_ID, p2_ID):

        p1_rating = self.getRatingFromID(p1_ID)
        p2_rating = self.getRatingFromID(p2_ID)

        # calculate new ratings
        elo_alg = elo()
        (p1_rating, p2_rating) =elo_alg.eloRating(p1_rating, p2_rating, 1000, whoWon)

        # update database
        self.setRating(p1_ID, p1_rating)
        self.setRating(p2_ID, p2_rating)

