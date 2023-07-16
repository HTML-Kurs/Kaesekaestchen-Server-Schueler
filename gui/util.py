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
def create_game(bot1, bot2, t, rnds):
    ai1 = create_ai(bot1)
    ai2 = create_ai(bot2)

    global player1_s
    global player2_s
    player1_s = 0
    player2_s = 0
    
    for i in range(rnds):
        state = GameState(5, bot1, bot2)
        playd = {state.player1: ai1, state.player2: ai2}
        Thread(target=exec_get_score, args=(state, playd, t)).start()
        create_window(state, player1_s, player2_s)
    create_window(state, player1_s, player2_s, True)

def exec_get_score(state, playerdict, t):
    global player2_s
    global player1_s
    k = game_loop(state, playerdict, t)
    if k == 1:
        player1_s += 1
    else:
        player2_s += 1

def game_loop(state: GameState, playerdict, t):
    print("[Game Started]")
    for _ in range(state.max_turns):
        print()
        print(f"Requesting move from {state.currentPlayer.name}")
        start = time.time()
        m = playerdict[state.currentPlayer].get_move(state, state.currentPlayer)
        end = time.time()
        if end - start > t:
            print("TIME_LOSS")
            print("Winner: " + playerdict[state.currentPlayer].opponent.name
                  + " -> " + str(playerdict[state.currentPlayer].opponent.name.id))
            return playerdict[state.currentPlayer].opponent.name.id
        print(f"Got move after {end - start} seconds")
        time.sleep(t - end + start)
        state.perform(m)
    print("Winner: " + state.get_winner().name + " -> " + str(state.get_winner().id))
    return state.get_winner().id
