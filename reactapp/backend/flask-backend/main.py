import flask, json
from flask import request
from strips.strips_util import LedStripManager

app = flask.Flask("__main__")

testStripsConfig = {
        "strips": [
            {
                "name": "Right Shelf",
                "id": 0,
                "mode": {
                    "mode_id": 1,
                    "mode_color_r": 0,
                    "mode_color_g": 0,
                    "mode_color_b": 255
                }
            },
            {
                "name": "Left Shelf",
                "id": 1,
                "mode": {
                    "mode_id": 2,
                    "mode_color_r": 0,
                    "mode_color_g": 0,
                    "mode_color_b": 255,
                    "mode_speed": 0.5
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
    return stripManager.get_all_strips()


@app.route("/strip/set/mode/<strip_id>")
def set_strip_mode(strip_id):
    if stripManager.set_mode(strip_id, json.load(request.data)):
        return {"success": True}
    else:
        return {"success": False}


app.run(debug=True)

