import random
import requests

post_list = [
    {
        'id': 1,
        'title': 'Post 1'
    },
    {
        'id': 2,
        'title': 'Post 2'
    },
]


def get_posts():
    return post_list


def create_posts(post_data):
    new_post_data = post_data
    new_post_data['id'] = random.randint(1, 100)
    post_list.append(new_post_data)
    data = {
        'event_type': 'PostCreated',
        'data': new_post_data,
    }
    requests.post('http://localhost:5005/events/', json=data)
    return new_post_data
