import sys
from rps_main import rocky

while 1:  # To continue or restart ?
    print('''GAME BEGIN...\n''')
    rocky.game_start(rocky)  # Start the game
    restart = input("Restart the game? (y/n) ")
    if restart.lower() == "Yy":
        continue
    sys.exit()