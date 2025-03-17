from art import logo, vs
import random
from game_data import data
from os import system, name

# define our clear function
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')
    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')

def soc_acct_data(account):
    acct_name = account["name"]
    acct_desc = account["description"]
    acct_country = account["country"]
    return f"{acct_name}, a {acct_desc}, from {acct_country}"

score = 0
answer = ""
is_game_over = False
a = {}

while not is_game_over:
    print(logo)

    if score == 0:
        a = random.choice(data)
    else:
        print(f"You're right! Current score: {score}")
    a_followers = a["follower_count"]
    print("Compare A: " + soc_acct_data(a))
    print(vs)

    b = random.choice(data)
    b_followers = b["follower_count"]
    print("Compare B: " + soc_acct_data(b))

    check_answer = False
    while not check_answer:
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if answer != 'a' and answer != 'b':
            print("Your input is invalid. Please try again.")
        else:
            check_answer = True

    if answer == 'a' and a_followers > b_followers:
        score += 1
        a = b
        clear()
    elif answer == 'b' and b_followers > a_followers:
        score += 1
        a = b
        clear()
    else:
        is_game_over = True
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")
