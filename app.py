import requests
from flask import Flask, render_template, request, abort
from functions import *
app = Flask(__name__)


@app.route('/')
def index():
    results = get_posts()
    return render_template('index.html', posts=results)


@app.route('/posts/<int:post_id>')
def page_post(post_id):
    post = get_post_by_id(post_id)
    if not post_id:
        abort(404)
    comments = get_comments_by_post_id(post_id)
    return render_template('post.html', comments=comments, post=post)


@app.route('/search')
def page_search():
    searching_word = request.args.get("s")
    if not searching_word:
        abort(404)
    posts = get_posts_by_word(searching_word)
    return render_template('search.html', posts=posts)


@app.route('/users/<username>')
def page_users(username):
    if not username:
        abort(404)
    users_posts = get_posts_by_username(username)
    return render_template('user-feed.html', users_posts=users_posts)


@app.errorhandler(404)
def page_not_found(e):
    return "Страница не найдена, но всё не так  плохо как кажется! Выпей чаю и через 5 мин попробуй еще раз"


if __name__ == '__main__':
    app.run()
