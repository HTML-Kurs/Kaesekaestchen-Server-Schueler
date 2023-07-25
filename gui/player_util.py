from pydoc import importfile
import time
from threading import Thread
from game import GameState
from gui.game_window import create_window


def create_ai(path):
    return importfile(path)

player1_s = 0
player2_s = 0
def create_game(bot, t, both):
    ai = create_ai(bot)
    if both: state = GameState(5, bot, "Player")
    else: state = GameState(5, "Player", bot)

    Thread(target=game_loop, args=(state, ai, t, bot)).start()
    create_window(state, 0, 0, player_move=True)
    create_window(state, 0, 0, True)

def game_loop(state: GameState, ai, max_time, botname):
    while state.get_winner() is None:
        if state.currentPlayer.name != botname:
            time.sleep(0.1)
            continue
        start = time.time()
        try:
            m = ai.get_move(state, state.currentPlayer, max_time)
        except:
            state.currentPlayer.opponent.score = state.size ** 2 - state.currentPlayer.score
            break
        end = time.time()
        if end - start > max_time:
            state.currentPlayer.opponent.score = state.size ** 2 - state.currentPlayer.score
            break
        state.perform(m)
    return state.get_winner().id
