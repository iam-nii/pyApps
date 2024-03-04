from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

BLOGS = "https://api.npoint.io/c790b4d5cab58020d391"


@app.route("/")
def home():
    return "<h1>Home Page</h1>"


@app.route("/guess/<username>")
def guess(username: str):
    date = datetime.now()
    year = date.year
    name = username.title()

    response = requests.get(f"https://api.agify.io/?name={name}")
    print(response.status_code)
    age = response.json()['age']

    response = requests.get(f"https://api.genderize.io/?name={name}")
    print(response.status_code)
    gender = response.json()['gender']

    return render_template("index.html", year=year, age=age, name=name, gender=gender)


@app.route("/blogs")
def blogs():
    response = requests.get(BLOGS)
    all_posts = response.json()
    print(all_posts)

    return render_template("blogs.html", posts=all_posts)


if __name__ == "__main__":
    app.run()