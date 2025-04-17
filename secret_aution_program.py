print("Welcome to the secret aution program")


def start_auction():
    is_end = False
    bid_list = {}

    while not is_end:
        name = input("What is your name?: ")
        bid = int(input("What's your bid?: "))
        continue_auction = input(
            "Are there any other bidders? Type 'yes' or 'no'. ")

        bid_list[name] = bid

        if continue_auction == "no":
            is_end = True

    return bid_list


def find_winner(bin_list):
    winner = ""
    hignest_bid = 0
    for name in bin_list:
        bid_amount = bin_list[name]
        if bid_amount > hignest_bid:
            hignest_bid = bid_amount
            winner = name
    print(f"The winner is {winner} with a bid of ${hignest_bid}")


bin_list = start_auction()
find_winner(bin_list)
