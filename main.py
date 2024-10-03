from game import Game
from color import Color

board = [[Color.EMPTY for j in range(8)] for i in range(8)]

game = Game(board)

result = game.start()