from table import Table as t
print('4 IN A ROW GAME')

tab = t()
tab.printTable()

# menuVar = 1
# while(menuVar):
#       raw = input("Wybierz do ktorego pola chcesz wstawić kolko. (0-6):")
#       if raw!='x':
#             inputList = raw.split()
#             xAxis = int(inputList[0])
#             yAxis = int(inputList[1])
#             """TODO: nie sprawdzam liczby i poprawnosci podanych danych"""
#             tab.move(1,xAxis, yAxis)
#             tab.printTable()
#             if tab.checkWinCon():
#                   print('WYGRANA')
#                   break
#       else:
#             print('koniec')

game_over = False
turn = 0
while not game_over:

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




