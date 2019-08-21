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
    return stripManager.get_all_strips()


@app.route("/strips/set", methods=['POST'])
def set_strip_mode():
    if stripManager.merge_strips(request.get_json()):
        return {"success": True}
    else:
        return {"success": False}


app.run(debug=True)

