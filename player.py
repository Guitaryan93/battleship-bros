''' Player class takes care of all the player data. How many ships remain, who's turn it is, etc... '''

from grid import Grid
from random import randint


class Player:
    def __init__(self, is_human, name):
        self.name = name
        self.attack_grid = Grid(self)   # Displays all previous hits and misses
        self.ship_grid = Grid(self)     # Displays the players ships and the opponents hits/misses
        self.turn = None            # Is it the players turn to play?
        self.is_human = is_human    # Humans get asked for player input!
        self.ships = []
        self.hp = 0
        self.current_hit_coords = ""
        self.attack_list = []
        self.hit_count = 0          # Keep track of hits while attack_list is in use
        self.failsafe_count = 0     # AI can get stuck in a loop... This count is to force a break out of these loops

    def get_hitpoints(self):
        for ship in self.ships:
            self.hp += ship.size

    def get_random_coords(self):
        ''' For computer player, build a pair of random coordinates '''
        rand_x = self.attack_grid.x_labels[randint(0, len(self.attack_grid.x_labels) - 1)]
        rand_y = self.attack_grid.y_labels[randint(0, len(self.attack_grid.y_labels) - 1)]
        rand_coords = rand_x + rand_y

        return rand_coords

    def create_attack_list(self, start_coords):
        self.current_hit_coords = start_coords
        cur_x = start_coords[0].upper()
        cur_y = start_coords[1]

        if not self.attack_grid.x_labels.index(cur_x) + 1 > len(self.attack_grid.x_labels) - 1:
            next_x = self.attack_grid.x_labels.index(cur_x) + 1
            self.attack_list.append(f"{self.attack_grid.x_labels[next_x]}{cur_y}")

        if not self.attack_grid.x_labels.index(cur_x) - 1 < 0:
            next_x = self.attack_grid.x_labels.index(cur_x) - 1
            self.attack_list.append(f"{self.attack_grid.x_labels[next_x]}{cur_y}")

        if not self.attack_grid.y_labels.index(cur_y) + 1 > len(self.attack_grid.y_labels) - 1:
            next_y = self.attack_grid.y_labels.index(cur_y) + 1
            self.attack_list.append(f"{cur_x}{self.attack_grid.y_labels[next_y]}")

        if not self.attack_grid.y_labels.index(cur_y) - 1 < 0:
            next_y = self.attack_grid.y_labels.index(cur_y) - 1
            self.attack_list.append(f"{cur_x}{self.attack_grid.y_labels[next_y]}")

    def check_remaining_ships(self, opponent):
        ''' Check if the biggest ship size has been reached '''
        biggest_ship = 0
        for ship in opponent.ships:
            if ship.hp > 0 and ship.size > biggest_ship:
                biggest_ship = ship.size

        # Reset AI attack before their turn. No need to keep looking for ships that have been destroyed.
        if self.hit_count >= biggest_ship:
            self.attack_list = []
            self.hit_count = 0
            self.current_hit_coords = ""

    def update_attack_list(self, player_input):
        ''' Update attack list to search on the same axis. '''
        if player_input[0].upper() == self.current_hit_coords[0].upper():
            search_vertical = True
            bigger_coord = player_input if self.attack_grid.y_labels.index(player_input[1]) > self.attack_grid.y_labels.index(
                self.current_hit_coords[1]) else self.current_hit_coords
            smaller_coord = player_input if self.attack_grid.y_labels.index(player_input[1]) < self.attack_grid.y_labels.index(
                self.current_hit_coords[1]) else self.current_hit_coords

        elif player_input[1] == self.current_hit_coords[1]:
            search_vertical = False
            bigger_coord = player_input if self.attack_grid.x_labels.index(player_input[0].upper()) > self.attack_grid.x_labels.index(
                self.current_hit_coords[0].upper()) else self.current_hit_coords
            smaller_coord = player_input if self.attack_grid.x_labels.index(player_input[0].upper()) < self.attack_grid.x_labels.index(
                self.current_hit_coords[0].upper()) else self.current_hit_coords

        else:
            return

        self.attack_list = []
        if search_vertical:
            if not self.attack_grid.y_labels.index(bigger_coord[1]) + 1 > len(self.attack_grid.y_labels) - 1:
                next_y = self.attack_grid.y_labels.index(bigger_coord[1]) + 1
                self.attack_list.append(f"{bigger_coord[0]}{self.attack_grid.y_labels[next_y]}")

            if not self.attack_grid.y_labels.index(smaller_coord[1]) - 1 < 0:
                next_y = self.attack_grid.y_labels.index(smaller_coord[1]) - 1
                self.attack_list.append(f"{smaller_coord[0]}{self.attack_grid.y_labels[next_y]}")
        else:
            if not self.attack_grid.x_labels.index(bigger_coord[0].upper()) + 1 > len(self.attack_grid.x_labels) - 1:
                next_x = self.attack_grid.x_labels.index(bigger_coord[0].upper()) + 1
                self.attack_list.append(f"{self.attack_grid.x_labels[next_x]}{bigger_coord[1]}")

            if not self.attack_grid.x_labels.index(smaller_coord[0].upper()) - 1 < 0:
                next_x = self.attack_grid.x_labels.index(smaller_coord[0].upper()) - 1
                self.attack_list.append(f"{self.attack_grid.x_labels[next_x]}{smaller_coord[1]}")

class Battleship:
    def __init__(self, num, name, size):
        self.num = num
        self.name = name
        self.size = size
        self.hp = size
        self.facing = ""
        self.placed = False
        self.coords = []

