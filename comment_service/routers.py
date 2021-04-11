from flask import request, jsonify

from app import app, API_PREFIX
from repositorys import get_post_comments, create_post_comments


@app.route(f'/{API_PREFIX}/posts/<int:post_id>/comments/', methods=['GET', 'POST'])
def comments_api(post_id):
    if request.method == 'POST':
        new_comment_data = dict(request.json or request.form)
        if not new_comment_data.get('content') or new_comment_data.get('content') == '':
            return jsonify({'message': 'Content fields is required'}), 400
        create_comment = create_post_comments(post_id, new_comment_data)
        return jsonify(create_comment), 201

    comments = get_post_comments(post_id)
    return jsonify(comments), 200
