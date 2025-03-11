from art import logo
import os

operation = ["+", "-", "*", "/"]

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def chosen_operation(input_operation, n1, n2):
    if input_operation == "+":
        return add(n1, n2)
    elif input_operation == "-":
        return subtract(n1, n2)
    elif input_operation == "*":
        return multiply(n1, n2)
    elif input_operation == "/":
        return divide(n1, n2)

new_calc = False

while not new_calc:
    print(logo)
    first_num_check = False
    while not first_num_check:
        first_num = input("What's the first number? ")
        if first_num.isnumeric():
            first_num_check = True
            first_num = int(first_num)
        else:
            print("The value that you entered is invalid. Please try again.")

    continue_calc = True
    while continue_calc:
        pick_operation_check = False
        while not pick_operation_check:
            pick_operation = input(f"Pick an operation {operation}: ")
            if pick_operation in operation:
                pick_operation_check = True
            else:
                print("The value that you entered is invalid. Please try again.")

        next_num_check = False
        while not next_num_check:
            next_num = input("What's the next number? ")
            if next_num.isnumeric():
                next_num_check = True
                next_num = int(next_num)
            else:
                print("The value that you entered is invalid. Please try again.")

        answer = chosen_operation(pick_operation, first_num, next_num)
        print(f"{first_num} {pick_operation} {next_num} = {answer}")

        continue_calc_check = False
        while not continue_calc_check:
            continue_calc_ans = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. ")
            if continue_calc_ans != 'y' and continue_calc_ans != 'n':
                print("The value that you entered is invalid. Please try again.")
            elif continue_calc_ans == 'y':
                continue_calc_check = True
                first_num = answer
            else:
                continue_calc_check = True
                continue_calc = False
                os.system('cls')
