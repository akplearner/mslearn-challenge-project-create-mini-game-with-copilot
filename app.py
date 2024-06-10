# Write 'hello world' to the console
print('Hello, World!')


# Create a rock paper scissors game, where the user plays against the computer. this are the rules: The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
# The computer's choice must be random.
# The player must be able to quit the game at any time.
# Path: app.py
import random

player_score = 0
computer_score = 0

while True:
    player_choice = input('Enter rock, paper, or scissors: ').lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    if player_choice not in ['rock', 'paper', 'scissors']:
        print('Invalid option. Try again.')
        continue

    print(f'Computer chose {computer_choice}.')

    if player_choice == computer_choice:
        print('It\'s a tie!')
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print('You win!')
        player_score += 1
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print('You win!')
        player_score += 1
    elif player_choice == 'paper' and computer_choice == 'rock':
        print('You win!')
        player_score += 1
    else:
        print('You lose!')
        computer_score += 1

    play_again = input('Do you want to play again? (yes/no): ').lower()
    if play_again != 'yes':
        break

print(f'Player score: {player_score}')
print(f'Computer score: {computer_score}')