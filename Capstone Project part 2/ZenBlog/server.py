from flask import Flask, render_template, request
import requests
import post
import smtplib

BLOGS = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)

MY_EMAIL = "portopapii@gmail.com"
MY_PASSWORD = "scpg eymd zzqm hybc"

POSTS = {}


@app.route("/")
def home():
    global POSTS
    error = True

    request_blogs = requests.get(BLOGS)
    response = request_blogs.json()

    if request_blogs.status_code == 200:
        error = False
        POSTS = {
            'ids': [],
            'posts': {},
        }

        for post_ in range(len(response)):
            POSTS['ids'].append(response[post_]['id'])
            POSTS['posts'][post_ + 1] = {
                'title': response[post_]['title'],
                'subtitle': response[post_]['subtitle'],
                'body': response[post_]['body'],
            }

    return render_template("index.html", posts=POSTS, error_=error)


@app.route("/single-post/<int:blog_id>")
def single_post(blog_id):
    print(POSTS)
    post_title = POSTS['posts'][blog_id]['title']
    post_body = POSTS['posts'][blog_id]['body']

    _post = post.Post(post_title, post_body)
    return render_template("single-post.html", post=_post, post_id=blog_id)


@app.route("/categories")
def categories():
    return render_template("category.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/search-results")
def search_result():
    return render_template("search-result.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/Send_data", methods=['POST', 'GET'])
def send_data():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="aidk366@gmail.com", msg=f"Subject:{subject}!\n\n"
                                                                                      f"Name: {username}\n"
                                                                                      f"Email: {email}\n"
                                                                                      f"Message:{message}")

    return "<h1>Message successfully sent</h1>"


if __name__ == "__main__":
    app.run(debug=True)
