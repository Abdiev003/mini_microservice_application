import random

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
    return new_post_data
