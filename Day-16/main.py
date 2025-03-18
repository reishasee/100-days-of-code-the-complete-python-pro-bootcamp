from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    user_order = input(f"What would you like? ({menu.get_items()}): ").lower()
    if user_order == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_order == "off":
        break
    else:
        menu_item = menu.find_drink(user_order)
        if coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
            coffee_maker.make_coffee(menu_item)
