import random
import os


def random_number():
    return random.randint(1, 100)


def guess_number(guessed_number: int, number: int):
    print(f'''{number=}''')
    print(f'''{guessed_number=}''')

    if guessed_number == number:
        return True

    if guessed_number < number:
        print("Too low.")
    else:
        print("Too high.")


def game_attempts(attempts: int):
    attempt_count = 0
    number = random_number()
    win = False
    while attempt_count < attempts:

        try:
            print(
                f"You have {attempts - attempt_count} attempts remaining to guess the number.")
            guessed_number = int(input("Make a guess: "))
            win = guess_number(guessed_number, number)

            if win:
                print("You Win😁")
                break
        except ValueError:
            print("Please enter a valid number! ❌")
            continue
        attempt_count += 1

    if not win:
        print(f"You lose! 😭 The number was {number}.")


def run_game():
    os.system("clear" if os.name == "posix" else "cls")
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    choose_difficulty = input(
        "Choose a difficulty. Type 'easy' or 'hard' ").strip().lower()

    attempts = 5 if choose_difficulty == "hard" else 10
    game_attempts(attempts)


run_game()
