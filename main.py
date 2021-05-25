from flask import Flask, render_template
import requests

def get_blogs():
    response = requests.get("https://api.npoint.io/ed99320662742443cc5b")
    response.raise_for_status()
    blogs = response.json()
    return blogs

app = Flask(__name__)

@app.route('/')
def home():
    blogs = get_blogs()
    print(blogs)
    return render_template("index.html", blogs=blogs)

@app.route('/post/<id>')
def post(id):
    blog = get_blogs()[int(id)-1]
    return render_template("post.html", blog=blog)

if __name__ == "__main__":
    app.run(debug=True)
