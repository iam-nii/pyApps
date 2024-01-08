import requests
BLOGS = "https://api.npoint.io/c790b4d5cab58020d391"

class Post:

    def __init__(self):
        self.response = requests.get(BLOGS)
        self.posts = self.get_posts()

    def get_posts(self):
        posts = self.response.json()
        return posts
