import random

import requests

post_list_comment = [
    {
        'id': 1,
        'title': 'Post 1',
        'comments': [
            {
                'id': 1,
                'content': 'Post 1'
            },
            {
                'id': 2,
                'content': 'Post 2'
            },
        ]
    },
    {
        'id': 2,
        'title': 'Post 2',
        'comments': [
            {
                'id': 1,
                'content': 'Comment 1'
            },
            {
                'id': 2,
                'content': 'Comment 2'
            },
        ]
    },
]


def get_posts():
    return post_list_comment


def create_post(post_data):
    post_list_comment.append(post_data)


def create_comment(post_id, comment_data):
    comment_data['id'] = random.randint(1, 1000)
    for post_comments in post_list_comment:
        if post_comments['id'] == post_id:
            post_comments.setdefault('comments', [])
            post_comments['comments'].append(comment_data)
            break
