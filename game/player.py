

class Player:

    def __init__(self, name:str, id:int, color:(int, int, int)):
        self.name = name
        self.id = id
        self.color = color
        self.opponent:Player = None
        self.score = 0

