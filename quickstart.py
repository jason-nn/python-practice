import json
from flask import Flask, jsonify
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home Page'


@app.route('/<name>')
def hello_name(name):
    return f'Hello, {escape(name.title())}!'


@app.route('/user/<username>')
def show_user(username):
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {escape(post_id)}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'


@app.route('/json')
def show_json():
    return jsonify({
        'first_name': 'Tanjiro',
        'last_name': 'Kamado',
    })
