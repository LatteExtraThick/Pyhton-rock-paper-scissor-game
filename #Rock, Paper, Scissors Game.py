 #Rock, Paper, Scissors Game

#How to Play:
#The player chooses Rock, Paper, or Scissors.
#The computer randomly picks Rock, Paper, or Scissors.

#Rules:
#Rock beats Scissors
#Scissors beats Paper
#Paper beats Rock
# The game declares the winner of each round.
# The game continues until the player chooses to exit.
# Keeps track of wins, losses, and ties.

import random

# Constants
CHOICES = ['rock', 'paper', 'scissors']

# Score tracking
player_score = 0
computer_score = 0
draws = 0

def display_menu():
    print("\n( ͡° ͜ʖ ͡°) Welcome to Rock, Paper, Scissors! ( ͡° ͜ʖ ͡°)")
    print("Choose an option:")
    print("1. Play a round")
    print("2. View score")
    print("3. Exit")

def get_player_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in CHOICES:
            return choice
        else:
            print("(╥_╥)Invalid input. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(CHOICES)

def determine_winner(player, computer):
    global player_score, computer_score, draws
    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a draw! ̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿ ")
        draws += 1
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        print("You win this round! ╰(◕ᗜ◕)╯ ")
        player_score += 1
    else:
        print("Computer wins this round! (▀̿Ĺ̯▀̿ ̿) ")
        computer_score += 1

def show_score():
    print("\n ( ͜。 ͡ʖ ͜。) Current Score:")
    print(f"You: {player_score}")
    print(f"Computer: {computer_score}")
    print(f"Draws: {draws}")

def play_game():
    while True:
        display_menu()
        choice = input("Enter your option (1/2/3): ").strip()

        if choice == '1':
            player = get_player_choice()
            computer = get_computer_choice()
            determine_winner(player, computer)
        elif choice == '2':
            show_score()
        elif choice == '3':
            print("\nThanks for playing! ─=≡Σᕕ( ͡° ͜ʖ ͡°)ᕗ ")
            show_score()
            break
        else:
            print(" o(╯□╰)o Invalid menu option. Please enter 1, 2, or 3.")

# Start the game
if __name__ == "__main__":
    play_game()

