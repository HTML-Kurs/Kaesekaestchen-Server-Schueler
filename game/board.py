from game.move import Move
from game.player import *


class GameState:

    def __init__(self, size: int, p1_name: str, p2_name: str):

        # create players
        self.player1 = Player(p1_name, 1, "#ff0000")
        self.player2 = Player(p2_name, 2, "#0000ff")
        self.player1.opponent = self.player2
        self.player2.opponent = self.player1

        self.size = size

        self.hor_lines: list(list(Line)) = []
        for x in range(self.size):
            self.hor_lines.append([])
            for y in range(self.size + 1):
                self.hor_lines[x] = Line("horizontal", x, y, self)

        self.ver_lines: list(list(Line)) = []
        for x in range(self.size + 1):
            self.ver_lines.append([])
            for y in range(self.size):
                self.ver_lines[x] = Line("vertical", x, y, self)

        # create quads
        self.fields = []
        for x in range(size):
            self.fields.append([])
            for y in range(size):
                self.fields[x].append(Field(x, y, self))

        self.currentPlayer = self.player1
        self.turn = 1

    def move_is_valid(self, move: Move):
        return move.line.owner is None

    def move_fills_field(self, move: Move):
        for f in move.line.fields:
            if f.filled_line_num() == 3:
                return True
        return False



class Field:

    def __init__(self, x: int, y: int, state: GameState):
        self.x = x
        self.y = y
        self.owner: Player = None
        self.state = state
        self.lines: list(Line) = []
        self.connect_to_lines()

    def connect_to_lines(self):
        self.lines.append(self.state.hor_lines[self.x])
        self.lines.append(self.state.hor_lines[self.x + 1])
        self.lines.append(self.state.hor_lines[self.y])
        self.lines.append(self.state.hor_lines[self.y + 1])
        for line in self.lines:
            line.fields.append(self)

    def get_right_line(self):
        return self.lines[0]

    def get_left_line(self):
        return self.lines[1]

    def get_bottom_line(self):
        return self.lines[2]

    def get_top_line(self):
        return self.lines[3]

    def is_filled(self):
        return self.filled_line_num() == 4

    def filled_line_num(self):
        return len([l for l in self.lines if l.owner is not None])


class Line:

    def __init__(self, dir, x: int, y: int, state: GameState):
        self.dir = dir
        self.x = x
        self.y = y
        self.owner: Player = None
        self.state = state
        self.fields: list(Field) = []
