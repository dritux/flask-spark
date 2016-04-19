from flask import jsonify
from . import app
from utils import requires_api_key, requires_json


@app.route('/')
def index():
    response = {"service": "Spark run service",
                "api_version": "1"}
    return jsonify(response)


@app.route('/api/files', methods=['GET'])
@requires_json
@requires_api_key
def get_files():
    return 'get'


@app.route('/api/files', methods=['POST'])
@requires_json
@requires_api_key
def post_files():
    return 'post'


@app.route('/api/files', methods=['PUT'])
@requires_json
@requires_api_key
def put_files():
    return 'put'


@app.route('/api/files', methods=['DELETE'])
@requires_json
@requires_api_key
def delete_files():
    return 'delete'

