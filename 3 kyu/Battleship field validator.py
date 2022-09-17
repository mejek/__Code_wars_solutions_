# Description:
#
# Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.
#
# Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.
#
# Before the game begins, players set up the board and place the ships accordingly to the following rules:
#
#     There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
#     Each ship must be a straight line, except for submarines, which are just single cell.
#     The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.
#
# My solution:
def validate_battlefield(field):
    # border check
    for x in range(10):
        for y in range(10):
            if field[x][y] == 1:
                if x > 0 and x < 9 and y > 0 and y < 9:
                    if field[x - 1][y - 1] == 1 or field[x - 1][y + 1] == 1 or field[x + 1][y - 1] == 1 \
                            or field[x + 1][y + 1] == 1:
                        return False
                elif x == 0 and y == 0:
                    if field[x + 1][y + 1] == 1:
                        return False
                elif x == 9 and y == 9:
                    if field[x - 1][y - 1] == 1:
                        return False
                elif x == 0 and y == 9:
                    if field[x + 1][y - 1] == 1:
                        return False
                elif x == 9 and y == 0:
                    if field[x - 1][y + 1] == 1:
                        return False
                elif x == 0 and y > 0 and y < 9:
                    if field[x + 1][y + 1] == 1 or field[x + 1][y - 1] == 1:
                        return False
                elif x == 9 and y > 0 and y < 9:
                    if field[x - 1][y - 1] == 1 or field[x - 1][y + 1] == 1:
                        return False
                elif y == 0 and x > 0 and x < 9:
                    if field[x + 1][y + 1] == 1 or field[x - 1][y + 1] == 1:
                        return False
                elif y == 9 and x > 0 and x < 9:
                    if field[x + 1][y - 1] == 1 or field[x - 1][y - 1] == 1:
                        return False

    # ships count
    ships = 0
    for x in field:
        ships += x.count(1)
    if ships != 20:
        return False

    # ships lenght rows
    rows = []
    for x in field:
        rows.append(''.join(str(i) for i in x))

    for y in range(10):
        col = ''
        for x in range(10):
            col += str(field[x][y])
        rows.append(col)
    for n in range(2, 11):
        sum = 0
        for row in rows:
            for ship in row.split('0'):
                if ship == '1' * n:
                    sum += 1
        if n == 2 and sum != 3:
            return False
        elif n == 3 and sum != 2:
            return False
        elif n == 4 and sum != 1:
            return False
        elif n >= 5 and sum != 0:
            return False
    return True