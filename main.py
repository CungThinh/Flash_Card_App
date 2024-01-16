from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
    
try:
    word_to_learn = pd.read_csv("/Users/cungthinh/Learn Python/Udemy Course/FlashCard/data/word_to_learn.csv")
except FileNotFoundError:
    word_to_learn = pd.read_csv("/Users/cungthinh/Learn Python/Udemy Course/FlashCard/data/french_words.csv")

random_row = pd.DataFrame()

def generate_new_word():
    global random_row, flip_timer
    window.after_cancel(flip_timer)
    random_row = word_to_learn.sample(1)
    canvas.itemconfig(card_front, image = card_front_img)
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text = random_row["French"].values[0], fill = "black")
    flip_timer = window.after(3000, func = flip_card)

def flip_card():
    canvas.itemconfig(card_front, image = card_back_img)
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text= random_row["English"].values[0], fill = "white")

def on_exit():
    word_to_learn.to_csv("/Users/cungthinh/Learn Python/Udemy Course/FlashCard/data/word_to_learn.csv", index=False)
    window.destroy()

def is_known():
    global word_to_learn
    word_to_learn.drop(random_row.index, inplace=True)
    generate_new_word()

window = Tk()
window.title("Flashy")
window.config(padx = 50, pady= 50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func = flip_card)

canvas = Canvas(height=526, width=800)
card_back_img = PhotoImage(file="/Users/cungthinh/Learn Python/Udemy Course/FlashCard/images/card_back.png")
card_front_img = PhotoImage(file="/Users/cungthinh/Learn Python/Udemy Course/FlashCard/images/card_front.png")
card_front = canvas.create_image(400, 263, image=card_front_img)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 181 ,text= "", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text = "", font= ("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


right_button_img = PhotoImage(file = "/Users/cungthinh/Learn Python/Udemy Course/FlashCard/images/right.png")
right_button = Button(image= right_button_img, highlightthickness= 0, command=is_known)
right_button.config(background=BACKGROUND_COLOR)
right_button.grid(row=1, column=0)

wrong_button_img = PhotoImage(file = "/Users/cungthinh/Learn Python/Udemy Course/FlashCard/images/wrong.png")
wrong_button = Button(image= wrong_button_img, highlightthickness= 0, command=generate_new_word)
wrong_button.config(background=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=1)

generate_new_word()

window.protocol("WM_DELETE_WINDOW", on_exit)
window.mainloop()