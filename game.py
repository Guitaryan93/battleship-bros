''' Class for the overall Game. Takes care of building the game, checking
    game conditions and screen controls, etc... '''

from grid import *
from player import Player, Battleship
import os
from time import sleep
from colorama import *
from random import randint


class Game:
    def __init__(self):
        self.ship_count = 5
        self.player_1 = Player(True, "Human Player")        # Human player
        self.player_2 = Player(False, "Computer Player")       # Computer player
        self.players = [self.player_1, self.player_2]
        self.message = ""
        self.game_over = False
        self.winning_player = None

        # Game Loop
        self.clear_screen()
        self.setup_ships()
        self.choose_starting_player()
        while not self.game_over:
            player, opponent = self.player_turn()
            self.check_win_conditions(player, opponent)
        self.display_winner()

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

        # Add debug code below this line for testing purposes
        # print(debug_code_example)

    def choose_starting_player(self):
        ''' Randomly decide which player gets the first turn '''
        starting_player = self.players[randint(0, 1)]
        starting_player.turn = True

    def player_turn(self):
        # Find out whose turn it is
        for p in self.players:
            if p.turn:
                player = p
            elif not p.turn:
                opponent = p

        # Check for computer / human player
        while player.turn:
            # Draw screen
            self.clear_screen()
            player.attack_grid.draw_grid()
            player.ship_grid.draw_grid()
            self.show_message()

            if player.is_human:
                player_input = input("Choose coordinates: ").lower()
                # Put any keywords first or else they will be skipped
                if player_input == "help" or player_input == "h":
                    self.show_help()
                elif player_input == "quit" or player_input == "q":
                    # Build me into a function/method!!!
                    print("Goodbye!")
                    sleep(2)
                    quit()
                # Check that the coordinate is a valid format
                elif validate_coordinates(player_input):
                    player_input = format_input(player_input)
                    self.perform_attack(player, opponent, player_input)

                else:
                    self.message = Fore.RED + "Incorrect co-ordinates. Please try again or type \"help\"."

            # Computer Player logic
            else:
                if player.hit_count > 0:
                    player.check_remaining_ships(opponent)

                if player.attack_list:
                    player_input = player.attack_list[randint(0, len(player.attack_list) - 1)]
                else:
                    player_input = player.get_random_coords()

                self.perform_attack(player, opponent, player_input)
                if player.attack_list and player.attack_list.count(player_input) > 0:
                    player.attack_list.remove(player_input)
                    if not player.attack_list:
                        player.current_hit_coords = ""
                        player.hit_count = 0

        return player, opponent

    def perform_attack(self, player, opponent, player_input):
        attack_grid_cell = player.attack_grid.search_grid(player_input)
        opponent_grid_cell = opponent.ship_grid.search_grid(player_input)
        grid_list = [attack_grid_cell, opponent_grid_cell]

        response, status = opponent_grid_cell.cell_feedback()

        if status == "hit":
            for g in grid_list:
                g.change_char(" X ")
                g.color_cell(Fore.RED)
            for ship in opponent.ships:
                if ship.coords.count(player_input.lower()) > 0:
                    ship.hp -= 1
            opponent.hp -= 1
            if not player.is_human:
                player.failsafe_count = 0       # On successful hit, reset the failsafe count for maximum power!
                if not player.attack_list:
                    # Build attack list for up, down, left and right directions
                    player.create_attack_list(player_input)
                    player.hit_count += 1
                elif player.attack_list and player.current_hit_coords != "":
                    # If a second hit is found, update the attack list to search on the same axis
                    player.update_attack_list(player_input)
                    player.hit_count += 1
        elif status == "miss":
            for g in grid_list:
                g.change_char(" o ")
                g.color_cell(Style.BRIGHT)
        else:
            if player.is_human:
                self.message = response
            # If the computer player gets stuck in a loop looking for attacks, break out after "n" failed attempts
            elif player.failsafe_count > 10:
                player.attack_list = []
                player.failsafe_count = 0
            # If computer player has already chosen this cell, and it was a hit previously, extend the attack search
            elif player.attack_list and opponent_grid_cell.has_ship:
                player.failsafe_count += 1
                player.update_attack_list(opponent_grid_cell.coords_string)

            return

        self.message = f"{player.name} {response}"
        player.turn = False
        opponent.turn = True

    def setup_ships(self):
        # Loop through each player and setup their ships to start the game
        for player in self.players:
            ship_list = [Battleship(1, "Carrier", 5),
                         Battleship(2, "Battleship", 4),
                         Battleship(3, "Cruiser", 3),
                         Battleship(4, "Submarine", 3),
                         Battleship(5, "Destroyer", 2)]

            while len(player.ships) < self.ship_count:
                if player.is_human:
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

                else:
                    # Setup current ship for computer player
                    current_ship = ship_list[len(player.ships)]

                # With successful choice, get user to choose starting coordinate
                while not current_ship.placed:
                    if player.is_human:
                        self.clear_screen()
                        player.ship_grid.draw_grid()
                        self.show_message()
                        ship_start = input(f"Choose starting coordinate to place {current_ship.name}: ")
                        if not validate_coordinates(ship_start):
                            self.message = Fore.RED + "Invalid choice. Try again."
                            continue
                        ship_start = format_input(ship_start)
                    else:
                        # Build random start coords for computer player
                        rand_x = player.ship_grid.x_labels[randint(0, len(player.ship_grid.x_labels) - 1)]
                        rand_y = player.ship_grid.y_labels[randint(0, len(player.ship_grid.y_labels) - 1)]
                        ship_start = rand_x.lower() + rand_y

                    # Check a ship is not already at the chosen coordinate
                    start_exists = False
                    for prev_ship in player.ships:
                        if prev_ship.coords.count(ship_start) > 0:
                            start_exists = True
                    if start_exists:
                        if player.is_human:
                            self.message = Fore.RED + "A ship already exists at these coordinates. Please try again."
                        continue

                    # With valid starting coordinate, redraw grid with reference shown
                    if player.is_human:
                        starting_cell = player.ship_grid.search_grid(ship_start)
                    else:
                        starting_cell = player.ship_grid.search_grid(ship_start)
                    if player.is_human:
                        starting_cell.change_char(" 0 ")
                        starting_cell.color_cell(Fore.GREEN)

                        self.clear_screen()
                        player.ship_grid.draw_grid()

                    directions = {}
                    start_x = ship_start[0].upper()
                    start_y = ship_start[1]

                    # Check the length of the labels lists to see if the ship will go beyond
                    # the grid boundaries. If not, create a list with the coordinates

                    # Right / East
                    if not player.ship_grid.x_labels.index(start_x) + current_ship.size > len(player.ship_grid.x_labels):
                        right_coords = [ship_start]
                        for i in range(1, current_ship.size):
                            next_x = player.ship_grid.x_labels.index(start_x) + i
                            right_coords.append(player.ship_grid.x_labels[next_x].lower() + start_y)
                        directions["right"] = right_coords

                    # Left / West
                    if not player.ship_grid.x_labels.index(start_x) - current_ship.size < 0:
                        left_coords = [ship_start]
                        for i in range(1, current_ship.size):
                            next_x = player.ship_grid.x_labels.index(start_x) - i
                            left_coords.append(player.ship_grid.x_labels[next_x].lower() + start_y)
                        directions["left"] = left_coords

                    # Down / South
                    if not player.ship_grid.y_labels.index(start_y) + current_ship.size > len(player.ship_grid.y_labels):
                        down_coords = [ship_start]
                        for i in range(1, current_ship.size):
                            next_y = player.ship_grid.y_labels.index(start_y) + i
                            down_coords.append(start_x.lower() + player.ship_grid.y_labels[next_y])
                        directions["down"] = down_coords

                    # Up / North
                    if not player.ship_grid.y_labels.index(start_y) - current_ship.size < 0:
                        up_coords = [ship_start]
                        for i in range(1, current_ship.size):
                            next_y = player.ship_grid.y_labels.index(start_y) - i
                            up_coords.append(start_x.lower() + player.ship_grid.y_labels[next_y])
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
                        if player.is_human:
                            starting_cell.change_char(" . ")
                            self.message = Fore.RED + "No valid placement available. Please try again"
                        continue

                    while not current_ship.coords:
                        if player.is_human:
                            self.clear_screen()
                            player.ship_grid.draw_grid()
                            # User then chooses direction from remaining options (if any)
                            print("Available directions:")
                            for key in directions.keys():
                                print(" - " + key.capitalize())
                            self.show_message()
                            chosen_direction = input("\nChoose a direction for the ship: ")
                        else:
                            # Computer player chooses a random available direction
                            possible_directions = []
                            for k in directions.keys():
                                possible_directions.append(k)
                            chosen_direction = possible_directions[randint(0, len(possible_directions) - 1)]

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
                            cur_cell = player.ship_grid.search_grid(coord)
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
                            cur_cell.color_cell(Fore.GREEN)

                        if player.is_human:
                            self.clear_screen()
                            player.ship_grid.draw_grid()

                            user_confirm = input("Are you sure about this placement? (Y/n): ")

                            # If cancelling, remove styling from grid cells and empty the chosen coords
                            if user_confirm.lower() == "n" or user_confirm.lower() == "no":
                                for coord in current_ship.coords:
                                    cur_cell = player.ship_grid.search_grid(coord)
                                    cur_cell.has_ship = False
                                    cur_cell.change_char(" . ")
                                    cur_cell.color_cell(Style.RESET_ALL)
                                current_ship.coords = []
                                break       # Drop back to choosing starting coordinate

                    # If coordinates have been chosen successfully then update, otherwise keep looping
                    if current_ship.coords:
                        player.ships.append(current_ship)
                        current_ship.placed = True

            # Total up the players hitpoints
            player.get_hitpoints()

    def check_win_conditions(self, player, opponent):
        if opponent.hp <= 0:
            self.winning_player = player
            self.game_over = True

    def display_winner(self):
        self.clear_screen()
        print(f"Congratulations, {self.winning_player.name}!\n\nYou are the winner!")
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again == "y" or play_again == "yes":
            self.__init__()
        else:
            print("Thanks for playing!")
            sleep(2)
            quit()
