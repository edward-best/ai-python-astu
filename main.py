from game import session
from color import Color

board = [[Color.EMPTY for j in range(8)] for i in range(8)]

result = session(board)