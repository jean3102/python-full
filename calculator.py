import os
from utils import sum_values, substract, division, multiplication, get_number
OPERATIONS = {"+", "-", "*", "/"}


def calculator():
    os.system("clear")

    is_running = False
    result = 0
    while True:
        first_value = result
        if not is_running:
            first_value = get_number("What is your first value? ")

        for symbol in OPERATIONS:
            print(symbol)

        operation = input("Pick an operation: ").strip()

        if operation not in OPERATIONS:
            print(f"The operation {operation} is not recognized")
            continue
        second_value = get_number("What is your second value? ")

        if operation == "+":
            result = sum_values(first_value, second_value)
        if operation == "-":
            result = substract(first_value, second_value)
        if operation == "*":
            result = multiplication(first_value, second_value)
        if operation == "/":
            if second_value == 0:
                print("Error: cannot divide by zero")
                break
            result = division(first_value, second_value)

        continue_calculate = input(
            f"Type 'y' to continue with {result}, 'n' to start a new calculator or 'end' to end ").lower()

        if continue_calculate == "n":
            result = 0
            is_running = False
            continue

        if continue_calculate == "y":
            is_running = True

        if continue_calculate == "end":
            break

        print(f"{first_value} {operation} {second_value} = {result}")


calculator()
