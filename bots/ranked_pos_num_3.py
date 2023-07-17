from game import *
import random

ranking = [22, 21, 20, 00, 10, 11, 30, 31, 32, 33]

def get_move(state:GameState, player:Player, time:float) -> Move:
    moves = state.get_possible_moves(player)
    best_rank = -1
    best_move = moves[0]
    for move in moves:
        d = [f.filled_line_num() for f in move.line.fields]
        k = max(d) * 10 + min(d)
        i = ranking.index(k)
        if i > best_rank:
            best_rank = i
            best_move = move
    return best_move