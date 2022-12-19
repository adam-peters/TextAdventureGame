import os
import time
import game

SCREEN_SIZE = os.get_terminal_size()

# clear game screen to start game
os.system('cls')

# create cool title screen
# --------------------------------
print("\n")
print("\n")
print("Cool Title Screen Here \n".center(SCREEN_SIZE.columns))
print("\n")
print("\n")
# --------------------------------

current_game = game.Game()
while input("Would you like to play The Magical Game? (yes or no) \n".center(SCREEN_SIZE.columns)).lower() != "no":
    current_game.play_game()


if current_game.game_counter == 0:
    print("you couldn't even play my game once...".center(SCREEN_SIZE.columns))
    time.sleep(2)
elif current_game.game_counter == 1:
    end_message_1 = "thank you for playing the game " + str(current_game.game_counter) + " time you cheap bastard!"
    print(end_message_1.center(SCREEN_SIZE.columns))
    time.sleep(2)
else:
    end_message_2 = "thank you for playing the game " + str(current_game.game_counter) + " times!"
    print(end_message_2.center(SCREEN_SIZE.columns))
    print("\n")
    time.sleep(2)

