from tkinter import *
import requests


def get_quote():
    response = requests.get("https://bible-api.com/romans 3:16")
    response.raise_for_status()

    bible_verse = response.json()
    message = bible_verse['verses'][0]['text']
    canvas.itemconfig(quote_text, text=message)


window = Tk()
window.title("The Bible Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Bible Verse Goes HERE", width=250, font=("Arial", 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="bible.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()