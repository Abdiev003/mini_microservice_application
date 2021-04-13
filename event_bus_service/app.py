import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_VERSION = 'v1.0'
API_PREFIX = f'api/{API_VERSION}'


@app.route('/events/', methods=['POST'])
def events():
    data = dict(request.form or request.json)
    requests.post('http://localhost:5000/events/', json=data)
    requests.post('http://localhost:5001/events/', json=data)
    requests.post('http://localhost:5002/events/', json=data)

    return jsonify({'message': 'success'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5005)
