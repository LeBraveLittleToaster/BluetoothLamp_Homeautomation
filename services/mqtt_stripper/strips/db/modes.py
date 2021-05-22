import abc
from typing import Optional

from mqtt_stripper.strips.db.modes_impl import ModeSolidColor, ModeSingleColorPulse


class Mode:

    def __init__(self, mode_id: int):
        self.mode_id = mode_id

    @abc.abstractmethod
    def to_dict(self):
        pass

    @abc.abstractmethod
    def to_mqtt_dict(self):
        pass

    @staticmethod
    def from_dict(data: dict):
        return None if data is None else get_mode(data)

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return str(self.to_dict())



def get_mode(mode_options: dict) -> Optional[Mode]:
    try:
        mode_id = mode_options.get("mode_id")
        if mode_id == 1:
            return ModeSolidColor(mode_options.get("h"), mode_options.get("s"),
                                  mode_options.get("v"), mode_options.get("brightness"))
        elif mode_id == 2:
            return ModeSingleColorPulse(mode_options.get("h"), mode_options.get("s"),
                                        mode_options.get("v"),
                                        mode_options.get("brightness_start"),
                                        mode_options.get("brightness_end"),
                                        mode_options.get("speed"))
    except KeyError as e:
        print("Malformed Json")
        print(str(e))
    return None
