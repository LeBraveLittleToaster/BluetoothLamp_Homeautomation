from enum import Enum

from objprint import add_objprint
from typing import List, Optional


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
            return BluetoothConOptions(options["address"])
        elif con_type == ConType.GPIO:
            return GPIOConOptions(options["pin"])
        elif con_type == ConType.MQTT:
            return MqttConOptions(options["address"], options["topic"], options["username"], options["password"])
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

@add_objprint()
class Config:
    def __init__(self, json_config: dict):
        self.version = json_config["version"]
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
    def __init__(self, address: str):
        super().__init__()
        self.address = address


class GPIOConOptions(ConOptions):
    def __init__(self, pin: int):
        super().__init__()
        self.pin = pin


class MqttConOptions(ConOptions):
    def __init__(self, address: str, topic: str, username: str, password: str):
        super().__init__()
        self.address: str = address
        self.topic: str = topic
        self.username: str = username
        self.password: str = password


def parse_strips(json_strips: dict) -> List[ConfigStrip]:
    if "strips" in json_strips and isinstance(json_strips["strips"], list):
        return list(filter(lambda x: x is not None,
                           map(lambda i_x: to_config_strip(i_x[0], i_x[1]), enumerate(json_strips["strips"]))))
    else:
        raise Exception("Failed to parse config!")
