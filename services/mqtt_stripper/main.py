import argparse
import uuid
from typing import List

from flask import Flask, request, abort
from flask_cors import CORS

from mqtt_stripper.config.runnerconfig import RunnerConfig
from mqtt_stripper.network.NetworkMessages import DeviceMessages, MoodMessages
from mqtt_stripper.strips.db.device import Device
from mqtt_stripper.strips.db.modes import ModeOff, ModeSolidColor, Mode
from mqtt_stripper.strips.db.mongo_connector import MongoConnector, MongoDbConfig, AlreadyPresentException
from mqtt_stripper.strips.db.mood import MoodManipulator, Mood
from mqtt_stripper.strips.strip_manager import StripManager

app = Flask(__name__)
CORS(app)

parser = argparse.ArgumentParser()
parser.add_argument("port", help="port the server is running on (http)",
                    type=int)
parser.add_argument("mqtt_ip", help="mqtt server ip", type=str)
parser.add_argument("mqtt_port", help="mqtt server port", type=int)
parser.add_argument("mqtt_username", help="mqtt username", type=str)
parser.add_argument("mqtt_password", help="mqtt password", type=str)
p_args = parser.parse_args()

config = RunnerConfig(p_args.port, p_args.mqtt_ip, p_args.mqtt_port, p_args.mqtt_username, p_args.mqtt_password)

mongo_con = MongoConnector(MongoDbConfig.get_default_config())
try:
    mongo_con.add_device("uuid1", "name", "loc", [1, 2, 3, 4, 5], "in", "out")
except AlreadyPresentException as e:
    print("Device uuid1 already in database...")

try:
    mongo_con.add_device("uuid2", "name2", "loc2", [1, 2, 3], "in2", "out2")
except AlreadyPresentException as e:
    print("Device uuid2 already in database...")

try:
    manis: List[MoodManipulator] = [MoodManipulator("uuid1", ModeOff()),
                                    MoodManipulator("uuid2", ModeSolidColor(123, 321, 111))]
    mongo_con.add_mood("uuid_mood", "Moodname", manis)
except AlreadyPresentException as e:
    print("Mood uuid_mood already in database...")

s_manager = StripManager(mongo_con, config)
s_manager.connect()


# s_manager.set_mood_mode("uuid_mood")


@app.route("/device/list", methods=["GET"])
def get_device_list():
    response = DeviceMessages.get_device_list_msg(mongo_con.get_device_list())
    print(response)
    return response


@app.route("/device/add", methods=["PUT"])
def add_device():
    if request.is_json:
        data: dict = request.get_json(silent=True)
        if data is not None and "device" in data:
            device = Device.from_dict(data.get("device"))
            try:
                mongo_con.add_device(device.uuid, device.name, device.location, device.input_topic, device.output_topic)
                return "", 200
            except AlreadyPresentException:
                print("Device already registered")
    abort(409)


@app.route("/device/<string:d_uuid>/delete", methods=["DELETE"])
def delete_device(d_uuid):
    mongo_con.remove_device(d_uuid)
    return "", 200


@app.route("/mood/list", methods=["GET"])
def get_mood_list():
    return MoodMessages.get_mood_list_msg(mongo_con.get_mood_list())


@app.route("/mood/add", methods=["PUT"])
def add_mood():
    if request.is_json:
        data: dict = request.get_json(silent=True)
        if data is not None and "mood" in data:
            mood = Mood.from_dict(data.get("mood"))
            try:
                m_uuid = uuid.uuid4()
                mongo_con.add_mood(str(m_uuid), mood.name, mood.manipulators)
                return "", 200
            except AlreadyPresentException:
                print("Mood uuid already present")
    abort(409)


@app.route("/mood/<string:m_uuid>/set", methods=["GET"])
def set_mood(m_uuid):
    s_manager.set_mood_mode(m_uuid)
    return "", 200


@app.route("/mood/<string:m_uuid>/delete", methods=["DELETE"])
def delete_mood(m_uuid):
    mongo_con.remove_mood(m_uuid)
    return "", 200


@app.route("/mode/<string:s_uuid>/set", methods=["POST"])
def set_mode(s_uuid):
    if request.is_json:
        data: dict = request.get_json(silent=True)
        if data is not None and "mode" in data:
            mode = Mode.from_dict(data.get("mode"))
            s_manager.set_mode(s_uuid, mode)
            return "", 200
    abort(500)


app.run("0.0.0.0", config.http_port)
