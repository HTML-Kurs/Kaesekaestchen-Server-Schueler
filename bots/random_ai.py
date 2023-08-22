from game import *
import random

def get_move(state:GameState, player:Player, time:float) -> Move:
    moves = state.get_possible_moves(player)
    chosen = random.choice(moves)
    return chosen
