import math
import sys

from table import Table as t
import pygame
print('4 IN A ROW GAME')




tab = t()
tab.draw_board()
tab.printTable()



game_over = False
turn = 0
while not game_over:

      for event in pygame.event.get():
            if event.type == pygame.QUIT:                   # gdy wyjscie
                  sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:        # gdy klik

                  if turn == 0:
                        again = 1
                        while again == 1:
                              selection = int(math.floor(event.pos[0]/100))
                              if tab.move(1,int(selection)):
                                    again = 0
                              else:
                                    print("Wybrana kolumna jest pelna, wybierz inna")
                                    again = 1

                  else:
                        again = 1
                        while again == 1:
                              selection = int(math.floor(event.pos[0]/100))

                              if tab.move(2,int(selection)):
                                    again = 0
                              else:
                                    print("Wybrana kolumna jest pelna, wybierz inna")
                                    again = 1


                  tab.printTable()

                  # check wincon
                  if tab.checkWinCon(turn + 1):
                        print('Gracz ', turn + 1, ' wygrywa!')
                        game_over = True

                  turn += 1
                  turn %= 2


      """ czesc konsolowa
      if turn == 0:
            again = 1
            while again == 1:
                  selection = (input("P1: Wybierz do ktorej kolumny chcesz wstawić kolko. (0-6):"))
                  if selection.isdigit() and 0 <= int(selection) < 7:                   # sprawdzam poprawnosc danych
                        if tab.move(1, int(selection)):     # jesli jest gdzie wstawic token                                                             # TODO: While sprawdzajacy poprawnosc danych
                              again = 0
                        else:
                              print("Wybrana kolumna jest pelna, wybierz inna")
                              again = 1
                  else:
                        print("Podano niepoprawne dane")
                        again = 1

      else:
            again = 1
            while again == 1:
                  selection = (input("P2: Wybierz do ktorej kolumny chcesz wstawić kolko. (0-6):"))
                  if selection.isdigit() and 0 <= int(selection) < 7:  # sprawdzam poprawnosc danych
                        if tab.move(2,int(selection)):  # jesli jest gdzie wstawic token                                                             # TODO: While sprawdzajacy poprawnosc danych
                              again = 0
                        else:
                              print("Wybrana kolumna jest pelna, wybierz inna")
                              again = 1
                  else:
                        print("Podano niepoprawne dane")
                        again = 1

      tab.printTable()

      #check wincon
      if tab.checkWinCon(turn+1):
            print('Gracz ', turn+1, ' wygrywa!')
            game_over = True

      turn += 1
      turn %= 2
      """




