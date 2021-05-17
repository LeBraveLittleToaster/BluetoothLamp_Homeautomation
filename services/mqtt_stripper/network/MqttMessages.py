import abc
import json
from enum import Enum

from mqtt_stripper.strips.db.modes import Mode


class MqttMsgType(Enum):
    MODE = 1
    ON_OFF = 2


class MqttMessage:
    def __init__(self, m_type: MqttMsgType):
        self.m_type = m_type

    def to_json(self):
        return json.dumps(self.to_dict())

    @abc.abstractmethod
    def to_dict(self):
        pass

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return str(self.to_dict())


class MqttOnOffMessage(MqttMessage):
    def __init__(self, is_on: bool):
        super().__init__(MqttMsgType.ON_OFF)
        self.is_on = is_on

    def to_dict(self):
        return {
            "type": str(self.m_type),
            "data": {
                "is_on": self.is_on
            }
        }


class MqttModeMessage(MqttMessage):
    def __init__(self, mode: Mode):
        super().__init__(MqttMsgType.MODE)
        self.mode = mode

    def to_dict(self):
        return {
            "type": str(self.m_type),
            "data": {
                "mode": self.mode.to_mqtt_dict()
            }
        }
