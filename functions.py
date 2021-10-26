import json
from typing import List

COMMENTS_PATH: str = "data/comments.json"
POSTS_PATH: str = "data/data.json"


def read_data():
    with open('data/data.json', 'r', encoding='utf8') as f:
        data = json.load(f)
        return data


def read_comments():
    with open('data/comments.json', 'r', encoding='utf8') as f:
        comments = json.load(f)
        return comments


def get_post_by_id(post_id):
    for post in read_data():
        if post['pk'] == post_id:
            return post


def get_comments_by_post_id(post_id):
    comments = []
    for comm in read_comments():
        if comm['post_id'] == post_id:
            comments.append(comm)
    return comments


def get_posts_by_word(word):
    for post in read_data():
        if word.lower() in post["content"].lower():
            return post


def get_posts_by_username(username):
    users_posts = []
    for post in read_data():
        if post["poster_name"] == username:
            users_posts.append(post)
    return users_posts


def get_posts():
    posts = read_data()
    return posts


def get_comments():
    comments = read_comments()
    return comments
