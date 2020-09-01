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

# sets the seconds argument for the time.sleep function
HALF_SECOND = 0.5
QUICK_PAUSE = 0.02
QUARTER_SECOND = 0.3

def main():
    intro_animation()




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


main() # <-- This is the game running