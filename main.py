from tkinter import *
import pandas
from random import randint

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv('data/french_words.csv')
data_list = data.to_dict(orient="records")


# ----- Flipper ----- #
def flipper():
    global language
    if language == 'French':
        language = 'English'
        lang_lbl.config(text=language, fg='white', bg='green')
        word_lbl.config(text=dataset[language], fg='white', bg='green')
        card.itemconfig(current_image, image=card_back)
    else:
        language = 'French'
        lang_lbl.config(text=language, fg='black', bg='white')
        word_lbl.config(text=dataset[language], fg='black', bg='white')
        card.itemconfig(current_image, image=card_front)

    window.after(3000, flipper)


# ----- Button functions -----#
def wrong():
    global dataset
    random_pos = randint(0, len(data_list) - 1)
    dataset = data_list[random_pos]
    word_lbl.config(text=dataset[language])


def right():
    global dataset
    random_pos = randint(0, len(data_list) - 1)
    dataset = data_list[random_pos]
    word_lbl.config(text=dataset[language])


# ----- UI-Setup ----- #
window = Tk()
window.title('Flash Card Learning')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
current_image = card.create_image(400, 263, image=card_front)
card.grid(column=1, row=1, columnspan=2)

wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=wrong)
wrong_button.grid(column=1, row=2)
right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0, command=right)
right_button.grid(column=2, row=2)

language = 'French'
lang_lbl = Label(text=language, font=('Ariel', 40, 'italic'), bg='white')
lang_lbl.place(x=400, y=150, anchor='center')
random_pos = randint(0, len(data_list) - 1)
dataset = data_list[random_pos]
word_lbl = Label(text=dataset[language], font=('Ariel', 60, 'bold'), bg='white')
word_lbl.place(x=400, y=253, anchor='center')

flipper()

window.mainloop()
