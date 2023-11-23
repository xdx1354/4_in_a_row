# This class will simulate working with database
# All data will be stored as txt files for now
# In the future I might change it to real SQL DB

"""
Players_list must be in format:
player_name;player_id;player_rating
"""

class DataBase(object):
    def __init__(self):
        self.path = './data/'
        self.table_of_players = []


    def getPlayersDB(self):
        """
        list will contain:
        Player's name
        Player's ID
        Player's rating
        :return: 2dim list
        """
        table_of_players = []
        with open(self.path + 'players_list.txt', 'r') as file:
            line = file.readline()

            while line:
                table_of_players.append(line.strip().split(';'))
                line = file.readline()

        self.table_of_players = table_of_players # may not be needed
        return table_of_players

    def savePlayerList(self, table_of_players):

        with open(self.path + 'players_list.txt', 'w') as file:
            for i in range(len(table_of_players)):
                line = ''
                j = 0
                for j in range(len(table_of_players.get(i)) -1 ):   # iterate despite last field to prevent putting unnecessary semicolon at the end
                    line += table_of_players.get(i).get(j) + ';'

                line += table_of_players.get(i).get(j+1) + '\n'     # inserting newline
                file.write(line)

    def getPlayersTuple(self):
        """

        :return: tupel (player_name, player_ID)
        """
        table_of_tuples = []
        with open(self.path + 'players_list.txt', 'r') as file:
            line = file.readline()

            while line:
                temp = line.strip().split(';')
                temp_tuple = (temp[0], temp[1])
                table_of_tuples.append(temp_tuple)
                line = file.readline()

        self.table_of_players = table_of_tuples  # may not be needed
        return table_of_tuples


