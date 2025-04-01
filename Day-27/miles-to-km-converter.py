from tkinter import *
WINDOW_WIDTH = 280
WINDOW_HEIGHT = 150
WINDOW_PADX = 75
WINDOW_PADY = 40
ENTRY_WIDTH = 12
SECOND_LINE_TEXT_PADY = 5
BG_COLOR = "white"

wn = Tk()
wn.title("Mile to Kilometer Converter")
wn.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
wn.config(padx=WINDOW_PADX, pady=WINDOW_PADY, background=BG_COLOR)

miles_input= Entry(width=ENTRY_WIDTH)
miles_input.grid(column=1, row=0)

miles_text = Label(text="miles")
miles_text.grid(column=2, row=0)
miles_text.config(background=BG_COLOR)

another_text = Label(text="is equal to")
another_text.grid(column=0, row=1)
another_text.config(pady=SECOND_LINE_TEXT_PADY, background=BG_COLOR)

km_text = Label(text="km")
km_text.grid(column=2, row=1)
km_text.config(pady=SECOND_LINE_TEXT_PADY, background=BG_COLOR)

km_calc = Label(text=0)
km_calc.config(pady=SECOND_LINE_TEXT_PADY, background=BG_COLOR)
km_calc.grid(column=1, row=1)

def button_clicked():
    miles = miles_input.get()
    km = 1.60934*float(miles)
    km_calc.config(text=km)
    return km_calc

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)

wn.mainloop()
