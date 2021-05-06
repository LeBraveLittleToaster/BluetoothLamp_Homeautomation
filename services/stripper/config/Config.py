from enum import Enum

from objprint import add_objprint
from typing import List, Optional

from stripper.model.modes import get_mode, Mode


class ConType(Enum):
    BLUETOOTH = 0
    MQTT = 1
    GPIO = 2


def auto_str(cls):
    def __str__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )

    cls.__str__ = __str__
    return cls


class ConOptions:
    def __init__(self):
        pass


def parse_options_by_type(con_type: ConType, options: dict) -> Optional[ConOptions]:
    try:
        if con_type == ConType.BLUETOOTH:
            return BluetoothConOptions(options["address"], options["port"])
        elif con_type == ConType.GPIO:
            return GpioConOptions(options["pin"])
        elif con_type == ConType.MQTT:
            return MqttConOptions(options["address"], options["port"], options["topic"], options["username"],
                                  options["password"])
    except KeyError:
        pass
    return None


def to_config_strip(strip_id: int, json_strip: dict):
    try:
        con_type = ConType[json_strip["con_type"]]
        options = parse_options_by_type(con_type, json_strip["options"])
        return None if options is None else ConfigStrip(json_strip["name"], json_strip["location"], strip_id, con_type,
                                                        options)
    except KeyError:
        return None


class ConfigMood:
    def __init__(self, name: str, mode: Mode):
        self.name = name
        self.mode = mode

    def to_dict(self):
        return {
            "name": self.name,
            "mode": self.mode.to_dict()
        }


def to_config_mood(json_config) -> Optional[ConfigMood]:
    try:
        name = json_config.get("name")
        mode = get_mode(json_config.get("mode"))
        return None if name is None or mode is None else ConfigMood(name, mode)
    except KeyError:
        print("Parse error on mode!")
        return None


def parse_moods(json_config) -> Optional[List[ConfigMood]]:
    try:
        moods = json_config["moods"]
        config_moods: List[ConfigMood] = list(map(lambda e: to_config_mood(e), moods))
        return [] if config_moods is None else config_moods
    except KeyError:
        return None


@add_objprint()
class Config:
    def __init__(self, json_config: dict):
        self.version = json_config["version"]
        self.moods: List[ConfigMood] = parse_moods(json_config)
        self.strips: List[ConfigStrip] = parse_strips(json_config)


@add_objprint()
@auto_str
class ConfigStrip:
    def __init__(self, name: str, location: str, strip_id: int, con_type: ConType, options: ConOptions):
        self.name: str = name
        self.location: str = location
        self.strip_id: int = strip_id
        self.con_type: ConType = con_type
        self.options: ConOptions = options


class BluetoothConOptions(ConOptions):
    def __init__(self, address: str, port: int):
        super().__init__()
        self.address: str = address
        self.port: int = port


class GpioConOptions(ConOptions):
    def __init__(self, pin: int):
        super().__init__()
        self.pin = pin


class MqttConOptions(ConOptions):
    def __init__(self, url: str, port: int, topic: str, username: str, password: str):
        super().__init__()
        self.url: str = url
        self.port = port
        self.topic: str = topic
        self.username: str = username
        self.password: str = password


def parse_strips(json_strips: dict) -> List[ConfigStrip]:
    if "strips" in json_strips and isinstance(json_strips["strips"], list):
        return list(filter(lambda x: x is not None,
                           map(lambda i_x: to_config_strip(i_x[0], i_x[1]), enumerate(json_strips["strips"]))))
    else:
        raise Exception("Failed to parse config!")
