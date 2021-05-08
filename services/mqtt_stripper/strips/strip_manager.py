from typing import List

from mqtt_stripper.strips.db.device import Device
from mqtt_stripper.strips.db.modes import Mode
from mqtt_stripper.strips.db.mongo_connector import MongoConnector
from stripper.config.Config import Config
from stripper.model.strips import ControllableStrip
from stripper.managers.strip_manager_utils import convert_config_to_controllable_strips


class StripManager:
    def __init__(self, mongo_con: MongoConnector):
        self.mongo_con: MongoConnector = mongo_con

    def print(self):
        print("+++++++++++++")
        print("DEVICE_TYPES:")
        for e in self.mongo_con.get_device_list():
            print(e)
        print("+++++++++++++")
        print("+++++++++++++")
        print("Mood_TYPES:")
        for e in self.mongo_con.get_mood_list():
            print(e)
        print("+++++++++++++")

    def set_mood_mode(self, mood_uuid: str):
        mood = self.mongo_con.get_mood(mood_uuid)
        if mood is not None:
            devices: List[Device] = self.mongo_con.get_devices_in_id_list(
                list(map(lambda x: x.strip_uuid, mood.manipulators))
            )
            print(devices)

    def set_mode(self, strip_uuid: str, mode: Mode):
        print("Setting strip: " + strip_uuid + " to mode: " + str(mode))
