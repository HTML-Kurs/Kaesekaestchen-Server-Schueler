from game import *
import random

def get_move(state:GameState, player:Player) -> Move:
    return random.choice(state.get_possible_moves(player))