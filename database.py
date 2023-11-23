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
            for player_data in table_of_players:
                line = ''
                for i in range(len(player_data) - 1):  # Iterate over each element in player_data except the last one
                    line += str(player_data[i]) + ';'  # Assuming player_data contains strings or convertible values

                line += str(player_data[-1]) + '\n'  # Add the last element and a newline
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


