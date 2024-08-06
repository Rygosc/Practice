import random
import time
import sys
import math


def print_slowly(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print_slowly("That's not a valid number. Please enter a real number! :)")


def number_tries(x, y):
    n = abs(y) - abs(x) + 1
    result = math.log2(n)
    return math.ceil(result)


def greet_user():
    print_slowly("Hi! Welcome to my lil game 😇\nWould you like to play?")


def quit_game():
    print_slowly("Thank you for playing! Goodbye!")


def start_game():
    print_slowly("Type 'Start' to begin, or 'No' to quit: ")
    text = input().strip()
    while True:
        if text.lower() == "start":
            print_slowly("Welcome! Please, choose the game!")
            print_slowly("I have 2 games available:")
            print_slowly(
                "1. The Computer will pick a random number in a preferred range and you will have to guess it."
            )
            print_slowly(
                "2. You will pick a number in a preferred range and the Computer will guess it."
            )
            game_choice()
            break
        elif text.lower() == "no":
            quit_game()
            break
        else:
            print_slowly('Please, type "Start" to play, or "No" to quit. Thanks!')
            text = input().strip()


def game_choice():
    print_slowly("Enter '1' for game 1 or '2' for game 2: ")
    txt = input().strip()
    while True:
        if txt == "1":
            print_slowly("You chose game 1! Great!")
            human_guessing_the_number()
            break
        elif txt == "2":
            print_slowly("You chose game 2! Awesome!")
            computer_guessing()
            break
        else:
            print_slowly("Invalid choice. Please enter '1' or '2'.")
            txt = input().strip()


def human_guessing_the_number():
    print_slowly(
        "Please, indicate the range of guesses :) (the first and the last 'border')"
    )
    x = get_integer_input("Enter the lower bound: ")
    y = get_integer_input("Enter the upper bound: ")
    number = random.randint(x, y)
    tries = number_tries(x, y)
    print_slowly(f"You will have {tries} tries to guess the number😁")
    print_slowly("Guess my number😎:")
    custom_number = get_integer_input("Type your number here: ")
    while tries > 0:
        if custom_number < x or custom_number > y:
            print_slowly(
                "It seems that the number you put is out of range 🤔 Don't try to fool me! :)"
            )
            custom_number = get_integer_input("Type your number here: ")
        else:
            if number == custom_number:
                times = number_tries(x, y) - tries + 1
                print_slowly(
                    f"Yaaay! You got it! Great job 🤩 It took you {times} attempts to guess!"
                )
                try_again("human")
                break
            elif number > custom_number:
                print_slowly("Nu-uh🤪 Try higher!")
            else:
                print_slowly("Nope 🙃 Try lower!")
            custom_number = get_integer_input("Type your number here: ")
            tries -= 1

    if tries == 0:
        print_slowly(
            f"Nope, not correct. I am sorry 😢 You ran out of tries... The number was: {number}"
        )
        try_again("human")


def computer_guessing():
    print_slowly(
        "Please, indicate the range of guesses :) (the first and the last 'border')"
    )
    left = get_integer_input("Enter the lower bound: ")
    right = get_integer_input("Enter the upper bound: ")
    tries = number_tries(left, right)
    print(f"Watch me guessing your number in {tries} tries")

    while left <= right and tries > 0:
        middle = random.randint(left, right)
        print_slowly(f"Is your number {middle}? Type 'yes' or 'no': ")
        question = input().strip().lower()
        if question == "yes":
            print_slowly("😎😎😎 I guessed it!")
            try_again("computer")
            return
        elif question == "no":
            print_slowly(
                "Is it higher or lower? Type 'H' for higher, and 'L' for lower:"
            )
            lowerhigher = input().strip().lower()
            if lowerhigher == "h":
                left = middle + 1
            elif lowerhigher == "l":
                right = middle - 1
            else:
                print_slowly("Invalid input. Please respond with 'H' or 'L'.")
        else:
            print_slowly("Invalid input. Please respond with 'yes' or 'no'.")

        tries -= 1

    if tries == 0:
        print_slowly(
            "I couldn't guess your number in the given tries. It seems like we have a mismatch. 😢"
        )
        try_again("computer")


def try_again(game_mode):
    print_slowly(
        "Would you like to play again? Type 'yes' to play again, 'no' to quit, or 'switch' to switch game mode:"
    )
    text = input().strip().lower()
    if text == "yes":
        print_slowly("Great! Let's start a new game.")
        if game_mode == "human":
            human_guessing_the_number()
        elif game_mode == "computer":
            computer_guessing()
    elif text == "no":
        quit_game()
    elif text == "switch":
        game_choice()
    else:
        print_slowly("Invalid input. Please type 'yes', 'no', or 'switch'.")
        try_again(game_mode)


if __name__ == "__main__":
    greet_user()
    start_game()
