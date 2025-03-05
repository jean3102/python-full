"""You are going to write a program that automatically prints the solution to the  % 15fizz_buzz_game game."""

for number in range(1, 17):

    if number % 5 == 0 and number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
