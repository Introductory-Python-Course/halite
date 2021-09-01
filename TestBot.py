import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square, opposite_cardinal
import random

myID, game_map = hlt.get_init()
hlt.send_init("TestBot")

def getDirection(startX, startY, stopX, stopY):
    diffX = startX - stopX
    diffY = startY - stopY

    if abs(diffX) < abs(diffY):
        if diffX > 0:
            return WEST
        return EAST
    else:
        if diffY > 0:
            return NORTH
        else:
            return SOUTH

def getSquareDir(startSquare, stopSquare):
    if startSquare.x > stopSquare.x:
        return WEST
    elif startSquare.x < stopSquare.x:
        return EAST
    elif startSquare.y > stopSquare.y:
        return NORTH
    return SOUTH

while True:
    game_map.get_frame()
    moves = []
    mySquares = []
    x = 0
    y = 0

    for square in game_map:
        if square.owner == myID:
            mySquares.append(square)
            x = x + square.x
            y = y + square.y

    # find center of our side of the map
    x = x / len(mySquares)
    y = y / len(mySquares)

    for square in mySquares:
        if square.strength > 5:
            neighbors = game_map.neighbors(square, 1, False)
            foundEnemy = False

            for neighbor in neighbors:
                if neighbor.owner != myID:
                    foundEnemy = True
                    if neighbor.strength < square.strength:
                        dir = getSquareDir(square, neighbor)
                        moves.append(Move(square, dir))
                        break

            if not foundEnemy:
                dir = opposite_cardinal(getDirection(square.x, square.y, x, y))
                moves.append(Move(square, dir))

    hlt.send_frame(moves)


