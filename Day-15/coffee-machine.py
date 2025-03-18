MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(menu, order, res):
    water = menu[order]["ingredients"]["water"]
    try:
        milk = menu[order]["ingredients"]["milk"]
    except KeyError:
        milk = 0
    coffee = menu[order]["ingredients"]["coffee"]

    if water > res["water"]:
        print("Sorry, there is not enough water.")
        return 0
    elif milk > res["milk"]:
        print("Sorry, there is not enough milk.")
        return 0
    elif coffee > res["coffee"]:
        print("Sorry, there is not enough coffee.")
        return 0
    else:
        return 1

def process_coins(q, d, n, p):
    total = round((0.25 * q) + (0.10 * d) + (0.05 * n) + (0.01 * p), 2)
    return total

def check_transaction(coins, menu, order, mon):
    if coins < menu[order]["cost"]:
        print("Sorry, that's not enough money. MONEY REFUNDED.")
    else:
        change = round(coins - menu[order]["cost"], 2)
        mon = round(mon + coins - change, 2)
        print(f"Here is your change: ${change}")
        return mon

def make_coffee(menu, order, res):
    water = menu[order]["ingredients"]["water"]
    try:
        milk = menu[order]["ingredients"]["milk"]
    except KeyError:
        milk = 0
    coffee = menu[order]["ingredients"]["coffee"]

    res["water"] = res["water"] - water
    res["milk"] = res["milk"] - milk
    res["coffee"] = res["coffee"] - coffee

    print(f"Here is your {order}. Enjoy!")

def report(res, mon):
    print(f"Water: {res['water']}ml")
    print(f"Milk: {res['milk']}ml")
    print(f"Coffee: {res['coffee']}g")
    print(f"Money: ${mon}")

money = 0
is_on = True

while is_on:
    try:
        user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_order == 'report':
            report(resources, money)
        elif user_order == 'off':
            is_on = False
            print("Thank you for using our coffee machine. Have a nice day!")
        else:
            if check_resources(MENU, user_order, resources) == 0:
                pass
            else:
                while True:
                    try:
                        print("Please insert coins.")
                        quarters = int(input("How many quarters? "))
                        dimes = int(input("How many dimes? "))
                        nickels = int(input("How many nickels? "))
                        pennies = int(input("How many pennies? "))
                        total_payment = process_coins(quarters, dimes, nickels, pennies)
                        money = check_transaction(total_payment, MENU, user_order, money)
                        make_coffee(MENU, user_order, resources)
                        break
                    except ValueError:
                        print("Your input is invalid. Please try again.")
    except KeyError:
        print("Your order is invalid. Please try again.")
