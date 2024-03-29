from table import Table as tab
from elo_algorithm import Elo_algorithm as elo
t = tab()


# 2 should win positive diag
t.table=[   [0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 2, 0],
            [0, 2, 1, 0, 2, 0, 0],
            [1, 1, 1, 2, 0, 0, 0],
            [2, 1, 1, 2, 0, 0, 0],
            [1, 2, 2, 2, 0, 0, 0] ]
assert t.checkWinCon(2) == True

# 2 should win horiz
t.table = [ [2, 2, 2, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0] ]
assert t.checkWinCon(2) == True

# 1 should win vert
t.table = [ [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0] ]
assert t.checkWinCon(1) == True

# 1 should win vert
t.table = [ [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0] ]
assert t.checkWinCon(1) == True

# 2 should win neg-diag
t.table = [ [2, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0] ]
assert t.checkWinCon(2) == True

# 2 should win neg-diag
t.table = [ [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 0] ]
assert t.checkWinCon(2) == True

# 1 should win pos-diag
t.table = [ [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0] ]
assert t.checkWinCon(1) == True


elo = elo()

r1 = 1000
r2 = 1400

print(elo.eloRating(r1, r2, 60, 2)) #good
