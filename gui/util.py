import threading
from pydoc import importfile
import time
from threading import Thread
from game import GameState
from gui.game_window import create_window


def create_ai(path):
    return importfile(path)

player1_s = 0
player2_s = 0
def create_game(bot1, bot2, t, both, tv):
    ai1 = create_ai(bot1)
    ai2 = create_ai(bot2)
    state = GameState(5, bot1, bot2)
    playd = {state.player1: ai1, state.player2: ai2}
    Thread(target=game_loop, args=(state, playd, t, tv)).start()
    create_window(state, 0, 0)
    player1_s = state.player1.score
    player2_s = state.player2.score

    if both:
        state = GameState(5, bot2, bot1)
        playd = {state.player1: ai2, state.player2: ai1}
        Thread(target=game_loop, args=(state, playd, t, tv)).start()
        create_window(state, player2_s, player1_s, True)
    else:
        create_window(state, 0, 0, True)

def game_loop(state: GameState, playerdict, t, tv):
    print("[Game Started]")
    for _ in range(state.max_turns):
        print()
        print(f"Requesting move from {state.currentPlayer.name}")
        start = time.time()
        try:
            m = playerdict[state.currentPlayer].get_move(state, state.currentPlayer, t)
        except:
            print("PRINT_EXCEPTION_LOSS")
            print("Winner: " + state.currentPlayer.opponent.name
                  + " -> " + str(state.currentPlayer.opponent.id))
            state.currentPlayer.opponent.score = state.size ** 2 - state.currentPlayer.score
            return state.currentPlayer.opponent.id
        end = time.time()
        if end - start > t:
            print("TIME_LOSS")
            print("Winner: " + state.currentPlayer.opponent.name
                  + " -> " + str(state.currentPlayer.opponent.id))
            state.currentPlayer.opponent.score = state.size ** 2 - state.currentPlayer.score
            return state.currentPlayer.opponent.id
        print(f"Got move after {end - start} seconds")
        if tv:
            time.sleep(t - end + start)
        state.perform(m)
    print("Winner: " + state.get_winner().name + " -> " + str(state.get_winner().id))
    return state.get_winner().id
