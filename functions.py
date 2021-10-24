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
    for comm in read_comments():
        if comm['post_id'] == post_id:
            return comm














