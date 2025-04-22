import json
from os import system
system("clear")


def print_code(data, indent=4):
    print(json.dumps(data, indent=indent))


def sum_values(a, b):
    return a + b


def substract(a, b):
    return a - b


def division(a, b):
    return a / b


def multiplication(a, b):
    return a * b


def get_number(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter valid number.")
