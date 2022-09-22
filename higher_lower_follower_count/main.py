from art import logo, vs
from game_data import data
import random
# from replit import clear
import os

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guess, a_follwers, b_follwers):
    if a_follwers > b_follwers:
        return guess == "a"
    else:
        return guess == "b"


while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Copmpare A: {format_data(account_a)}")
    print(vs)
    print(f"Copmpare B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B'").lower()

    a_follwers_count = account_a["follower_count"]
    b_follwers_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follwers_count, b_follwers_count)
    os.system("cls")
    # clear()
    if is_correct:
        score += 1
        print(f"You're right. Your score is {score}")
    else:
        print(f"Sorry that's wrong. The final score are {score}")
        game_should_continue = False