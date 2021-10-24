from flask import Flask, render_template
import json
from functions import *
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/posts/<int:pk>')
def post_page(pk):
    posts = get_posts()
    return render_template("post.html", posts=posts, post_id=post_id)




@app.errorhandler(404)
def page_not_found(e):
    return "Страница не найдена, но всё не так  плохо как кажется! Выпей чаю и через 5 мин попробуй еще раз"


app.run()