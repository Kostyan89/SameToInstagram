import requests
from flask import Flask, render_template, request
from functions import *
app = Flask(__name__)


@app.route('/')
def index():
    posts = get_posts()
    comments = get_comments()
    return render_template('index.html', posts=posts, comments=comments)


@app.route('/posts/<int:post_id>')
def page_index(post_id):
    posts = get_post_by_id(post_id)
    comments = get_comments_by_post_id(post_id)
    return render_template('post.html', comments=comments, post=posts)


@app.route('/search')
def page_search(word):
    data = request.args.get('s')
    posts = get_posts_by_word(word)
    return render_template('search.html', posts=posts, data=data)


@app.route('/users/<username>')
def page_users(username):
    posts = get_posts_of_user(username)
    return render_template('user-feed.html', posts=posts)


@app.errorhandler(404)
def page_not_found(e):
    return "Страница не найдена, но всё не так  плохо как кажется! Выпей чаю и через 5 мин попробуй еще раз"


if __name__ == '__main__':
    app.run(debug=True)
