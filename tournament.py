import game
import gui
import os
import time

max_time = 1.5
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
            start = time.time()
            try:
                m = playd[state.currentPlayer].get_move(state, state.currentPlayer, max_time)
            except:
                state.currentPlayer.opponent.score = state.size ** 2 - state.currentPlayer.score
                break
            end = time.time()
            if end - start > max_time:
                state.currentPlayer.opponent.score = state.size ** 2 - state.currentPlayer.score
                break
            state.perform(m)
        scores[state.get_winner().name][0] += 1
        scores[bot1][1] += state.player1.score
        scores[bot2][1] += state.player2.score

        plot()

input()