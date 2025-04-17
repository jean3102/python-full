
def welcome_message():
    print("Welcome to the Secret Auction Program!")


def collect_bids():
    bid_list = {}

    while True:
        name = input("What is your name?: ")
        try:
            bid = int(input("What's your bid?: "))
        except ValueError:
            print("Please enter a valid number for ther bid")
            continue

        continue_auction = input(
            "Are there any other bidders? Type 'yes' or 'no'. ").strip().lower()

        bid_list[name] = bid

        if continue_auction == "no":
            break

    return bid_list


def get_highest_bidder(bid_records):
    highest_bid = 0
    winner = ""
    for bidder, amount in bid_records.items():
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    return winner, highest_bid


def run_auction():
    welcome_message()
    bids = collect_bids()
    winner, amount = get_highest_bidder(bids)
    print(f"\n🏆 The winner is {winner} with a bid of ${amount}!")


run_auction()
