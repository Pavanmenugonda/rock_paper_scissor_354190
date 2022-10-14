import random
import sys


class rocky(object):
    choices = {1: "ROCK", 2: "PAPER", 3: "SCISSOR"}  # Choose options 1,2,3 to play

    # function to check the valid choice
    def to_check_input_valid(self, player_choice):

        try:
            player_choice = int(player_choice)
        except ValueError:
            return False
        if player_choice in rocky.choices:
            return True
        return False

    # returning the player choice
    def player_choice(self, player_choice):

        if rocky.to_check_input_valid(rocky, player_choice):
            player_choice = int(player_choice)
            player_choosen = rocky.choices[player_choice]
            return player_choosen
        return False

    # returning computer choice
    def computer_choice(self):

        computer_number = random.randint(1, 3)
        computer_choice = rocky.choices[computer_number]
        return computer_choice

    # checking the winner
    def to_check_winner(self, player_choosen, computer_choosen):

        if player_choosen == computer_choosen:  # No winner, if it's a tie.
            return None
        if player_choosen == "ROCK" and computer_choosen == "SCISSOR":
            return "Player"
        if player_choosen == "PAPER" and computer_choosen == "ROCK":
            return "Player"
        if player_choosen == "SCISSOR" and computer_choosen == "PAPER":
            return "Player"
        return "Computer"

    # here the game starts
    def game_start(self):

        player_points = 0
        computer_points = 0
        round_number = 0

        while player_points < 5 and computer_points < 5:
            prompt = "Choose 1.ROCK\n       2)PAPER\n       3)SCISSOR\n       4)Quit\n "
            player_input = input(prompt)
            # To Quit the game
            if player_input == "4":
                print('''
                GAME ENDED!
                Play again''')
                sys.exit()

            # If wrong input, ask the player to choose again
            elif not rocky.to_check_input_valid(rocky, player_input):
                print("Please choose your optionagain.\n")

            elif rocky.to_check_input_valid(rocky, player_input):
                round_number += 1
                computer_action = rocky.computer_choice(rocky)
                player_action = rocky.player_choice(rocky, player_input)
                winner = rocky.to_check_winner(rocky, player_action, computer_action)

                # Give 1 point to winner in each round.
                if winner is None:  # If it's a tie, no one gets a point.
                    winner = "TIE"
                elif winner == "Player":
                    player_points += 1
                elif winner == "Computer":
                    computer_points += 1

                # printing the results of the game
                print(f"******** Game{round_number} ********")
                print(f"{winner} ")
                print(f"You played :{player_action}")
                print(f"Computer played :{computer_action}")
                print(f"Your points are :{player_points}.")
                print(f"Computer's points are {computer_points}.\n")

        # output
        game_winner = str()
        if player_points + computer_points == 5:
            print('''
                           GAME ENDED!
                           Play again''')
            print(f"The winner of the competition is: {game_winner}!")
            print(f"The total rounds are {round_number}.\n")
            sys.exit()

        if player_points > computer_points:
            game_winner = "You"
        else:
            game_winner = "Computer"
