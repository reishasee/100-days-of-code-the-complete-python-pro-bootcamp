from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_password = [random.choice(letters) for letter in range(random.randint(2, 10))]
    symbol_password = [random.choice(symbols) for symbol in range(random.randint(2, 10))]
    number_password = [random.choice(numbers) for number in range(random.randint(2, 10))]
    password_list = letter_password + symbol_password + number_password

    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)
    password_entry.insert(0, shuffled_password)
    pyperclip.copy(shuffled_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please do not leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title="Save Password",
                                       message=f"Do you want to save the following details? \nWebsite: {website} \nEmail/Username: {email} \nPassword: {password}")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, "end")
            email_entry.delete(0, "end")
            password_entry.delete(0, "end")

            website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

wn = Tk()
wn.title("Password Manager")
wn.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:", padx=5, pady= 5)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", padx=5, pady=5)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", padx=5, pady=5)
password_label.grid(column=0, row=3)

#Entry
website_entry = Entry(width=51)
website_entry.grid(column=1, columnspan=2, row=1)
website_entry.focus()

email_entry = Entry(width=51)
email_entry.grid(column=1, columnspan=2, row=2)
# email_entry.insert(0, "username@email.com")

password_entry = Entry(width=33)
password_entry.grid(column=1, columnspan=1, row=3)

#Button
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, columnspan=2, row=4)

wn.mainloop()
