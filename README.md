# battleship-bros
This is a Battleship style game written in Python 3.
This is the REPOSITORY where Battleships will be collaborated on!

We will write Battleships using Python 3, some bitchin' ASCII graphics, maybe some military sounding MIDI music and a shit ton of time...

Add to this these notes anything that is relevant to the game but not part of the code. e.g. links to resources, images, ideas, sketching code, ramblings, etc...

## GAME PLAN:
There is tons of info here: https://en.wikipedia.org/wiki/Battleship_(game)

- Title needed, with an option for the player to look at the rules or start a game

- Rules needed. Must be clear and concise. Must be able to start a game after reading rules. Maybe player can access rules any time during play if its set to a string "help" or "rules" for example?

- Grid must be drawn when game starts. Grid from original board game is 10x10 squares, A-J by 1-10.

- Player chooses where their ships are drawn before play. Not sure the easiest way for player to communicate this. Maybe the ships are listed with their lengths and the player chooses a coordinate and then is asked for vertical or horizontal orientation. e.g:
                  SHIP:         SIZE:
                  Carrier       5
                  Battleship    4
                  Cruiser       3
ship_choice = input("Choose vessel to place: ")   "Carrier"
ship_coordinate = input("Choose a coordinate to place the ", ship_choice, ": ")    "B7"
ship_orientation = input("Place vertical or horizontal?(v/h): ")    "h"
player_carrier = [B7, C7, D7, E7, F7]

