# Original tutorial by @kylieying
# https://youtu.be/8ext9G7xspg?t=1465
# Clarifications, tweaks and explanatory comments by me
# Challenge: Convert this to a Python Turtle game
# -----------------------------------------------------

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
        # While the word does have a dash or space in it we choose again as it's not valid for play
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

    # This is the main game loop within the hangman() method

    # While the length of word_letters set() is greater than 0 (because later we remove the letters the player guesses)
    # and while guesses remaining is greater than 0 we loop over each of the commands below
    while len(word_letters) > 0 and guesses > 0:
        # If guesses are exactly 8 then we've just started the game (or we guessed a letter right on first guess ;)
        if guesses == 8:
            print(f"You have {guesses} guesses - good luck!")
        # Else guesses don't equal 8 so we must have guessed wrong at least once already
        else:
            print(f"You have {guesses} guesses left and you have used these letters: ", " ".join(used_letters))

        # Above here we declared a set() assigned to used_letters to store letters the player has guessed
        # Here we show the letters from used_letters, i.e. the letters that have been guessed correctly so far
        # else we show a dash in place of a letter in the word_to_guess, as it hasn't been guessed yet
        # (e.g. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word_to_guess]
        # Then we print out word_list (with guessed letters and substitute dashes for the player to see)
        # by joining each letter with a space. Remember, as word_list is an array so the letters are in order
        print("Current word: ", ' '.join(word_list)) 

        # Here we get the player to input a letter and assign it to user_letter, converting it to upper case
        # This is to ensure it matches the alphabet set() we created above using set(string.ascii_uppercase)
        user_letter = input("Guess a letter: ").upper()
        # If the user_letter is in the alphabet list, excluding the list of already guessed letters in used_letters
        if user_letter in alphabet - used_letters:
            # then add the new user_letter to the used_letters set()
            used_letters.add(user_letter)
            # However, if the above isn't true, we haven't guessed it yet
            # So then we check if the new user_letter is in the word_to_guess set(), stored in word_letters
            if user_letter in word_letters:
                # If true, we remove the user_letter from word_letters so it won't be guessed again
                word_letters.remove(user_letter)
                # This give a blank line between repeated game text
                print("")

            # Else must mean the letter was already in used_letters or it was in the word
            # If not we a) haven't already guessed it or b) have guessed a letter incorrectly
            else:
                # So our guesses go down one for the incorrect guess
                guesses -= 1
                print('\nYour letter,', user_letter, 'is not in the word.')

        # If the guessed letter was already in used_letters we tell the player and don't deduct a guess
        elif user_letter in used_letters:
            print("You already used this letter, please try again.")

        # Else if the guessed letter is a) not in the alphabet, b) not in used_letters and c) not in the word
        # Then it can't be a letter and we let the player know (and add a new line)
        else:
            print("Invalid letter, please try again.\n")

    # If guesses is now 0, then we come out of the while loop and we must be out of guesses
    if guesses == 0:
        print('You died, sorry. The word was', word_to_guess)
    # Else if guesses is greater than 0, but word_letters length is 0, then we must have guessed them all
    else:
        print('You guessed the word:', word_to_guess, '!!')


# Call hangman() and run the game
hangman()
