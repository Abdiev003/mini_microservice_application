from flask import request, jsonify

from app import app, API_PREFIX
from repositorys import get_posts, create_posts


@app.route(f'/{API_PREFIX}/posts/', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        post_data = dict(request.json or request.form)
        if not post_data.get('title') or post_data.get('title') == '':
            return jsonify('{message: Title fields is required}'), 400
        new_post_data = create_posts(post_data)
        return jsonify(new_post_data), 201
    post_list = get_posts()
    return jsonify(post_list), 200
