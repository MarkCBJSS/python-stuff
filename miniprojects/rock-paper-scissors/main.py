# Tutorial by @kylieying
# https://www.youtube.com/watch?v=8ext9G7xspg&list=PLZJq_8DKT2L5lzSdUstt1_tUTPhdFD1gH
# Tweaks and explanatory comments by me

import random

# Define a function that gets a value for the Player and the Computer
# We ask the player for their choice, the Computer randomly makes its own choice
def play():
    user = input("'r' for Rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    print(f"The computer guessed {computer}")

    # Check if both choices were the same
    if user == computer:
        return "It's a tie"

    # Call the is_win function, passing user as the player value and computer as the opponent value
    # is_win returns True only if the player wins, so the if statement below would evaluate to True
    if is_win(user, computer):
        return "You won!"

    # If it's not a tie and the player didn't win, then they must have lost
    return "You lost!"

# Define a function to check the winning conditions. We only need to check if the player won, not the Computer too
def is_win(player, opponent):
    # Winning patterns are: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        # return True if the player wins
        return True
    # If the result is False for the above, then the player lost

# We call the play() function within the print() function to print out the return values
print(play())

