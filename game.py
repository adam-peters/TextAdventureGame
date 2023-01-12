import os
import time


SCREEN_SIZE = os.get_terminal_size()


# animation that plays "You Win"
def play_win():
    speed = .5
    for i in range(4):
        os.system('cls')

        print(" /$$     /$$                        /$$      /$$ /$$          \n".center(SCREEN_SIZE.columns))
        print("|  $$   /$$/                       | $$  /$ | $$|__/          \n".center(SCREEN_SIZE.columns))
        print(" \  $$ /$$//$$$$$$  /$$   /$$      | $$ /$$$| $$ /$$ /$$$$$$$ \n".center(SCREEN_SIZE.columns))
        print("  \  $$$$//$$__  $$| $$  | $$      | $$/$$ $$ $$| $$| $$__  $$\n".center(SCREEN_SIZE.columns))
        print("   \  $$/| $$  \ $$| $$  | $$      | $$$$_  $$$$| $$| $$  \ $$\n".center(SCREEN_SIZE.columns))
        print("    | $$ | $$  | $$| $$  | $$      | $$$/ \  $$$| $$| $$  | $$\n".center(SCREEN_SIZE.columns))
        print("    | $$ |  $$$$$$/|  $$$$$$/      | $$/   \  $$| $$| $$  | $$\n".center(SCREEN_SIZE.columns))
        print("    |__/  \______/  \______/       |__/     \__/|__/|__/  |__/\n".center(SCREEN_SIZE.columns))

        time.sleep(speed)
        os.system('cls')

        print(" __      __                          __       __  __           \n".center(SCREEN_SIZE.columns))
        print("|  \    /  \                        |  \  _  |  \|  \          \n".center(SCREEN_SIZE.columns))
        print(" \$$\  /  $$______   __    __       | $$ / \ | $$ \$$ _______  \n".center(SCREEN_SIZE.columns))
        print("  \$$\/  $$/      \ |  \  |  \      | $$/  $\| $$|  \|       \ \n".center(SCREEN_SIZE.columns))
        print("   \$$  $$|  $$$$$$\| $$  | $$      | $$  $$$\ $$| $$| $$$$$$$\\n".center(SCREEN_SIZE.columns))
        print("    \$$$$ | $$  | $$| $$  | $$      | $$ $$\$$\$$| $$| $$  | $$\n".center(SCREEN_SIZE.columns))
        print("    | $$  | $$__/ $$| $$__/ $$      | $$$$  \$$$$| $$| $$  | $$\n".center(SCREEN_SIZE.columns))
        print("    | $$   \$$    $$ \$$    $$      | $$$    \$$$| $$| $$  | $$\n".center(SCREEN_SIZE.columns))
        print("     \$$    \$$$$$$   \$$$$$$        \$$      \$$ \$$ \$$   \$$\n".center(SCREEN_SIZE.columns))

        time.sleep(speed)
        os.system('cls')

        print(" __      __                         __       __  __           \n".center(SCREEN_SIZE.columns))
        print("/  \    /  |                       /  |  _  /  |/  |          \n".center(SCREEN_SIZE.columns))
        print("$$  \  /$$/______   __    __       $$ | / \ $$ |$$/  _______  \n".center(SCREEN_SIZE.columns))
        print(" $$  \/$$//      \ /  |  /  |      $$ |/$  \$$ |/  |/       \ \n".center(SCREEN_SIZE.columns))
        print("  $$  $$//$$$$$$  |$$ |  $$ |      $$ /$$$  $$ |$$ |$$$$$$$  |\n".center(SCREEN_SIZE.columns))
        print("   $$$$/ $$ |  $$ |$$ |  $$ |      $$ $$/$$ $$ |$$ |$$ |  $$ |\n".center(SCREEN_SIZE.columns))
        print("    $$ | $$ \__$$ |$$ \__$$ |      $$$$/  $$$$ |$$ |$$ |  $$ |\n".center(SCREEN_SIZE.columns))
        print("    $$ | $$    $$/ $$    $$/       $$$/    $$$ |$$ |$$ |  $$ |\n".center(SCREEN_SIZE.columns))
        print("    $$/   $$$$$$/   $$$$$$/        $$/      $$/ $$/ $$/   $$/ \n".center(SCREEN_SIZE.columns))

        time.sleep(speed)
        os.system('cls')

        print("$$\     $$\                         $$\      $$\ $$\           \n".center(SCREEN_SIZE.columns))
        print("\$$\   $$  |                        $$ | $\  $$ |\__|          \n".center(SCREEN_SIZE.columns))
        print(" \$$\ $$  /$$$$$$\  $$\   $$\       $$ |$$$\ $$ |$$\ $$$$$$$\  \n".center(SCREEN_SIZE.columns))
        print("  \$$$$  /$$  __$$\ $$ |  $$ |      $$ $$ $$\$$ |$$ |$$  __$$\ \n".center(SCREEN_SIZE.columns))
        print("   \$$  / $$ /  $$ |$$ |  $$ |      $$$$  _$$$$ |$$ |$$ |  $$ |\n".center(SCREEN_SIZE.columns))
        print("    $$ |  $$ |  $$ |$$ |  $$ |      $$$  / \$$$ |$$ |$$ |  $$ |\n".center(SCREEN_SIZE.columns))
        print("    $$ |  \$$$$$$  |\$$$$$$  |      $$  /   \$$ |$$ |$$ |  $$ |\n".center(SCREEN_SIZE.columns))
        print("    \__|   \______/  \______/       \__/     \__|\__|\__|  \__|\n".center(SCREEN_SIZE.columns))

        time.sleep(speed)
        os.system('cls')


