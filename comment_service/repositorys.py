import random

post_list_comment = [
    {
        'id': 1,
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
    {
        'id': 93,
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
    {
        'id': 63,
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
    {
        'id': 47,
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


def get_post_comments(post_id):
    for post_comment in post_list_comment:
        if post_comment['id'] == post_id:
            return post_comment
    return None


def create_post_comments(post_id, comment_content):
    comment_content['id'] = random.randint(1, 1000)
    for post_comments in post_list_comment:
        if post_comments['id'] == post_id:
            post_comments.setdefault('comments', [])
            post_comments['comments'].append(comment_content)
            break
    else:
        new_post = {
            'id': post_id,
            'comments': [
                comment_content
            ]
        }
        post_list_comment.append(new_post)
    return comment_content
