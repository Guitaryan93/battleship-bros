# This is the opening graphic for Battleship
# It would be sweet to add sounds eventually...

# TITLE GRAPHIC ORIGINAL:
# print("""
#     ____   ___   ______ ______ __     ______ _____  __  __ ____ ____
#    / __ ) /   | /_  __//_  __// /    / ____// ___/ / / / //  _// __ \\
#   / __  |/ /| |  / /    / /  / /    / __/   \__ \ / /_/ / / / / /_/ /
#  / /_/ // ___ | / /    / /  / /___ / /___  ___/ // __  /_/ / / ____/
# /_____//_/  |_|/_/    /_/  /_____//_____/ /____//_/ /_//___//_/
# """)

import time

skip_intro = 0
if skip_intro == 0:
    # sets the seconds argument for the time.sleep function
    HALF_SECOND = 0.5
    QUICK_PAUSE = 0.02
    QUARTER_SECOND = 0.3
elif skip_intro == 1:
    HALF_SECOND = 0
    QUICK_PAUSE = 0
    QUARTER_SECOND = 0


def main():
    intro_animation()
    game_rules = menu()
    # Empty grids are generated
    p1_fleet, p1_attack_grid, p2_fleet, p2_attack_grid = initiate_battle_space()
    start_game(game_rules, p1_fleet, p1_attack_grid, p2_fleet, p2_attack_grid)


def intro_animation():
    # simple animation using time.sleep for delaying printing strings
    print("\nRyStu Games Presents", end="")
    time.sleep(HALF_SECOND)
    print(".", end="")
    time.sleep(HALF_SECOND)
    print(".", end="")
    time.sleep(HALF_SECOND)
    print(".")
    time.sleep(HALF_SECOND)

    # prints a line of animated '*'
    for i in range(70):
        print("*", end="")
        time.sleep(QUICK_PAUSE)

    # print the game title graphic line by line like dial up internet
    print("\n    ____   ___   ______ ______ __     ______ _____  __  __ ____ ____ ")
    time.sleep(QUARTER_SECOND)
    print("   / __ ) /   | /_  __//_  __// /    / ____// ___/ / / / //  _// __ \\")
    time.sleep(QUARTER_SECOND)
    print("  / __  |/ /| |  / /    / /  / /    / __/   \__ \ / /_/ / / / / /_/ /")
    time.sleep(QUARTER_SECOND)
    print(" / /_/ // ___ | / /    / /  / /___ / /___  ___/ // __  /_/ / / ____/ ")
    time.sleep(QUARTER_SECOND)
    print("/_____//_/  |_|/_/    /_/  /_____//_____/ /____//_/ /_//___//_/ \n")

    for i in range(70):
        print("*", end="")
        time.sleep(QUICK_PAUSE)

    # print an epic 80's action movie tagline. One. Word. at. A. TIME.
    print("\nTime to ", end="")
    time.sleep(HALF_SECOND)
    print("SINK. ", end="")
    time.sleep(HALF_SECOND)
    print("OR. ", end="")
    time.sleep(HALF_SECOND)
    print("SWIM.")
    time.sleep(1)
    print()
    return


def menu():
    print(chr(8779))  # sea waves
    print(chr(127754))  # another wave
    print(chr(10060))  # good cross
    print(chr(9773))

    print("For the game rules type HELP.")
    print("To dive straight in hit ENTER.")
    menu_selection = str(input(">>> ")).upper()
    rules = "You've never played BATTLESHIP? Pffft."
    while menu_selection != "":
        if menu_selection == "HELP":
            print("\n", rules, "\n")
            print("For the game rules type HELP.")
            print("To dive straight in hit ENTER.")
            menu_selection = str(input(">>> ")).upper()
        else:
            print("Not a valid option.")
        print("For the game rules type HELP.")
        print("To dive straight in hit ENTER.")
        menu_selection = str(input(">>> ")).upper()
    game_type = 0
    while True:
        try:
            game_type = int(input("How many players? \n1 - 1 player \n2 - 2 Player \n >>> "))
            if game_type == 1 or 2:
                break
            else:
                print("Enter '1' or '2'")
        except ValueError:
            print("Enter '1' or '2'")
    # if game_type == 1:
    # difficulty = 0
    # while difficulty != 1 or 2 or 3:
    #     difficulty = int(input("Enter difficulty:"))
    return game_type


def initiate_battle_space():
    empty_ten_by_ten = [
        [["carrier_vertical", 1], ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0],  # Row 1
         ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0]],
        [["carrier_vertical", 2], ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0],  # Row 2
         ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0]],
        [["carrier_vertical", 3], ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0],  # Row 3
         ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0]],
        [["carrier_vertical", 4], ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0],  # Row 4
         ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0]],
        [["carrier_vertical", 5], ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0],  # Row 5
         ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0]],
        [["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0],  # Row 6
         ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0]],
        [["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0],  # Row 7
         ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0]],
        [["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0],  # Row 8
         ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0]],
        [["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0],  # Row 9
         ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0]],
        [["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0],  # Row 10
         ["Empty", 0], ["Empty", 0], ["Empty", 0], ["Empty", 0]]]

    return empty_ten_by_ten, empty_ten_by_ten, empty_ten_by_ten, empty_ten_by_ten


