from enum import Enum

from typing import List


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


def parse_options_by_type(con_type: ConType, options: dict):
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


def to_strip(strip_id: int, json_strip: dict):
    try:
        con_type = ConType[json_strip["con_type"]]
        options = parse_options_by_type(con_type, json_strip["options"])
        return None if options is None else ConfigStrip(json_strip["name"], strip_id, con_type, options)
    except KeyError:
        return None


class Config:
    def __init__(self, json_config: dict):
        self.strips: List[ConfigStrip] = parse_strips(json_config)


class ConOptions:
    def __init__(self):
        pass


@auto_str
class ConfigStrip:
    def __init__(self, name: str, strip_id: int, con_type: ConType, options: ConOptions):
        self.name = name
        self.strip_id = strip_id
        self.con_type = con_type
        self.options = options


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
        self.address = address
        self.topic = topic
        self.username = username
        self.password = password


def parse_strips(json_strips: dict) -> List[ConfigStrip]:
    if "strips" in json_strips and isinstance(json_strips["strips"], list):
        return list(filter(lambda x: x is not None,
                           map(lambda i_x: to_strip(i_x[0], i_x[1]), enumerate(json_strips["strips"]))))
    else:
        raise Exception("Failed to parse config!")
