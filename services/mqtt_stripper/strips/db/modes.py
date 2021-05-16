import abc
from typing import Optional


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


class ModeOff(Mode):

    def __init__(self):
        super().__init__(0)

    def to_dict(self):
        return {
            "mode_id": self.mode_id
        }

    def to_mqtt_dict(self):
        return self.to_dict();


class ModeSolidColor(Mode):

    def __init__(self, h, s, v, brightness):
        super().__init__(1)
        self.h = h
        self.s = s
        self.v = v
        self.brightness = brightness

    def to_dict(self):
        return {"mode_id": self.mode_id, "h": self.h, "s": self.s, "v": self.v, "brightness": self.brightness}

    def to_mqtt_dict(self):
        return {"mode_id": self.mode_id,
                "color": {"h": self.h, "s": self.s, "v": self.v, "brightness": self.brightness}, "options": {}}


class ModeSingleColorPulse(Mode):

    def __init__(self, h, s, v, brightness_start, brightness_end, speed):
        super().__init__(2)
        self.h = h
        self.s = s
        self.v = v
        self.brightness = brightness_start
        self.brightness_start = brightness_start
        self.brightness_end = brightness_end
        self.speed = speed

    def to_dict(self):
        return {"mode_id": self.mode_id, "h": self.h, "s": self.s, "v": self.v, "brightness": self.brightness_start,
                "brightness_start": self.brightness_start, "brightness_end": self.brightness_end, "speed": self.speed
                }

    def to_mqtt_dict(self):
        return {"mode_id": self.mode_id, "h": self.h, "s": self.s, "v": self.v, "brightness": self.brightness_start,
                "options": {
                    "brightness_start": self.brightness_start,
                    "brightness_end": self.brightness_end,
                    "speed": self.speed
                }}


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
