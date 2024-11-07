from game import session
from color import Color
import importlib
import pkgutil
import random
import copy

discovered_bots = [
    (owner, importlib.import_module(owner))
    for finder, owner, ispkg
    in pkgutil.iter_modules()
    if owner.startswith('bot_')
]

random.shuffle(discovered_bots)

def init_game_board():
    board = [[Color.EMPTY for j in range(8)] for i in range(8)]
    board[3][4] = Color.BLACK
    board[4][3] = Color.BLACK
    board[3][3] = Color.WHITE
    board[4][4] = Color.WHITE
    return board

def divide(bots):
    new = bots
    result = []
    starter_index = 2
    if len(new) > 2 and len(new) % 2 == 1:
        result.append(new[0:3])
        starter_index += 1
    else:
        result.append(new[0:2])
    for i in range(starter_index, len(new), 2):
        result.append(new[i:i+2])
    return result

def get_winner(obj):
    winner_name = None
    winner_score = 0
    for winner, score in obj.items():
        if score >= winner_score:
            winner_name = winner
            winner_score = score
    return winner_name

def group_stage(playing_bots):
    results = []
    obj = {key[1].__name__: 0 for key in playing_bots}
    print(" vs ".join([key[1].__name__ for key in playing_bots]))
    if len(playing_bots) == 2:
        board = init_game_board()
        results.append(session(board, playing_bots[0][1], playing_bots[1][1]))
    else:
        results.append(group_stage(playing_bots[0:2]))
        results.append(group_stage([playing_bots[0], playing_bots[2]]))
        results.append(group_stage(playing_bots[1:3]))

    if len(playing_bots) == 2:
        for result in results:
            obj[result["first bot"]] += result["stat"][result["first bot"]]
            obj[result["second bot"]] += result["stat"][result["second bot"]]
    else:
        for result in results:
            for k, v in result.items():
                obj[k] += v

    return obj

i = 1
while len(discovered_bots) > 1:
    print("Раунд ", i)
    divided = divide(discovered_bots)
    winners = []
    for group in divided:
        obj = group_stage(group)
        winner = get_winner(obj)
        print("Победитель ", winner)
        winners.append(winner)
    discovered_bots = [bot for bot in discovered_bots if bot[0] in winners]
    i += 1