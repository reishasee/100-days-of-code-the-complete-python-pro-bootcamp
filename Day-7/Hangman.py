import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)
#print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
incorrect_letters = []

while not game_over:

    print(f"**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    if guess in incorrect_letters or guess in correct_letters:
        print(f"You've already guessed {guess}. Please try again.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word and guess not in incorrect_letters:
        incorrect_letters.append(guess)
        print(f"You've guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True

            print(f"The correct word is {chosen_word}.")
            print(f"**************************** YOU LOSE ****************************")

    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN ****************************")

    print(stages[lives])
