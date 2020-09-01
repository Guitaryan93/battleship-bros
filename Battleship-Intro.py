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

skip_intro = 1
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
    p1_fleet, p1_attack_grid, p2_fleet, p2_attack_grid = initiate_battlespace()
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

def initiate_battlespace():
    p1_fleet = [["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"]]

    p1_attack_grid = [["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"]]

    p2_fleet = [["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                        ["Empty"], ["Empty"]]

    p2_attack_grid = [["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"], ["Empty"],
                          ["Empty"], ["Empty"]]
    return p1_fleet, p1_attack_grid, p2_fleet, p2_attack_grid


def start_game(game_rules, p1_fleet, p1_attack_grid, p2_fleet, p2_attack_grid):
    # ....AND THE REST. LOL




# These are taken straight from chess program but will function the same
# They change player strings into list indices and back ("a1" -> [0][0] and ([0][0] -> "a1")
# CHANGES COORDINATES FROM LETTER NUMBER TO LIST INDICES (ADDRESSES OF THE SQUARES)
def encode_coordinates(player_selection):
    letter_number_coord = [int(player_selection[1]) - 1, ord(player_selection[0].lower()) - 97]
    return letter_number_coord

# CHANGES LIST INDICES BACK TO LETTER NUMBER COORDINATES
def decode_coordinates(number_letter_coord):
    non_list_coords = str(chr(number_letter_coord[1] + 97)) + str(number_letter_coord[0] + 1)
    return non_list_coords



main() # <-- This is the game running