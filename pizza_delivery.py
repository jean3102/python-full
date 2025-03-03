# Write a Pizza Delivery Program Congratulations,
# you've got a job at Python Pizza Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

size_choice = input("what size pizza do you want? S, M, L: ").lower()
peperoni = input("Do you want peperoni on your pizza? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()
TOTAL_PRICE = 0
SMALL_PIZZA_PRICE = 15
MEDIUM_PIZZA_PRICE = 20
LARGE_PIZZA_PRICE = 25

# * work out how much they need to pay based on their size choice.
if size_choice == "s":
    TOTAL_PRICE = SMALL_PIZZA_PRICE
    if peperoni == "y":
        TOTAL_PRICE += 2

if size_choice == "m":
    TOTAL_PRICE = MEDIUM_PIZZA_PRICE

if size_choice == "l":
    TOTAL_PRICE = LARGE_PIZZA_PRICE

if extra_cheese == "y":
    TOTAL_PRICE += 1

if peperoni == "y":
    TOTAL_PRICE += 3

if peperoni == "y" and size_choice != "s":
    TOTAL_PRICE += 1

print(f"Your final bill is: {TOTAL_PRICE}")
