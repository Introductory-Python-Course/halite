import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random

myID, game_map = hlt.get_init()
hlt.send_init("MyPythonBot")

while True:
    game_map.get_frame()

    moves = []

    ########### Your code goes here ###########

    for square in game_map:
        if square.owner == myID:
            moves.append(Move(square, random.choice((NORTH, EAST, SOUTH, WEST, STILL))))

    ########### Your code ends here ###########

    hlt.send_frame(moves)
