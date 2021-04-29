import json

from flask.json import jsonify
from flask_cors import CORS
from flask import Flask
from markupsafe import escape

from stripper.config.Config import Config

app = Flask(__name__)
CORS(app)


with open('../default_config.json') as config_json:
    config: Config = Config(json.load(config_json))





@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


app.run("0.0.0.0", 4321)