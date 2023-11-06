import turtle

FONT = ('Courier', 10, 'bold')
ALIGNMENT = "center"
# setting up the screen
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.title(titlestring="U.S. States Game")

# Getting the data from the csv file
import pandas

data = pandas.read_csv("50_states.csv")
print(data)
states = data["state"].to_list()
guessed_states = []
states_to_learn = []
score = 0

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

while len(guessed_states) < 50:
    guess = screen.textinput(title=f"{score}/50 states correct", prompt="What's another state name?").title()

    if guess == "Exit":
        screen.bye() # exiting the screen
        states_to_learn = [state for state in states if state not in guessed_states]
        data_to_file = pandas.DataFrame(states_to_learn)
        print(data_to_file)
        data_to_file.to_csv("states_to_learn.csv")
        # for state in states:
        #     if state not in guessed_states:
        #         states_to_learn.append(state)
        break

    if guess in states:
        state_guess = data[data.state == guess]
        state_xcor = int(state_guess.x.iloc[0])
        state_ycor = int(state_guess.y.iloc[0])
        pen.goto(state_xcor, state_ycor)
        pen.write(arg=guess, align=ALIGNMENT, font=FONT)
        guessed_states.append(guess)
        #alternative approach: pen.write(arg=state_guess.state.item(), align=ALIGNMENT, font=FONT)



turtle.mainloop()  # An alternative to screen.exitonclick()
# screen.exitonclick()
