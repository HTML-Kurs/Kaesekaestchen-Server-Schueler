import copy

import game
import gui
import os
import time

from game import Move

max_time = 5.0
bots = gui.load_bots()
scores = {key: [0, 0] for key in bots}

def plot():
    os.system('cls')
    global scores
    scores = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1]).__reversed__()}
    print("         Bot                        Wins       Score")
    for key, value in scores.items():
        print(str(key).ljust(38, " "),
              str(value[0]).ljust(10, " "),
              str(value[1])
        )

plot()
for bot1 in bots:
    for bot2 in bots:
        if bot1==bot2:
            continue
        ai1 = gui.util.create_ai(bot1)
        ai2 = gui.util.create_ai(bot2)
        state = game.GameState(5, bot1, bot2)
        playd = {state.player1: ai1, state.player2: ai2}
        while state.get_winner() is None:
            copy_state = copy.deepcopy(state)
            start = time.time()
            try:
                c_m = playd[state.current_player].get_move(copy_state, copy_state.current_player, max_time)
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
        scores[state.get_winner().name][0] += 1
        scores[bot1][1] += state.player1.score
        scores[bot2][1] += state.player2.score

        plot()

input()