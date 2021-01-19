# Original tutorial by @kylieying
# https://youtu.be/8ext9G7xspg?t=1465
# Clarifications, tweaks and explanatory comments by me

# Further reading:
# https://realpython.com/python-sets/
# --------------------------------------------------------------

# Import the standard Python modules
import random
import string
# Import the list of words from the words_file.py file
from words_file import list_of_words

# Define a function that takes a word to guess for the user, from the list of words we imported
def get_valid_word(list_of_words):
    # we make a random choice from the list of words and assign it to the variable a_valid_word
    a_valid_word = random.choice(list_of_words)
    # we check the word to see if it contains a dash (-) or space ( )
    while '-' in a_valid_word or ' ' in a_valid_word:
        # While the word has a dash or space in it we choose again as it's not valid for play
        # (we do this so the player is only choosing letters, not weird characters)
        a_valid_word = random.choice(list_of_words)

    # Once we have a word to guess that is valid, we return it for use in the the hangman() function as word_to_guess
    return a_valid_word.upper()


def hangman():
    # We call the get_valid_word method above, passing it the valid word we found, assigning it to the variable word_to_guess
    word_to_guess = get_valid_word(list_of_words)
    # We pass the built in set() method the word_to_guess, assigning it to the word_letters variable
    # A set() generates a list of characters for us to match our guesses against
    word_letters = set(word_to_guess)
    # Next we create another set() with the alphabet as a list
    alphabet = set(string.ascii_uppercase)
    # Finally we create a set() from all the letters the player has guessed
    used_letters = set()

    # Here we allow the player a certain number of tries at guessing the correct letters
    # Typically we'd draw: post, head, body, left arm , right arm, left leg, right leg, noose
    guesses = 8

    while len(word_letters) > 0 and guesses > 0:
        print('You have', guesses, 'guesses left and you have used these letters: ', ' '.join(used_letters))

        # What the current words is (i.e. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word_to_guess]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")

            else:
                guesses = guesses - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print("You already used this letter, please try again.")

        else:
            print("Invalid letter, please try again.")

    # gets here when len(word_letters) == 0 OR when lives == 0
    if guesses == 0:
        print('You died, sorry. The word was', word_to_guess)
    else:
        print('YAY! You guessed the word:', word_to_guess, '!!')


if __name__ == '__main__':
    hangman()
