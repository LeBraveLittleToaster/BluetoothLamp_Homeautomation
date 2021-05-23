from typing import List, Optional


class DeviceState:
    def __init__(self, is_on: bool, c_mode: Optional[dict] = None):
        self.is_on = is_on
        self.c_mode: dict = c_mode

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "is_on": self.is_on,
            "c_mode": None if self.c_mode is None else self.c_mode
        }

    @staticmethod
    def from_dict(data: dict):
        return None if data is None else DeviceState(
            data.get("is_on", False),
            data.get("c_mode", None))


class Device:
    def __init__(self, uuid: str, name: str, location: str, supported_modes: List[int], state: DeviceState,
                 input_topic: str,
                 output_topic: str):
        self.uuid = uuid
        self.name = name
        self.location = location
        self.supported_modes = supported_modes
        self.state = state
        self.input_topic = input_topic
        self.output_topic = output_topic

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "uuid": self.uuid,
            "name": self.name,
            "location": self.location,
            "supported_modes": self.supported_modes,
            "state": None if self.state is None else self.state.to_dict(),
            "input_topic": self.input_topic,
            "output_topic": self.output_topic
        }

    @staticmethod
    def from_dict(data: dict):
        return Device(data.get("uuid"), data.get("name"), data.get("location"), data.get("supported_modes"),
                      DeviceState.from_dict(data.get("state")), data.get("input_topic"), data.get("output_topic"))
