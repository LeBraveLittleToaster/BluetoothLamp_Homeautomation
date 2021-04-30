import json

from flask_cors import CORS
from flask import Flask, request
from markupsafe import escape

from stripper.config.Config import Config
from stripper.managers.strip_manager import StripManager
from stripper.net_messages.device_messages import get_device_list_message

app = Flask(__name__)
CORS(app)

with open('../default_config.json') as config_json:
    config: Config = Config(json.load(config_json))

strips_manager = StripManager(config)
strips_manager.print()


# strips_manager.connect_all()


@app.route('/device/list', methods=['GET'])
def get_device_list():
    return get_device_list_message(strips_manager.strips)


@app.route('/device/<int:d_id>/mode/set', methods=['POST'])
def set_mode_for_strip_by_id(d_id):
    return "id " + str(d_id)


@app.route('/device/<int:d_id>/mode/send', methods=["GET"])
def send_mode_for_strip_by_id(d_id: int):
    return "id " + str(d_id)


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
