import random
import string

WORDLIST_FILENAME = "palavras.txt"

def load_words():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = in_file.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter in letters_guessed:
            pass
        else:
            return False

    return True

def get_guessed_word():
     guessed = ''

     return guessed

def available_letters():
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase

    return available

def print_welcome():
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secret_word), ' letters long.'
    print '-------------'

def print_available_letter(letters_guessed):
    available = available_letters()
    empty = ''
    letter = ''

    for letter in available:
        if letter in letters_guessed:
            available = available.replace(letter, empty)

    print 'Available letters', available
    letter = raw_input('Please guess a letter: ')

    return letter

def letter_was_guessed(letters_guessed, secret_word):
    guessed = get_guessed_word()
    for letter in secret_word:
        if letter in letters_guessed:
            guessed += letter
        else:
            guessed += '_ '
    print 'Oops! You have already guessed that letter: ', guessed

def letter_is_valid(letter, letters_guessed, secret_word):
    letters_guessed.append(letter)
    guessed = get_guessed_word()

    for letter in secret_word:
        if letter in letters_guessed:
            guessed += letter
        else:
            guessed += '_ '

    print 'Good Guess: ', guessed

def letter_is_invalid(letter, secret_word, letters_guessed):
    letters_guessed.append(letter)

    guessed = get_guessed_word()
    for letter in secret_word:
        if letter in letters_guessed:
            guessed += letter
        else:
            guessed += '_ '

    print 'Oops! That letter is not in my word: ',  guessed

def word_guessed(secret_word, letters_guessed):
    if is_word_guessed(secret_word, letters_guessed):
        print 'Congratulations, you won!'
    else:
        print 'Sorry, you ran out of guesses. The word was ', secret_word, '.'

def not_end_game(secret_word, letters_guessed, guesses):
    no_guesses = 0

    return not is_word_guessed(secret_word, letters_guessed) and guesses > no_guesses

def hangman(secret_word):
    guesses = 8
    empty = ''
    letters_guessed = []

    while not_end_game(secret_word, letters_guessed, guesses):
        print 'You have ', guesses, 'guesses left.'

        letter = print_available_letter(letters_guessed)

        if letter in letters_guessed:
            letter_was_guessed(letters_guessed, secret_word)
        elif letter in secret_word:
            letter_is_valid(letter, letters_guessed, secret_word)
        else:
            guesses -= 1
            letter_is_invalid(letter, secret_word, letters_guessed)

        print '------------'

    else:
        word_guessed(secret_word, letters_guessed)

secret_word = load_words().lower()
hangman(secret_word)
