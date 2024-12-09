print("Welcome to the tip calculator")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people split the bill? "))

total_bill = bill * (1 + (tip/100))
per_pax = round(total_bill / num_people, 2)

print(f'Each person should pay: ${per_pax}')
