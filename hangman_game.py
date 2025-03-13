import random

# 1- Randomly choose a word from word_list. Then print it.
WORD_LIST = ["apple", "banana", "cherry", "date"]
HANGMAN_STAGES = [
    '''
    -----
    |   |
        |
        |
        |
        |
    -----''',
    '''
    -----
    |   |
    O   |
        |
        |
        |
    -----''',
    '''
    -----
    |   |
    O   |
    |   |
        |
        |
    -----''',
    '''
    -----
    |   |
    O   |
   /|   |
        |
        |
    -----''',
    '''
    -----
    |   |
    O   |
   /|\\  |
        |
        |
    -----''',
    '''
    -----
    |   |
    O   |
   /|\\  |
   /    |
        |
    -----''',
    '''
    -----
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    -----'''
]

RANDOM_WORD = random.choice(WORD_LIST)
print(f"Random word: {RANDOM_WORD}")
PLACEHOLDER = ""
LIFE = 6
GAME_OVER = False
ARRAY_WORDS_FOUND = []

for underscore in RANDOM_WORD:
    PLACEHOLDER += "_"
    ARRAY_WORDS_FOUND.append("_")

# 2- Ask the user to guess a letter and assign their answer to a variable called guess.
while not GAME_OVER:
    if LIFE == 0:
        print("You Lose!")
        GAME_OVER = True
        break

    DISPLAY = "".join(ARRAY_WORDS_FOUND)
    print(f"Word Found: {DISPLAY}")
    print(f"{LIFE}/6 LIVES LEFT")
    print(f"STAGE: {HANGMAN_STAGES[6 - LIFE]}")

    GUESS = input("Guess a letter: ").lower()

    # 3- Check if the letter the user guessed (guess) is one of the letters in the chosen word.
    # Print "Right" if it's correct, "Wrong" if it's not.
    FIND = False

    for index, letter in enumerate(RANDOM_WORD):
        if letter == GUESS:
            FIND = True
            ARRAY_WORDS_FOUND[index] = letter

    if not FIND:
        LIFE -= 1
        print("That's not in the word. You lose a life.")

    # Check if the user has found all the letters
    if "".join(ARRAY_WORDS_FOUND) == RANDOM_WORD:
        print("You Win!")
        GAME_OVER = True
