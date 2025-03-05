"""You are going to write a program that automatically prints the solution to the  % 15 game."""

for number in range(0, 101):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 5 % 15 == 0:
        print("FizzBuzz")
    else:
        print(number)
