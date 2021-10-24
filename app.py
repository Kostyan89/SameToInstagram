from flask import Flask, render_template
import json
from functions import *
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/posts/<int:post_id>')
def page_index(post_id):
    post = get_post_by_id(post_id)
    comments = get_comments_by_post_id(post_id)
    return render_template('post.html', comments=comments, post=post)


@app.route('/search/s=<word>')
def page_search(word):
    posts = get_posts_by_word(word)
    return render_template('search.html', posts=posts)


@app.route('/users/<username>')
def page_users(username):
    posts = get_posts_of_user(username)
    print(posts)
    return render_template('user-feed.html', posts=posts)


@app.errorhandler(404)
def page_not_found(e):
    return "Страница не найдена, но всё не так  плохо как кажется! Выпей чаю и через 5 мин попробуй еще раз"


app.run(debug=True)