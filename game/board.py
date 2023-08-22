from game.player import *

class GameState:

    def __init__(self, size: int, p1_name: str, p2_name: str):

        # create players
        self.player1 = Player(p1_name, 1, (255, 0, 0))
        self.player2 = Player(p2_name, 2, (0, 0, 255))
        self.player1.opponent = self.player2
        self.player2.opponent = self.player1

        self.size = size
        self.all_lines: list(Line) = []
        self.last_moves: list(Move) = []
        self.current_player = self.player1
        self.max_turns = 2 * size * (size + 1)

        self.hor_lines: list[list(Line)] = []
        for x in range(self.size):
            self.hor_lines.append([])
            for y in range(self.size + 1):
                l = Line("horizontal", x, y, self)
                self.hor_lines[x].append(l)
                self.all_lines.append(l)

        self.ver_lines: list[list(Line)] = []
        for x in range(self.size + 1):
            self.ver_lines.append([])
            for y in range(self.size):
                l = Line("vertical", x, y, self)
                self.ver_lines[x].append(l)
                self.all_lines.append(l)

        # create quads
        self.fields = []
        for x in range(size):
            self.fields.append([])
            for y in range(size):
                self.fields[x].append(Field(x, y, self))

    def perform(self, m):
        if m.player != self.current_player:
            print("ERROR: Move Player and Current Player dont match")
            return
        if not m.is_valid():
            print("ERROR: Move is invalid")
            return
        fields = m.get_filling_fields()
        for field in fields:
            field.owner = m.player
            m.player.score += 1
        m.line.owner = m.player
        if len(fields) == 0:
            self.current_player = m.player.opponent
        self.last_moves.append(m)

    def undo_last_move(self):
        m = self.last_moves[-1]
        m.line.owner = None
        fields = m.get_filling_fields()
        for field in fields:
            field.owner = None
            m.player.score -= 1
        self.current_player = m.player
        self.last_moves = self.last_moves[:-1]

    def get_turn(self) -> int:
        return self.max_turns - len([l for l in self.all_lines if l.owner is None])

    def get_winner(self):
        if self.player1.score + self.player2.score < self.size**2:
            return None
        return self.player1 if self.player1.score > self.player2.score else self.player2

    def get_possible_moves(self, player: Player):
        return [Move(l, player) for l in self.all_lines if l.owner is None]



class Field:

    def __init__(self, x: int, y: int, state: GameState):
        self.x = x
        self.y = y
        self.owner: Player = None
        self.state = state
        self.lines: list(Line) = []
        self.connect_to_lines()

    def connect_to_lines(self):
        self.lines.append(self.state.hor_lines[self.x][self.y])
        self.lines.append(self.state.hor_lines[self.x][self.y + 1])
        self.lines.append(self.state.ver_lines[self.x][self.y])
        self.lines.append(self.state.ver_lines[self.x + 1][self.y])
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
        return len(self.get_filled_lines())

    def get_filled_lines(self):
        return [l for l in self.lines if l.owner is not None]

    def get_unfilled_lines(self):
        return [l for l in self.lines if l.owner is None]

class Line:

    def __init__(self, dir, x: int, y: int, state: GameState):
        self.dir = dir
        self.x = x
        self.y = y
        self.owner: Player = None
        self.state = state
        self.fields: list(Field) = []

class Move:
    def __init__(self, l:Line, player:Player):
        self.line = l
        self.player = player

    def is_valid(self):
        return self.line.owner is None

    def get_filling_fields(self):
        k = []
        for f in self.line.fields:
            if f.filled_line_num() == 3:
                k.append(f)
        return k

    def move_fills_field(self):
        return len(self.get_filling_fields()) == 0

