import flask, json
import time
from flask import jsonify
import bluetooth
from flask import request
from flask_cors import CORS, cross_origin
from strips.strips_util import LedStripManager

from strips.modes import *


app = flask.Flask("__main__")
cors = CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'

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
print("Creating sockets")
stripManager = LedStripManager(testStripsConfig)
print("Starting frontend")


@app.route("/")
def my_index():
    return flask.render_template("index.html", token="Hello Flask+React")


@app.route("/strips/")
@cross_origin()
def get_all_strips():
    rsp = {
        "strips" : stripManager.get_all_strips()
    }
    return jsonify(rsp)


@app.route("/strips/set", methods=['POST'])
@cross_origin()
def set_strip_mode():
    print(request.get_json())
    if stripManager.merge_strips(request.get_json()["strips"]):
        stripManager.sendNetworkMsg()
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})


app.run(host='0.0.0.0',port=5000, debug=True)

#stripManager.sendNetworkMsg()
#print("Sleeping 5sec")
#time.sleep(10)
