import argparse
import logging as log
import uuid
from typing import List

from flask import Flask, request, abort
from flask_cors import CORS

from mqtt_stripper.config.runnerconfig import RunnerConfig
from mqtt_stripper.network.NetworkMessages import DeviceMessages, MoodMessages
from mqtt_stripper.strips.db.device import Device
from mqtt_stripper.strips.db.modes import ModeSolidColor, Mode
from mqtt_stripper.strips.db.mongo_connector import MongoConnector, MongoDbConfig, AlreadyPresentException
from mqtt_stripper.strips.db.mood import MoodManipulator
from mqtt_stripper.strips.strip_manager import DeviceManager

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

log.info("Creating default objects for testing...")
try:
    mongo_con.add_device("uuid1", "name", "loc", [1, 2, 3, 4, 5], "in", "out")
except AlreadyPresentException as e:
    log.warning("Device uuid1 already in database...")

try:
    mongo_con.add_device("uuid2", "name2", "loc2", [1, 2, 3], "in2", "out2")
except AlreadyPresentException as e:
    log.warning("Device uuid2 already in database...")

try:
    manis: List[MoodManipulator] = [MoodManipulator("uuid1", True, ModeSolidColor(1, 2, 3, 123)),
                                    MoodManipulator("uuid2", True, ModeSolidColor(123, 321, 111, 255))]
    mongo_con.add_mood("uuid_mood", "Moodname", manis)
except AlreadyPresentException as e:
    log.warning("Mood uuid_mood already in database...")

try:
    manis: List[MoodManipulator] = [MoodManipulator("uuid1", True, ModeSolidColor(3, 2, 1, 111)),
                                    MoodManipulator("uuid2", True, ModeSolidColor(123, 321, 111, 255))]
    mongo_con.add_mood("uuid_mood2", "Moodname2", manis)
except AlreadyPresentException as e:
    log.warning("Mood uuid_mood2 already in database...")

s_manager = DeviceManager(mongo_con, config)
s_manager.connect()


@app.route("/device/list", methods=["GET"])
def get_device_list():
    return DeviceMessages.get_device_list_msg(mongo_con.get_device_list())


@app.route("/device/add", methods=["PUT"])
def add_device():
    if request.is_json:
        data: dict = request.get_json(silent=True)
        if data is not None and "device" in data:
            device = Device.from_dict(data.get("device"))
            try:
                mongo_con.add_device(device.uuid, device.name, device.location, device.supported_modes,
                                     device.input_topic, device.output_topic)
                return "", 200
            except AlreadyPresentException:
                print("Device already registered")
    abort(409)


@app.route("/device/<string:d_uuid>/state/set$is_on=<string:s_is_on>", methods=["PUT"])
def set_device_is_on(d_uuid, s_is_on: str):
    if s_is_on.lower() in ['true', 'false']:
        s_manager.set_is_on(d_uuid, s_is_on.lower() == 'true')
        return "", 200
    else:
        return "", 507


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
        try:
            mood_name: str = data.get("mood").get("name")
            mood_device_uuids: List[str] = data.get("mood").get("device_uuids")
            device_from_db: List[Device] = mongo_con.get_devices_in_id_list(mood_device_uuids)
            mood_uuid = str(uuid.uuid4())
            manipulators = list(map(lambda d: MoodManipulator(d.uuid, d.state.is_on, d.state.c_mode), device_from_db))
            mongo_con.add_mood(mood_uuid, mood_name, manipulators)
            return "", 200
        except KeyError:
            print("JSON key missing")
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
        else:
            print("No json field mode found...")
    else:
        print("Body is no json...aborting...")
    abort(500)


app.run("0.0.0.0", config.http_port)
