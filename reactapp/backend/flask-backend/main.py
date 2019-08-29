import flask, json;
from flask import jsonify;
from flask import request
from strips.strips_util import LedStripManager

app = flask.Flask("__main__")

testStripsConfig = {
        "strips": [
            {
                "name": "Right Shelf",
                "id": 0,
                "mode": {
                    "mode_id": 0
                }
            },
            {
                "name": "Couch",
                "id": 0,
                "mode": {
                    "mode_id": 0
                }
            },
            {
                "name": "Left Shelf",
                "id": 0,
                "mode": {
                    "mode_id": 0
                }
            }
        ]
    }

stripManager = LedStripManager(testStripsConfig)


@app.route("/")
def my_index():
    return flask.render_template("index.html", token="Hello Flask+React")


@app.route("/strips/")
def get_all_strips():
    return jsonify(stripManager.get_all_strips())


@app.route("/strips/set", methods=['POST'])
def set_strip_mode():
    if stripManager.merge_strips(request.get_json()):
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})


app.run(debug=True)

