from art import logo
import os

end_bid = False
bidders = {}
    
while not end_bid:
    print(logo)
    bidder_name = input("What is your name? ").lower()

    check_bid = False

    while not check_bid:
        bid = input("What is your bid? $")
        if bid.isnumeric():
            check_bid = True
            bid = int(bid)
            bidders[bidder_name] = bid
        else:
            print("Your input is invalid. Please try again.")
            
    check_other_bidders = False

    while not check_other_bidders:
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no.' ").lower()
        if other_bidders != 'yes' and other_bidders != 'no':
            print("Your input is invalid. Please try again. ")
        elif other_bidders == 'no':
            check_other_bidders = True
            end_bid = True
        else:
            check_other_bidders = True
            
    os.system('cls')
    
highest_bidder = ""
highest_bid = 0

for name, bid_price in bidders.items():
    if bid_price > highest_bid:
        highest_bid = bid_price
        highest_bidder = name

# print(bidders)
print(f'The winner is {highest_bidder} with a bid of ${highest_bid}.')
