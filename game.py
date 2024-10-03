from color import Color

class Game:
    def __init__(self, board: list[list[Color]]):
        self.board = board
    
    def start(self) -> dict:
        return {"winner" : "not you"}
