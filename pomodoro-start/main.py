from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
FONT = (FONT_NAME, 50, "bold")
WORK_MIN = 0.2
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps = 0
check = "✔"
mark = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
# noinspection PyTypeChecker
def reset_timer():
    global timer, reps, mark
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    window.after_cancel(timer)
    reps = 0
    mark = ""


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break)
        label.config(text="Long Break", fg=RED)
        reps = 0
    elif reps % 2 == 0:
        count_down(short_break)
        label.config(text="Break", fg=PINK)
        reps += 1
    else:
        count_down(work_time)
        label.config(text="Work", fg=GREEN)
        reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, mark
    minutes = math.floor(count / 60)
    seconds = round(count % 60, 2)

    if seconds < 10:
        seconds = "0" + str(seconds)

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            mark += check
            check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro App")

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="0:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Label
label = Label()
label.config(text="Timer", bg=YELLOW, font=FONT, fg=GREEN)
label.grid(column=1, row=0)

# Buttons
start_btn = Button(command=start_timer)
start_btn.config(text="Start", highlightthickness=0)
start_btn.grid(column=0, row=2)

reset_btn = Button(command=reset_timer)
reset_btn.config(text="Reset", highlightthickness=0)
reset_btn.grid(column=2, row=2)

# Check marks
check_marks = Label()
check_marks.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()
