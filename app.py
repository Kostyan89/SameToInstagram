from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/posts/<int:post_id>')
def posts_page(post_id):
    with open ('data.json', 'r') as f:
        comments = json.load(f)

    return render_template("post.html", comments=comments, post_id=post_id)





@app.errorhandler(404)
def page_not_found(e):
    return "Страница не найдена, но всё не так  плохо как кажется! Выпей чаю и через 5 мин попробуй еще раз"


app.run()