# Tutorial by @kylieying
# https://www.youtube.com/watch?v=8ext9G7xspg&list=PLZJq_8DKT2L5lzSdUstt1_tUTPhdFD1gH
# Tweaks by me

import random


def play():
    user = input("'r' for Rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return "You won!"

    return "You lost!"


def is_win(player, opponent):
    # return true if the player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


print(play())
