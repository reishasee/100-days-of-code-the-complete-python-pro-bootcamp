BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "French"
DATA_FILE = "french_words.csv"

from tkinter import *
import pandas as pd
import random
random_vocab = {}

wn = Tk()
wn.title("Flash Card App")
wn.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip = wn.after(ms=3000, func=lambda: change_card(random_vocab["English"]))

try:
    data = pd.read_csv(f"data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv(f"data/{DATA_FILE}")

data_dict = data.to_dict(orient="records")
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")

#-------------------------------------------------- NEXT VOCAB --------------------------------------------------#
def next_vocab():
    global random_vocab, flip
    wn.after_cancel(flip)
    random_vocab = random.choice(data_dict)
    canvas.itemconfig(lang_text, text=LANGUAGE, fill="black")
    canvas.itemconfig(vocab_text, text=f"{random_vocab[LANGUAGE]}", fill="black")
    canvas.itemconfig(front_img, image=card_front)
    flip = wn.after(ms=3000, func=lambda: change_card(random_vocab["English"]))

#-------------------------------------------------- CORRECT ANSWER --------------------------------------------------#
def right():
    data_dict.remove(random_vocab)
    new_data = pd.DataFrame(data_dict)
    new_data.to_csv("data/words_to_learn.csv")
    next_vocab()

#-------------------------------------------------- CARD BACK --------------------------------------------------#
def change_card(word):
    canvas.itemconfig(front_img, image=card_back)
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(vocab_text, text=word, fill="white")

#-------------------------------------------------- CARD FRONT --------------------------------------------------#
#Create canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

#Insert canvas image
front_img = canvas.create_image(400, 263, image=card_front)

#Access data
# first_vocab = random.choice(data_dict)[LANGUAGE]

#Insert canvas text
lang_text = canvas.create_text(400, 150, font=("Arial", 40, "italic"), text=LANGUAGE)
vocab_text = canvas.create_text(400, 263, font=("Arial", 40, "bold"), text="")
canvas.grid(column=0, columnspan=2, row=0)

#Create buttons
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, bd=0, command=right)
right_button.grid(column=1, row=1)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, bd=0, command=next_vocab)
wrong_button.grid(column=0, row=1)

next_vocab()

wn.mainloop()
