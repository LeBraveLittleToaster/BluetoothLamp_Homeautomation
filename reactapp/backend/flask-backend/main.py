import flask, json
import time
from flask import jsonify
import bluetooth
from flask import request
from strips.strips_util import LedStripManager

from strips.modes import *

app = flask.Flask("__main__")

testStripsConfig = {
        "strips": [
            {
                "name": "Right Shelf",
                "id": 0,
                "mode": {
                    "mode_id": 1,
                    "mode_color_h" : 255,
                    "mode_color_s" : 0,
                    "mode_color_v" : 255
                },
                "mac_address" : "98:D3:31:F6:0E:28"
            }
        ]
    }

stripManager = LedStripManager(testStripsConfig)


@app.route("/")
def my_index():
    return flask.render_template("index.html", token="Hello Flask+React")


@app.route("/strips/")
def get_all_strips():
    rsp = {
        "strips" : stripManager.get_all_strips()
    }
    return jsonify(rsp)


@app.route("/strips/set", methods=['POST'])
def set_strip_mode():
    if stripManager.merge_strips(request.get_json()):
        stripManager.sendNetworkMsg()
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})


app.run(debug=True)

#stripManager.sendNetworkMsg()
#print("Sleeping 5sec")
#time.sleep(10)
