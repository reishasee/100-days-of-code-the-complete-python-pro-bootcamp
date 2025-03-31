import pandas as pd

#TODO 1. Create a dictionary in this format:
nato = pd.read_csv("nato_phonetic_alphabet.csv")
letter_list = nato.letter.to_list()
code_list = nato.code.to_list()
nato_dict = {letter:code_list[letter_list.index(letter)] for letter in letter_list}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
phonetic_code_words = [nato_dict[letter] for letter in word]
print(phonetic_code_words)
