# Minimax Solver
import math

from game import *

def get_move(state:GameState, player:Player, time:float) -> Move:
    return minimax(state, player, 3)[0]


def score_position(state:GameState, player:Player) -> float:
    score = player.score - player.opponent.score
    if player == state.currentPlayer:
        for r in state.fields:
            for f in r:
                if f.filled_line_num() == 3:
                    score += 0.9
    else:
        for r in state.fields:
            for f in r:
                if f.filled_line_num() == 3:
                    score -= 0.9
    return score


def minimax(state:GameState, player:Player, depth:int, alpha=-math.inf, beta=math.inf) -> (Move, float):
    if state.get_winner() is not None:
        if state.get_winner() == player:
            return None, math.inf
        else:
            return None, -math.inf
    if depth == 0:
        return None, score_position(state, player)

    possible_moves = state.get_possible_moves(state.currentPlayer)
    best_move = possible_moves[0]
    best_score = 0
    if state.currentPlayer == player:
        best_score = -math.inf
        for move in possible_moves:
            state.perform(move)
            _, score = minimax(state, player, depth-1, alpha, beta)
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
            state.perform(move)
            _, score = minimax(state, player, depth - 1, alpha, beta)
            state.undo_last_move()
            if score < best_score:
                best_score = score
                best_move = move
            beta = min(beta, score)
            if alpha >= beta:
                break

    return best_move, best_score
