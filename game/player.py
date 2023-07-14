

class Player:

    def __init__(self, name:str, id:int, color:str):
        self.name = name
        self.id = id
        self.color = color
        self.opponent:Player = None

