import pandas
from tkinter import *
import random
import time

BACKGROUND = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 45, "bold")

data_frame = {}
# Getting the data from the file
try:
    data_frame = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_frame = pandas.read_csv("data/russian_words.csv")
finally:
    words_dict_list = data_frame.to_dict(orient="records")
#word_to_learn = data_frame.to_csv("words_to_learn.csv", index=False)

random_word = {}

def flip_card():
    english_word = random_word['English']
    if "," in english_word:
        long_word = english_word.split(",")
        english_word = long_word[0] + "\n" + long_word[1]

    # Changing the background content
    canvas.itemconfig(canvas_image, image=new_image)
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=english_word)


def display_cards():
    global random_word
    random_word = random.choice(words_dict_list)
    russian_word = random_word['Russian']

    if "/" in russian_word:
        long_word = russian_word.split("/")
        russian_word = long_word[0] + " /\n" + long_word[1]

    canvas.itemconfig(title_text, text="Russian")
    canvas.itemconfig(word_text, text=russian_word)
    canvas.itemconfig(canvas_image, image=old_image)
    window.after(3000, func=flip_card)


def is_known():
    # Remove the random generated word from the list
    print(random_word)
    words_dict_list.remove(random_word)
    display_cards()
    new_dataframe = pandas.DataFrame(words_dict_list)
    new_dataframe.to_csv("data/words_to_learn.csv", index=False)


window = Tk()
window.title("Rusky - English")
window.config(width=900, height=600, pady=50, padx=50, bg=BACKGROUND)


# Creating the flash card canvas
canvas = Canvas(width=800, height=530, bg=BACKGROUND, highlightthickness=0)
old_image = PhotoImage(file="./images/card_front.png")
new_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 265, image=old_image)
title_text = canvas_title = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
word_text = canvas_word = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Creating the buttons
# Wrong button
wrong_btn = Button()
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_btn.config(image=wrong_image, highlightthickness=0, command=display_cards)
wrong_btn.grid(row=1, column=0)

# Right button
right_btn = Button()
right_image = PhotoImage(file="./images/right.png")
right_btn.config(image=right_image, highlightthickness=0, command=is_known)
right_btn.grid(row=1, column=1)

# End

display_cards()



window.mainloop()