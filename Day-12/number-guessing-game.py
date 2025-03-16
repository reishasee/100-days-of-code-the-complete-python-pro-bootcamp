from art import logo
import os
import random

is_play_again = True
attempts = -1
user_guess = 0

while is_play_again:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)

    check_level_input = False
    while not check_level_input:
        difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty_level == "easy":
            check_level_input = True
            attempts = 10
        elif difficulty_level == "hard":
            check_level_input = True
            attempts = 5
        else:
            print("Your input is invalid. Please try again.")

    is_game_over = False

    while not is_game_over:
        if attempts == 0:
            is_game_over = True
            print(f"You've run out of guesses. You LOSE.")
        else:
            print(f"You have {attempts} attempt/s remaining to guess the number.")
            check_user_guess = False
            while not check_user_guess:
                try:
                    user_guess = int(input("Make a guess: "))
                    if user_guess < 1 or user_guess > 100:
                        print("Your input is invalid. Please try again.")
                    else:
                        check_user_guess = True
                        if user_guess != number:
                            attempts -= 1
                            if attempts != 0:
                                if user_guess > number:
                                    print("Too high.")
                                else:
                                    print("Too low.")
                        else:
                            is_game_over = True
                            print("You are correct. You WIN!")
                except ValueError:
                    print("Your input is invalid. Please try again.")

    check_play_again = False
    while not check_play_again:
        play_again = input("Do you want to play another game? Type 'y' if YES, type 'n' if NO. ").lower()
        if play_again == 'n':
            is_play_again = False
            check_play_again = True
            print("Thank you for playing the Number Guessing Game. Have a nice day!")
        elif play_again == 'y':
            check_play_again = True
            os.system('cls')
        else:
            print("Your input is invalid. Please try again.")
