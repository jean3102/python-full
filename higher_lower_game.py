from data.influencers import influencers, vs, title
from os import system
import random


def print_influencer(influencer_a: dict, group: str):
    """Prints formatted influencer data"""

    name = influencer_a["name"]
    description = influencer_a["description"]
    country = influencer_a["country"]
    print(f"Comparete {group}: {name}, a {description} from {country}")


def compare_followers(follower_count_a: int, follower_count_b: int, choices: str):

    if choices == "a":
        return follower_count_a > follower_count_b
    if choices == "b":
        return follower_count_b > follower_count_a
    return False


def get_random_influencers():

    influencer_a = random.choices(influencers)
    influencer_b = random.choices(influencers)

    print_influencer(influencer_a[0], "A")
    print(vs)
    print_influencer(influencer_b[0], "B")
    return influencer_a[0]["follower_count"], influencer_b[0]["follower_count"]


def start_game():
    system("clear")
    score = 0
    while True:

        follower_count_a, follower_count_b = get_random_influencers()
        if follower_count_a == follower_count_b:
            continue

        choices = input(
            "who has more followers? Type 'A' or 'B' ").lower().strip()
        is_correct = compare_followers(
            follower_count_a, follower_count_b, choices)

        if not is_correct:
            system("clear")
            print(f"Sorry, that's wrong. Final score: {score}")
            break
        system("clear")
        score += 1
        print(f"You're right! Current score: {score}.")
    print(title)


start_game()
