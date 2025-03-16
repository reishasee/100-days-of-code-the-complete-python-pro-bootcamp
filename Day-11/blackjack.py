import os
import random
from art import logo

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        index_eleven = cards.index(11)
        cards[index_eleven] = 1

    return sum(cards)

def compare(u_score, comp_score):
    if u_score == comp_score:
        return "It's a DRAW."
    elif comp_score == 0 or u_score > 21:
        return "You LOSE."
    elif u_score == 0 or comp_score > 21 or u_score > comp_score:
        return "You WIN!"
    else:
        return "You LOSE."

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        check_deal = False
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            while not check_deal:
                user_should_deal = input("Type 'y' to get another card, type 'n' to pass. ").lower()
                if user_should_deal == 'y' or user_should_deal == 'n':
                    check_deal = True
                    if user_should_deal == 'y':
                        user_cards.append(deal_card())
                    else:
                        is_game_over = True
                else:
                    print("You've entered an invalid input. Please try again.")

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

start_game = True
while start_game:
    check_play = False
    while not check_play:
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if play == 'y':
            check_play = True
            os.system('cls')
            play_game()
        elif play == 'n':
            check_play = True
            start_game = False
            print("Thank you for playing Blackjack. Have a nice day!")
        else:
            print("You've entered an invalid input. Please try again.")
