# Ranked Minimax Solver
import math

from game import *

def get_move(state:GameState, player:Player, time:float) -> Move:
    return minimax(state, player, 3)[0]

ranking = [22, 21, 20, 00, 10, 11, 30, 31, 32, 33]
#ranking = [22, 20, 21, 10, 00, 11 , 30, 31, 32, 33]
def rank_move(move:Move) -> float:
    d = [f.filled_line_num() for f in move.line.fields]
    return ranking.index( max(d) * 10 + min(d))


def minimax(state:GameState, player:Player, depth:int, alpha=-math.inf, beta=math.inf, end_score=0) -> (Move, float):
    if state.get_winner() is not None:
        if state.get_winner() == player:
            return None, math.inf
        else:
            return None, -math.inf
    if depth == 0:
        return None, end_score

    possible_moves = state.get_possible_moves(state.currentPlayer)
    best_move = possible_moves[0]
    best_score = 0
    if state.currentPlayer == player:
        best_score = -math.inf
        for move in possible_moves:
            s = rank_move(move)
            state.perform(move)
            _, score = minimax(state, player, depth-1, alpha, beta, end_score+1.4**(depth-1)*s)
            state.undo_last_move()
            if score > best_score:
                best_score = score
                best_move=move
            alpha = max(alpha, score)
            if alpha >= beta:
                break
    else:
        best_score = math.inf
        for move in possible_moves:
            s = rank_move(move)
            state.perform(move)
            _, score = minimax(state, player, depth - 1, alpha, beta, end_score - 1.4**(depth-1)*s)
            state.undo_last_move()
            if score < best_score:
                best_score = score
                best_move = move
            beta = min(beta, score)
            if alpha >= beta:
                break

    return best_move, best_score
