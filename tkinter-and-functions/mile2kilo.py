from tkinter import *

window = Tk()
window.minsize(width=250, height=100)
window.config(padx=10, pady=10)
window.title("Miles to Kilometers")

def calc():
    miles = miles_txt.get()
    result = float(miles) * 1.609
    result_label.config(text=f"{result}")


miles_txt = Entry()
miles_txt.config(width=20)
miles_txt.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_txt = Label(text="Km")
km_txt.grid(column=2, row=1)

calculate = Button(text="Calculate")
calculate.config(command=calc)
calculate.grid(column=1, row=2)

window.mainloop()