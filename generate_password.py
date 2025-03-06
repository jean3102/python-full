import random

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
SYMBOLS = "!@#$%^&*()"
NUMBERS = "0123456789"

print("Welcome to the Password Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


def get_random_elements(count, elements):
    return random.choices(elements, k=count)


char_letters = get_random_elements(nr_letters, LETTERS)
char_symbols = get_random_elements(nr_symbols, SYMBOLS)
char_numbers = get_random_elements(nr_numbers, NUMBERS)

password_list = char_letters + char_symbols + char_numbers
random.shuffle(password_list)
PASSWORD = "".join(password_list)
print(f'''{PASSWORD=}''')
