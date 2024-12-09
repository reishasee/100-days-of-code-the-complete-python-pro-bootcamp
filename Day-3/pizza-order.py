print("Welcome to Python Pizza Deliveries")

size = input("What size pizza do you want? S, M, or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

if size == 's':
    size_price = 15
elif size == 'm':
    size_price = 20
elif size == 'l':
    size_price = 25
else:
    print("You typed the wrong input.")
    
if pepperoni == 'y' and size == 's':
    add_pep = 2
elif pepperoni == 'y' and size == 'm' or size == 'l':
    add_pep = 3
else:
    add_pep = 0

if extra_cheese == 'y':
    add_extra_cheese = 1
else:
    add_extra_cheese = 0

final_bill = size_price + add_pep + add_extra_cheese

print(f'Your final bill is: ${final_bill}')
