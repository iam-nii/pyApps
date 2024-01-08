from flask import Flask, render_template
import post

POSTS = post.Post()

app = Flask(__name__)

@app.route('/')
def home():
    print(f"POSTS: {POSTS.posts}")
    return render_template("index.html", posts=POSTS.posts)

@app.route('/blog/<int:blog_id>')
def get_blogs(blog_id):
    return render_template('post.html', post_id=blog_id, posts=POSTS.posts)


if __name__ == "__main__":
    app.run(debug=True)
