import random
import os
RANKS = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}


def get_random_card() -> str:
    return random.choice(list(RANKS.keys()))


def print_message(player_result, computer_result):
    player, player_score = player_result
    computer, computer_score = computer_result
    print(f"Your final hand: {player}, final score: {player_score}")
    print(
        f"Computer's final hand: {computer}, final score: {computer_score}")


def determinate_winner(player_score: int, computer_score: int):
    if player_score > 21:
        print("You lose 😭!")
    elif computer_score > 21 or player_score > computer_score:
        print("You win 😁!")
    elif computer_score == player_score:
        print("Draw 🖐️")
    else:
        print("You lose 😭!")


def play_game():
    os.system("clear")
    player_turn = True
    player: list[int] = [RANKS[get_random_card()]]
    computer: list[int] = [RANKS[get_random_card()]]

    player_score = sum(player)
    computer_score = sum(computer)

    while True:
        if player_turn:
            player_score = sum(player)
            computer_score = sum(computer)
            player.append(RANKS[get_random_card()])

            print(f"Your cards: {player}, current score: {player_score}")
            print(f"Computer's first card: {computer}")
            print("-----------------------------------")

            if player_score > 21:
                break

            choise = input(
                "Type 'y' to get another card, type 'n' to pass: ").strip()

            if choise == 'n':
                player_turn = False
        else:
            computer.append(RANKS[get_random_card()])
            computer_score = sum(computer)
            if computer_score > 21 or computer_score > player_score:
                break

    print_message([player, player_score], [computer, computer_score])
    determinate_winner(player_score, computer_score)


print("Black jack Game")
play_game()
