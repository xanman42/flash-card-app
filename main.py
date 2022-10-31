from tkinter import *
import pandas


BACKGROUND_COLOR = "#B1DDC6"



# ----- UI-Setup ----- #
window = Tk()
window.title('Flash Card Learning')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
card.create_image(400, 263, image=card_front)
card.grid(column=1, row=1, columnspan=2)

wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=1, row=2)
right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column=2, row=2)

lang_lbl = Label(text='french', font=('Ariel', 40, 'italic'), bg='white')
lang_lbl.place(x=400, y=150, anchor='center')
word_lbl = Label(text='trouve', font=('Ariel', 60, 'bold'), bg='white')
word_lbl.place(x=400, y=253, anchor='center')




window.mainloop()
