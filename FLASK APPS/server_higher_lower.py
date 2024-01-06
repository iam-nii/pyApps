import random
from flask import Flask

app = Flask(__name__)

number = random.randint(0, 9)

@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src= 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width='300'>"

# print(number)
@app.route("/<int:guess>")
def guess(guess):
    if guess > number:
        return f"<h1 style='color: purple'>{guess} is too high, try again!</h1>" \
               f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < number:
        return f"<h1 style='color: red'>{guess} is oo low, try again!</h1>"\
               f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)