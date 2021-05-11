import json
from typing import List, Optional

from mqtt_stripper.strips.db.device import Device
from mqtt_stripper.strips.db.mood import Mood


class DeviceMessages:
    @staticmethod
    def get_device_list_msg(devices: List[Device]) -> str:
        return json.dumps({
            "devices": list(map(lambda x: x.to_dict(), devices))
        })

    @staticmethod
    def get_device_msg(device: Device):
        return json.dumps({
            "device": device.to_dict()
        })

    @staticmethod
    def get_device_add_msg(uuid: str):
        return json.dumps({
            "uuid": uuid
        })


class MoodMessages:
    @staticmethod
    def get_mood_list_msg(moods: List[Mood]):
        return json.dumps({
            "moods": list(map(lambda x: x.to_dict(), moods))
        })

    @staticmethod
    def get_mood_msg(mood: Mood):
        return json.dumps({
            "mood": mood.to_dict()
        })
