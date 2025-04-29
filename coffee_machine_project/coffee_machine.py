from menu import MENU, TYPE_COINS
import os
os.system("clear")


class CoffeeMachine:
    def __init__(self) -> None:
        self.__is_on: bool = False
        self.__water: int = 1400
        self.__milk: int = 300
        self.__coffee: int = 100
        self.__money: float = 10.0

    def custom_order(self):
        if not self.__is_on:
            print("The Coffee Machine is off.")
            return

        while True:
            coffee_type = input(
                "\nWhat would you like? ('espresso', 'latte', 'cappuccino') or type 'off' to turn off: ").strip().lower()

            if coffee_type == "off":
                self.turn_off()
                print("Turning off the Coffee Machine. Goodbye!")
                break

            if coffee_type not in MENU:
                print(
                    "Invalid option. Please choose 'espresso', 'latte', or 'cappuccino'.")
                continue

            cost = MENU[coffee_type]["cost"]
            if not self.__has_sufficient_change(cost):
                print("Sorry, no change available.")
                continue

            if self.__has_sufficient_resources(coffee_type):
                self.__process_coins(coffee_type, cost)

            self.report()

    def __process_coins(self, coffee_type: str, cost: float):
        self.__print_coin_options()
        total_payment = 0.0

        while total_payment < cost:
            coin_type = input(
                "Insert coin type ('done' to cancel): ").strip().lower()
            if coin_type == "done":
                print("Transaction cancelled. Returning coins.")
                return

            if coin_type not in TYPE_COINS:
                print("Invalid coin type. Try again.")
                continue

            try:
                quantity = int(input(f"How many {coin_type}?: "))
                if quantity < 0:
                    print("Please insert a positive number.")
                    continue

                total_payment += quantity * TYPE_COINS[coin_type]
                print(f"Total inserted: ${total_payment:.2f} / ${cost:.2f}")

            except ValueError:
                print("Please enter a valid number.")

        change = total_payment - cost
        if change > self.__money:
            print("Machine doesn't have enough change.")
            print(f"${total_payment:.2f} returned.")
            return

        self.__process_purchase(coffee_type, cost)
        print(f"Here is ${change:.2f} in change.")
        print(f"Enjoy your {coffee_type}!")

    def __process_purchase(self, coffee_type: str, cost: float):
        ingredients = MENU[coffee_type]["ingredients"]

        self.__water -= ingredients.get("water", 0)
        self.__milk -= ingredients.get("milk", 0)
        self.__coffee -= ingredients.get("coffee", 0)
        self.__money -= cost

    def __has_sufficient_resources(self, coffee_type: str) -> bool:
        ingredients = MENU[coffee_type]["ingredients"]

        if self.__water < ingredients.get("water", 0):
            print("Sorry, not enough water.")
            return False
        if self.__milk < ingredients.get("milk", 0):
            print("Sorry, not enough milk.")
            return False
        if self.__coffee < ingredients.get("coffee", 0):
            print("Sorry, not enough coffee.")
            return False
        return True

    def __has_sufficient_change(self, cost: float) -> bool:
        return self.__money >= cost

    def __print_coin_options(self):
        print("Accepted coin types: 'quarters', 'dimes', 'pennies'")

    def refill(self, milk=None, water=None, coffee=None, money=None):
        if milk is not None:
            self.__milk = milk
        if water is not None:
            self.__water = water
        if coffee is not None:
            self.__coffee = coffee
        if money is not None:
            self.__money = money
        print("Refill complete!")

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

    def report(self):
        print("\n------ Coffee Machine Report ------")
        print(f"Status: {'ON' if self.__is_on else 'OFF'}")
        print(f"Water: {self.__water}ml")
        print(f"Milk: {self.__milk}ml")
        print(f"Coffee: {self.__coffee}g")
        print(f"Money: ${self.__money:.2f}")
        print("-----------------------------------")
