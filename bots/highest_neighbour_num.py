# Highes Neighbour Num
from game import *
import random

def get_move(state:GameState, player:Player, time:float) -> Move:
    moves = state.get_possible_moves(player)
    primary_max = 0
    secondary_max = 0
    best_move = moves[0]

    for move in moves:
        d = [f.filled_line_num() for f in move.line.fields]
        if primary_max < max(d):
            primary_max = max(d)
            secondary_max = min(d)
            best_move = move
        elif primary_max == max(d) and secondary_max < min(d):
            primary_max = max(d)
            secondary_max = min(d)
            best_move = move

    return best_move