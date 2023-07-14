from game.board import Line, Field
from game.player import Player

class Move:
    def __init__(self, l:Line, player:Player):
        self.line = l
        self.player = player

    def is_valid(self):
        return self.line.owner is None

    def get_filling_fields(self) -> list(Field):
        k = []
        for f in self.line.fields:
            if f.filled_line_num() == 3:
                k.append(f)
        return k
    def move_fills_field(self):
        return len(self.get_filling_fields()) == 0
