from flask import Flask, render_template
import json
from functions import *
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/posts/<int:post_id>')
def page_index(post_id):
    comm = get_post_by_id(post_id)
    return render_template('post.html', comm=comm)


@app.route('/search/s=<word>')
def post_search(word):
    post = get_post_by_word(word)
    print(post)
    return render_template('search.html', post=post)











@app.errorhandler(404)
def page_not_found(e):
    return "Страница не найдена, но всё не так  плохо как кажется! Выпей чаю и через 5 мин попробуй еще раз"


app.run()