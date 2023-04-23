''' Player class takes care of all the player data. How many ships remain, who's turn it is, etc... '''


class Player:
    def __init__(self, is_human):
        self.turn = True            # Is it the players turn to play?
        self.is_human = is_human    # Humans get asked for player input!
        self.ships = []


class Battleship:
    def __init__(self, num, name, size):
        self.num = num
        self.name = name
        self.size = size
        self.facing = ""
        self.placed = False
        self.coords = []