# Ships will be saved as separate horizontal and vertical versions. Each of these will contain a list of length
# equal to the length of the ship (eg carrier_list = 5 values), within each of these squares there is a dictionary
# which contains the 3 lines of each ship section.


def start_game(game_rules, p1_fleet, p1_attack_grid, p2_fleet, p2_attack_grid):
    print_board(p1_fleet, p2_attack_grid)
    # Players will place one end at a time. This will decide if horizontal/vertical
    # Player 1 place boats
    # Place Carrier (5 squares long)
    carrier_end_coord_one = input("Place first end of carrier: ")

    if game_rules == 2:
        # Player 2 places boats
        pass
    elif game_rules == 1:
        # AI player places boats
        pass


def print_board(p1_squares, p2_attack_grid):
    row = 0  # Starting row
    sps = 12  # sps = number of spaces (sps) in each column (not being used currently)
    # reversed_number_rows = p1_fleet
    # reversed_number_rows.reverse()

    # print the letters and top on grid
    ltrs = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    print(f"  {ltrs[0]:^12}{ltrs[1]:^12}{ltrs[2]:^12}{ltrs[3]:^12}{ltrs[4]:^12}{ltrs[5]:^12}{ltrs[6]:^12}{ltrs[7]:^12}"
          f"{ltrs[8]:^12}{ltrs[9]:^12}")
    print("_", "|_         _" * 10, "|_", sep="")

    current_grid = p1_squares

    for p1_square in p1_squares:
        # Print 3 lines that from each row (1-10). Lines are printed across letters (A-J)
        line_number = 1
        print_line(p1_square, p1_squares, row, line_number)
        line_number += 1
        print_line(p1_square, p1_squares, row, line_number)
        line_number += 1
        print_line(p1_square, p1_squares, row, line_number)
        row += 1


# PRINT LINE
def print_line(p1_square, p1_squares, row, line_number):
    if line_number == 1:
        empty_line = "|           "
    elif line_number == 2:
        empty_line = "            "
    elif line_number == 3:
        empty_line = "|_         _"
    full_line = []
    for column in range(0, 10):
        current_coordinate = [row, column]
        if p1_square[column][0] == "Empty":
            full_line.append(empty_line)
        else:
            full_line.append(ship_graphics_retriever(p1_squares, current_coordinate, line_number))
    if line_number == 1:
        print(" ", "".join(full_line), "|", sep="")
    elif line_number == 2:
        print(" ", "".join(full_line), sep="")
    elif line_number == 3:
        print("_", "".join(full_line), "|_", sep="")
    return


def ship_graphics_retriever(p1_squares, cc, line_number):
    # cc = current_coordinate

    # Ship graphics here. Number of rows in variable indicates length of sprite
    carrier_vertical = [{1: "|    /^\    ", 2: "    / w&\   ", 3: "|_ |     | _"},
                        {1: "|  | ||| |  ", 2: "   | (_) |  ", 3: "|_ |/===\| _"},
                        {1: "|  ||___Z|  ", 2: "   ||(*)||  ", 3: "|_ |[(_)|| _"},
                        {1: "|  | ||| |  ", 2: "   |8---8|  ", 3: "|_ |[(_)|| _"},
                        {1: "|  | ||| |  ", 2: "   | (H) |  ", 3: "|_ |_____| _"}]

    # Assigns the graphics based on what is present in the currently selected coordinate
    # Each ship will have a vertical and horizontal version
    # Checks if the vertical carrier sprite is present in the square being printed
    if "carrier_vertical" in p1_squares[cc[0]][cc[1]][0]:
        # Check the second value in the square to find what section of the carrier it is
        # (x coord, y coord, second value)
        if p1_squares[cc[0]][cc[1]][1] == 1:
            ship_sprite = carrier_vertical[0][line_number]
            return ship_sprite
        elif p1_squares[cc[0]][cc[1]][1] == 2:
            ship_sprite = carrier_vertical[1][line_number]
            return ship_sprite
        elif p1_squares[cc[0]][cc[1]][1] == 3:
            ship_sprite = carrier_vertical[2][line_number]
            return ship_sprite
        elif p1_squares[cc[0]][cc[1]][1] == 4:
            ship_sprite = carrier_vertical[3][line_number]
            return ship_sprite
        elif p1_squares[cc[0]][cc[1]][1] == 5:
            ship_sprite = carrier_vertical[4][line_number]
            return ship_sprite


def encode_coordinates(player_selection):
    # These are taken straight from chess program but will function the same
    # They change player strings into list indices and back ("a1" -> [0][0] and ([0][0] -> "a1")
    # CHANGES COORDINATES FROM LETTER NUMBER TO LIST INDICES (ADDRESSES OF THE SQUARES)
    letter_number_coord = [int(player_selection[1]) - 1, ord(player_selection[0].lower()) - 97]
    return letter_number_coord


# CHANGES LIST INDICES BACK TO LETTER NUMBER COORDINATES
def decode_coordinates(number_letter_coord):
    non_list_coords = str(chr(number_letter_coord[1] + 97)) + str(number_letter_coord[0] + 1)
    return non_list_coords


main()  # <-- This is the game running


# RYANS COMMENT TEST!!!!!!!!!
# STUART'S COMMENT TEST!!!!!!