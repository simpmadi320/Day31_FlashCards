from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

current_card = {}

# Gets records
# Part 2
data = pandas.read_csv("data/french_words.csv")
word_dictionary = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    try:
        window.after_cancel(flip_timer)
    except:
        pass
    flip_to_french()
    current_card = random.choice(word_dictionary)
    canvas.itemconfig(word_l, text=current_card["French"])
    flip_timer = window.after(3000, flip_to_english)


def correct_answer():
    next_card()


def wrong_answer():
    next_card()


def flip_to_english():
    canvas.itemconfig(canvas_image, image=CARD_BACK_IMAGE)
    canvas.itemconfig(language_l, fill="white", text="English")
    canvas.itemconfig(word_l, fill="white", text=current_card["English"])


def flip_to_french():
    canvas.itemconfig(canvas_image, image=CARD_FRONT_IMAGE)
    canvas.itemconfig(language_l, fill="black", text="French")
    canvas.itemconfig(word_l, fill="black")


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

CARD_BACK_IMAGE = PhotoImage(file="images/card_back.png")
CARD_FRONT_IMAGE = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 265, image=CARD_FRONT_IMAGE)

wrong_pi = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_pi, highlightthickness=0, command=wrong_answer)
wrong_button.grid(row=1, column=0)

right_pi = PhotoImage(file="images/right.png")
right_button = Button(image=right_pi, highlightthickness=0, command=correct_answer)
right_button.grid(row=1, column=1)

language_l = canvas.create_text(400, 150, text="French", fill="black", font=LANGUAGE_FONT, anchor="n")
word_l = canvas.create_text(400, 263, text="trouve", fill="black", font=WORD_FONT, anchor="n")

next_card()

window.mainloop()