class Game:
    game_counter = 0
    endgame = False
    win = False
    current_location = "starting"
    end_location = ""
    death = ""
    win_message = ""
    interfacing = True
    wrong_counter = 0
    commands = ["goto", "look", "die"]

    places = {
        "starting": "You are by a road, there is a forest in one direction and a lake in another",
        "forest": "You are in a forest",
        "lake": "You are by a lake",
    }

    def play_game(self):
        self.game_counter += 1

        while not self.endgame:
            os.system('cls')
            print(self.places.get(self.current_location).center(SCREEN_SIZE.columns).center(SCREEN_SIZE.columns))
            self.get_command()

            if self.current_location == "lake":
                self.endgame = True
                self.death = "You drowned"
            if self.current_location == end_location:
                self.endgame = True
                self.win = True
                self.win_message = "You made it to the magical forest \n"

        # Handle winning and losing
        if self.win:
            print(self.win_message.center(SCREEN_SIZE.columns))
            time.sleep(3)
            play_win()
        else:
            os.system('cls')
            print(self.death.center(SCREEN_SIZE.columns))
            time.sleep(3)

        self.reset_game()

    def reset_game(self):
        self.endgame = False
        self.win = False
        self.current_location = "starting"
        self.death = ""
        self.win_message = ""

    def get_command(self):

        # runs until a command is used to progress the game
        while self.interfacing:
            user_input = input("What would you like to do?, ls for list of commands \n".center(SCREEN_SIZE.columns))

            print()

            user_input = user_input.lower()
            user_input_list = user_input.split()
            command = user_input_list[0]

            # assigns a subject if there is more than two words typed
            subject = ""
            if len(user_input_list) == 2:
                subject = user_input_list[1]

            # command decision tree
            if command == "ls":
                self.print_commands()
            elif command == "look":
                print(self.current_location.center(SCREEN_SIZE.columns))
            elif command == "goto":
                if subject == "":
                    print("Where would you like to go (goto 'someplace')".center(SCREEN_SIZE.columns))
                elif subject == "someplace":
                    print("wise guy, huh...?".center(SCREEN_SIZE.columns))
                    time.sleep(1)
                    print("why don't you go sleep with the fish!".center(SCREEN_SIZE.columns))
                    time.sleep(1)
                    self.death = "cute fish swim around you as you lungs slowly fill with water..."
                    self.endgame = True
                    self.interfacing = False
                elif subject in self.places:
                    self.current_location = subject
                    self.interfacing = False
                else:
                    print("Location does not exits".center(SCREEN_SIZE.columns))
            elif command == "die":
                print("You are not getting off that easy...".center(SCREEN_SIZE.columns))
                print("\n")
            else:
                if self.wrong_counter == 0:
                    print("Huh?... I don't recognize that command".center(SCREEN_SIZE.columns))
                elif self.wrong_counter == 1:
                    print("You know you can type ls for commands".center(SCREEN_SIZE.columns))
                elif self.wrong_counter == 2:
                    print("Are you stupid?!?!".center(SCREEN_SIZE.columns))
                elif self.wrong_counter > 2:
                    self.death = "You were shot, your body never was found..."
                    self.interfacing = False
                    self.endgame = True
                self.wrong_counter += 1

        self.wrong_counter = 0

    # prints out the commands a user can use, called from get_command
    def print_commands(self):
        for c in self.commands:
            print(c.center(SCREEN_SIZE.columns))

        print("\n")

    # see if a bad input could be an attempted command
    # (ex. user typed "gofo", this will suggest "goto" command)
