# from art import logo
import random

# print (logo)
is_game_over = False


def play():
    print("Welcome to the Number guessing game")

    print("I am thinng to a number between 1 and 100.")

    chosen_number = random.randint(1, 100)

    print(chosen_number)

    first_attempts = 10

    if input(print("Chose a difficulty. Type 'easy' or 'hard' ")) == "easy":
        print(f"You have {first_attempts} attempts remainning to guess the number")
    else:
        first_attempts = 5
        print(f"You have {first_attempts} attempts remainning to guess the number")
    print(f"Make a guess")

    global is_game_over
    # global first_attempts
    player_number = int(input())

    while first_attempts >= 1 and is_game_over == False and first_attempts != player_number:
        if first_attempts <= 1:
            print("You lose")
            is_game_over = True
        elif player_number < chosen_number:
            print("Yout number is to small")
            # guess_method(player_number)
            first_attempts -= 1
            print(f"You have {first_attempts} attempts remainning to guess the number")
            print("Guess again")
            player_number = int(input())
        elif player_number > chosen_number:
            print("Yout number is to big")
            # guess_method(player_number)
            first_attempts -= 1
            print(f"You have {first_attempts} attempts remainning to guess the number")
            print("Guess again")
            player_number = int(input())
        elif player_number == chosen_number:
            print("You win")
            is_game_over = True


play()


# def guess_method(player_number=None):
#     global first_attempts
#     first_attempts -= 1
#     print(f"You have {first_attempts} attempts remainning to guess the number")
#     print("Guess again")
#     return player_number == int(input())


def restart():
    global is_game_over
    if input(print(f"Do you want to play another game? 'y' or 'n'")) == "y":
        play()


restart()
