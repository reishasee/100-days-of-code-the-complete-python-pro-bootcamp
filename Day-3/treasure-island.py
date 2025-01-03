print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_challenge = input("You're at a cross road. Where do you want to go? \n     Type 'left' or 'right' ").lower()
if first_challenge == 'left':
    second_challenge = input("You've come to a lake. There is an island in the middle of the lake. \n     Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()

    if second_challenge == 'wait':
        third_challenge = input("You arrived at the island unharmed. There is a house with 3 doors. \nOne red, one yellow, one blue. \n     Which color do you choose? Type 'red', 'yellow', or 'blue' ").lower()

        if third_challenge == 'yellow':
            print("You found the treasure! You win!")
        elif third_challenge == 'red':
            print("It's a room full of fire. Game over.")
        elif third_challenge == 'blue':
            print("You enter a room full of beasts. Game over.")
        else:
            print("You entered an invalid color. Game over.")

    elif second_challenge == 'swim':
        print("You get attacked by an angry trout. Game over.")

    else:
        print("Your input is invalid. Game over.")

elif first_challenge == 'right':
    print("You fell into a hole. Game over.")

else:
    print("Your input is invalid. Game over.")

