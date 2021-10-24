import json
from typing import List

COMMENTS_PATH: str = "data/comments.json"
POSTS_PATH: str = "data/data.json"


def read_file(filename: str) -> List[dict]:
    with open(filename, encoding='utf-8') as f:
        return json.load(f)


def get_comments_by_post_id(post_id: int) -> List[dict]:
    results = []
    for comment in read_file(COMMENTS_PATH):
        if comment['post_id'] == post_id:
            results.append(comment)
    return results


def get_posts() -> List[dict]:
    results = []
    for post in read_file(POSTS_PATH):
        post['comments_count'] = len(get_comments_by_post_id(post['pk']))
        results.append(post)
    return results


