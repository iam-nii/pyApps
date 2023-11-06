from tkinter import *

def button_clicked():
    new_input = text_box.get()
    my_label.config(text=new_input)


window = Tk()
window.title("My first GUI python program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

#labels
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New text")
my_label.config(padx=30, pady=10)
my_label.grid(column=0, row=0)


#buttons
my_button = Button(text="Click Me", command=button_clicked, width=10)
my_button.grid(column=0, row=1)

# Entry
text_box = Entry(width=20)
text_box.grid(column=0, row=2)

window.mainloop()