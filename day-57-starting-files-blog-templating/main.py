from flask import Flask, render_template
import post
import requests

BLOGS = "https://api.npoint.io/c790b4d5cab58020d391"


app = Flask(__name__)
POSTS = {}

@app.route('/')
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


@app.route('/blog/<int:blog_id>')
def get_blogs(blog_id):

    post_title = POSTS['posts'][blog_id]['title']
    post_body = POSTS['posts'][blog_id]['body']

    _post = post.Post(post_title, post_body)

    return render_template('post.html', post=_post)


if __name__ == "__main__":
    app.run(debug=True)
