import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random


myID, game_map = hlt.get_init()
hlt.send_init("MyPythonBot")

while True:
    game_map.get_frame()

    moves = []
    for square in game_map:
        if square.owner == myID and square.strength > 5:
            moves.append(Move(square, random.choice((NORTH, EAST))))

    hlt.send_frame(moves)
