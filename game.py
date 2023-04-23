''' Class for the overall Game. Takes care of building the game, checking
    game conditions and screen controls, etc... '''

from grid import Grid
from player import Player, Battleship
import os
import re
from time import sleep
from colorama import *


class Game:
    def __init__(self):
        self.ship_count = 5
        self.enemy_grid = Grid()        # Top grid to display hits/misses
        self.player_grid = Grid()       # Bottom grid to show players ships
        self.player_1 = Player(True)
        self.player_2 = Player(False)
        self.players = [self.player_1]   #, self.player_2]
        self.message = ""

        # Game Loop
        self.clear_screen()
        self.setup_ships()
        self.player_turn(self.player_1)

    def clear_screen(self):
        # Clear for Windows (nt) or Linux/Mac OS
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def show_help(self):
        print("How to play Battleship...")

    def show_message(self):
        ''' Show and then reset the screen message for player feedback '''
        print(self.message + Style.RESET_ALL)
        self.message = ""

    def player_turn(self, player):
        # Check for computer / human player
        if player.is_human:
            while player.turn:
                player_input = input("Choose coordinates: ").lower()
                # Put any keywords first or else they will be skipped
                if player_input == "help" or player_input == "h":
                    self.show_help()
                elif player_input == "quit" or player_input == "q":
                    print("Goodbye!")
                    sleep(2)
                    quit()
                # Check that the coordinate is a valid format
                elif self.player_grid.validate_coordinates(player_input):
                    grid_cell = self.player_grid.search_grid(player_input)
                    response = grid_cell.update_cell()
                    self.message = response
                    self.show_message()
                else:
                    self.message = Fore.RED + "Incorrect co-ordinates. Please try again or type \"help\"."
                    self.show_message()

    def setup_ships(self):
        # Loop through each player and setup their ships to start the game
        for player in self.players:
            ship_list = [Battleship(1, "Carrier", 5),
                         Battleship(2, "Battleship", 4),
                         Battleship(3, "Cruiser", 3),
                         Battleship(4, "Submarine", 3),
                         Battleship(5, "Destroyer", 2)]

            while len(player.ships) < self.ship_count:
                self.clear_screen()
                # Show available ships
                print("No. | Ship Name   | Size")
                print("----|-------------|-----")
                for ship in ship_list:
                    if not ship.placed:
                        print(f" {ship.num}  | {ship.name.ljust(11, ' ')} |  {ship.size}")
                self.show_message()

                ship_choice = input("\nChoose a ship to place: ").lower()
                current_ship = None

                for ship in ship_list:
                    if str(ship.num) == ship_choice or ship.name.lower() == ship_choice:
                        current_ship = ship

                if current_ship is None:
                    self.message = Fore.RED + "Invalid choice. Try again."
                    continue
                elif current_ship.placed:
                    self.message = "This ship has already been placed. Please try again."
                    continue

                # With successful choice, get user to choose starting coordinate
                while not current_ship.placed:
                    self.clear_screen()
                    self.player_grid.draw_grid()
                    self.show_message()
                    ship_start = input(f"Choose starting coordinate to place {current_ship.name}: ")
                    if not self.player_grid.validate_coordinates(ship_start):
                        self.message = Fore.RED + "Invalid choice. Try again."
                        continue
                    ship_start = self.player_grid.format_input(ship_start)

                    # Check a ship is not already at the chosen coordinate
                    start_exists = False
                    for prev_ship in player.ships:
                        if prev_ship.coords.count(ship_start) > 0:
                            start_exists = True
                    if start_exists:
                        self.message = Fore.RED + "A ship already exists at these coordinates. Please try again."
                        continue

                    # With valid starting coordinate, redraw grid with reference shown
                    starting_cell = self.player_grid.search_grid(ship_start)
                    starting_cell.change_char(" 0 ")
                    starting_cell.color_cell(Fore.RED)

                    self.clear_screen()
                    self.player_grid.draw_grid()

                    directions = {}
                    start_x = ship_start[0].upper()
                    start_y = ship_start[1]

                    # Check the length of the labels lists to see if the ship will go beyond
                    # the grid boundaries. If not, create a list with the coordinates

                    # Right / East
                    if not self.player_grid.x_labels.index(start_x) + current_ship.size > len(self.player_grid.x_labels):
                        right_coords = [ship_start]
                        for i in range(1, current_ship.size):
                            next_x = self.player_grid.x_labels.index(start_x) + i
                            right_coords.append(self.player_grid.x_labels[next_x].lower() + start_y)
                        directions["right"] = right_coords

                    # Left / West
                    if not self.player_grid.x_labels.index(start_x) - current_ship.size < 0:
                        left_coords = [ship_start]
                        for i in range(1, current_ship.size):
                            next_x = self.player_grid.x_labels.index(start_x) - i
                            left_coords.append(self.player_grid.x_labels[next_x].lower() + start_y)
                        directions["left"] = left_coords

                    # Down / South
                    if not self.player_grid.y_labels.index(start_y) + current_ship.size > len(self.player_grid.y_labels):
                        down_coords = [ship_start]
                        for i in range(1, current_ship.size):
                            next_y = self.player_grid.y_labels.index(start_y) + i
                            down_coords.append(start_x + self.player_grid.y_labels[next_y])
                        directions["down"] = down_coords

                    # Up / North
                    if not self.player_grid.y_labels.index(start_y) - current_ship.size < 0:
                        up_coords = [ship_start]
                        for i in range(1, current_ship.size):
                            next_y = self.player_grid.y_labels.index(start_y) - i
                            up_coords.append(start_x + self.player_grid.y_labels[next_y])
                        directions["up"] = up_coords

                    dir_to_remove = []
                    for coord_list in directions:
                        for coord in directions[coord_list]:
                            for ships in player.ships:
                                for prev_coord in ships.coords:
                                    if coord.lower() == prev_coord.lower():
                                        dir_to_remove.append(coord_list)

                    for direction in dir_to_remove:
                        if direction in directions:
                            directions.pop(direction)

                    if not directions:
                        starting_cell.change_char(" . ")
                        self.message = Fore.RED + "No valid placement available. Please try again"
                        continue

                    while not current_ship.coords:
                        self.clear_screen()
                        self.player_grid.draw_grid()
                        # User then chooses direction from remaining options (if any)
                        print("Available directions:")
                        for key in directions.keys():
                            print(" - " + key.capitalize())
                        self.show_message()
                        chosen_direction = input("\nChoose a direction for the ship: ")

                        if chosen_direction.lower() == "r" or chosen_direction.lower() == "right":
                            if "right" in directions:
                                current_ship.coords = directions["right"]
                                current_ship.facing = "right"
                            else:
                                self.message = Fore.RED + "Direction unavailable. Please try again."
                                continue

                        elif chosen_direction.lower() == "l" or chosen_direction.lower() == "left":
                            if "left" in directions:
                                current_ship.coords = directions["left"]
                                current_ship.facing = "left"
                            else:
                                self.message = Fore.RED + "Direction unavailable. Please try again."
                                continue

                        elif chosen_direction.lower() == "u" or chosen_direction.lower() == "up":
                            if "up" in directions:
                                current_ship.coords = directions["up"]
                                current_ship.facing = "up"
                            else:
                                self.message = Fore.RED + "Direction unavailable. Please try again."
                                continue

                        elif chosen_direction.lower() == "d" or chosen_direction.lower() == "down":
                            if "down" in directions:
                                current_ship.coords = directions["down"]
                                current_ship.facing = "down"
                            else:
                                self.message = Fore.RED + "Direction unavailable. Please try again."
                                continue

                        else:
                            self.message = Fore.RED + "Not a valid choice. Please try again."
                            continue

                        # Show the ship placement and confirm with the user
                        for coord in current_ship.coords:
                            cur_cell = self.player_grid.search_grid(coord)
                            cur_cell.has_ship = True
                            if current_ship.facing == "right" or current_ship.facing == "left":
                                if current_ship.coords.index(coord) == 0:
                                    if current_ship.facing == "right":
                                        cur_cell.change_char(" <=")
                                    else:
                                        cur_cell.change_char("=> ")
                                elif current_ship.coords.index(coord) == len(current_ship.coords) - 1:
                                    if current_ship.facing == "right":
                                        cur_cell.change_char("=> ")
                                    else:
                                        cur_cell.change_char(" <=")
                                else:
                                    cur_cell.change_char("===")
                            elif current_ship.facing == "up" or current_ship.facing == "down":
                                if current_ship.coords.index(coord) == 0:
                                    if current_ship.facing == "down":
                                        cur_cell.change_char(" A ")
                                    else:
                                        cur_cell.change_char(" V ")
                                elif current_ship.coords.index(coord) == len(current_ship.coords) - 1:
                                    if current_ship.facing == "down":
                                        cur_cell.change_char(" V ")
                                    else:
                                        cur_cell.change_char(" A ")
                                else:
                                    cur_cell.change_char(" H ")
                            cur_cell.color_cell(Fore.RED)

                        self.clear_screen()
                        self.player_grid.draw_grid()

                        user_confirm = input("Are you sure about this placement? (Y/n): ")

                        # If cancelling, remove styling from grid cells and empty the chosen coords
                        if user_confirm.lower() == "n" or user_confirm.lower() == "no":
                            for coord in current_ship.coords:
                                cur_cell = self.player_grid.search_grid(coord)
                                cur_cell.has_ship = False
                                cur_cell.change_char(" . ")
                                cur_cell.color_cell(Style.RESET_ALL)
                            current_ship.coords = []
                            break       # Drop back to choosing starting coordinate

                    # If coordinates have been chosen successfully then update, otherwise keep looping
                    if current_ship.coords:
                        player.ships.append(current_ship)
                        current_ship.placed = True

            for ship in player.ships:
                print(ship.name + " - " + str(ship.size) + " - ", end="")
                print(ship.coords)
