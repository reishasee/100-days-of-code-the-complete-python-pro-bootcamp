rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

choices = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors. "))
computer = random.randint(0, 2)

if user == 0 or user == 1 or user == 2:
    print(choices[user])

print("Computer chose:")
print(choices[computer])

if user > 2 or user < 0:
    print("You typed an invalid number. You lose.")
elif user == computer:
    print("It's a draw.")
elif user + 1 == computer or user - 2 == computer:
    print("You lose.")
elif user - 1 == computer or user + 2 == computer:
    print("You win.")
