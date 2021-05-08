from typing import List, Optional

from mqtt_stripper.strips.db.device import Device
from mqtt_stripper.strips.db.mood import Mood


class DeviceMessages:
    @staticmethod
    def get_device_list_msg(devices: List[Device]) -> str:
        return str({
            "devices": list(map(lambda x: x.to_dict(), devices))
        })

    @staticmethod
    def get_device_msg(device: Device):
        return str({
            "device": device.to_dict()
        })

    @staticmethod
    def get_device_add_msg(uuid:str):
        return str({
            "uuid" : uuid
        })


class MoodMessages:
    @staticmethod
    def get_mood_list_msg(moods: List[Mood]):
        return str({
            "moods": list(map(lambda x: x.to_dict(), moods))
        })

    @staticmethod
    def get_mood_msg(mood: Mood):
        return str({
            "mood": mood.to_dict()
        })
