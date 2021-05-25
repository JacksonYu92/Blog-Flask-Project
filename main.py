from flask import Flask, render_template
from post import Post
import requests

def get_blogs():
    response = requests.get("https://api.npoint.io/ed99320662742443cc5b")
    response.raise_for_status()
    blogs = response.json()
    post_objects = [Post(blog['id'], blog['title'], blog['subtitle'], blog['body']) for blog in blogs]
    return post_objects

app = Flask(__name__)

@app.route('/')
def home():
    blogs = get_blogs()
    return render_template("index.html", blogs=blogs)

@app.route('/post/<int:id>')
def post(id):
    requested_post = None
    blogs =get_blogs()
    for blog in blogs:
        if blog.id == id:
            requested_post = blog
    return render_template("post.html", blog=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
