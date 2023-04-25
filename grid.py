''' Classes for the Grid and Grid Cells. Should allow us to draw and manage the grid using cell objects. '''

import re
from colorama import *


def validate_coordinates(coords):
    valid_coords = False
    if re.fullmatch("[a-j][0-9]", coords) or re.fullmatch("[0-9][a-j]", coords):
        valid_coords = True

    return valid_coords


def format_input(player_input):
    ''' Change the player input to match the gridcells - Letter,Number - F5'''
    formatted_input = ""
    if re.fullmatch("[0-9][a-j]", player_input):
        for char in player_input:
            formatted_input = char + formatted_input
    else:
        formatted_input = player_input

    return formatted_input


class Grid:
    def __init__(self, player):
        self.player = player
        self.x_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.y_labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.width = 11
        self.height = 11
        self.cells = []
        self._build_grid()

    def _build_grid(self):
        for y in range(len(self.y_labels)):
            for x in range(len(self.x_labels)):
                cell = Gridcell(self, self.x_labels[x], self.y_labels[y])
                self.cells.append(cell)

    def draw_grid(self):
        # Top line of alpha coordinates
        print("   ", end="")
        for label in self.x_labels:
            print(" " + label + " ", end="")
        print()     # Add a newline

        # Grid lines beginning with numeric coordinates
        start_idx = 0
        end_idx = 10
        for label in self.y_labels:
            print(" " + label + " ", end="")
            for cell in range(start_idx, end_idx):
                print(self.cells[cell].char, end="")
                # print(" " + self.cells[cell].char + " ", end="")
                # print(" " + self.cells[cell].coords_string, end="")
            start_idx += 10
            end_idx += 10
            print()     # Add a newline

        print()     # End with a newline for easier reading on-screen

    def search_grid(self, coords):
        ''' Search through the grid cells to find and return one matching the player input. '''
        for cell in self.cells:
            if cell.coords_string.lower() == coords.lower():
                return cell

        return None


class Gridcell:
    def __init__(self, grid, x, y):
        self.grid = grid
        self.coords = [x, y]
        self.coords_string = f"{self.coords[0].lower()}{self.coords[1]}"
        self.prev_selected = False
        self.has_ship = False
        self.char = " . "
        self.color_cell(Fore.CYAN)

    def cell_feedback(self):
        ''' Check and update the cell depending on whether it has been selected before,
            it contains a ship, or if it is a missed shot '''
        if self.prev_selected:
            if self.grid.player.is_human:
                msg = "This coordinate has been previously selected, please try again or type \"help\"."
            else:
                msg = ""
            status = "error"
        elif self.has_ship:
            self.prev_selected = True
            msg = "HIT!"
            status = "hit"
        else:
            self.prev_selected = True
            msg = "Missed..."
            status = "miss"

        return msg, status

    def change_char(self, new_char):
        self.char = new_char

    def color_cell(self, color):
        self.char = color + self.char + Style.RESET_ALL
