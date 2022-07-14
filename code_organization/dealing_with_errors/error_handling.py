from flask import Flask, jsonify, abort
from blogs import fetch_blogs, fetch_blog
from db import NotFoundError


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/blogs')
def all_blogs():
    try:
        return jsonify(fetch_blogs())
    except NotFoundError:
        abort(404, description="Resource not found!")

@app.route('/blogs/<id>')
def get_blog(id):
    try:
        return jsonify(fetch_blog(id))
    except NotFoundError:
        abort(404, description="Resource not found!")

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)