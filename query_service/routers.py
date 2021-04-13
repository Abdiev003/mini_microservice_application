import requests
from flask import request, jsonify

from app import app, API_PREFIX
from repositorys import get_posts, create_post, create_comment


@app.route(f'/{API_PREFIX}/posts/', methods=['GET'])
def posts():
    posts = get_posts()
    return jsonify(posts), 200


@app.route('/events/', methods=['POST'])
def events():
    data = dict(request.form or request.json)
    action_data = data.get('data')
    action_id = data.get('post_id')
    if data.get('event_type') == 'PostCreated':
        create_post(action_data)
    if data.get('event_type') == 'CommentCreated':
        create_comment(action_id, action_data)
    return jsonify({'message': 'success'})

