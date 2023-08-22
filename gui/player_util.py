import copy
from pydoc import importfile
import time
from threading import Thread
from game import GameState, Move
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
        if state.current_player.name != botname:
            time.sleep(0.1)
            continue
        copy_state = copy.deepcopy(state)
        start = time.time()
        try:
            c_m = ai.get_move(copy_state, copy_state.current_player, max_time)
            if c_m.line.dir == "horizontal":
                m = Move(state.hor_lines[c_m.line.x][c_m.line.y], state.current_player)
            else:
                m = Move(state.ver_lines[c_m.line.x][c_m.line.y], state.current_player)
        except:
            state.current_player.opponent.score = state.size ** 2 - state.current_player.score
            break
        end = time.time()
        if end - start > max_time:
            state.current_player.opponent.score = state.size ** 2 - state.current_player.score
            break
        state.perform(m)
    return state.get_winner().id
