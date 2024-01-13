from flask import Flask, render_template
import requests
import post

BLOGS = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
