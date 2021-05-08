from typing import List

from mqtt_stripper.strips.db.modes import Mode


class MoodManipulator:
    def __init__(self, strip_uuid: str, mode: Mode):
        self.strip_uuid = strip_uuid
        self.mode = mode

    def to_dict(self):
        return {
            "strip_uuid": self.strip_uuid,
            "mode": self.mode.to_dict()
        }

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return str(self.to_dict())

    @staticmethod
    def from_dict(data: dict):
        return MoodManipulator(
            data.get("strip_uuid"),
            Mode.from_dict(data.get("mode"))
        )


class Mood:
    def __init__(self, uuid: str, name: str, manipulators: List[MoodManipulator]):
        self.uuid = uuid
        self.name = name
        self.manipulators = manipulators

    def to_dict(self):
        return {
            "uuid": self.uuid,
            "name": self.name,
            "manipulators": list(map(lambda x: x.to_dict(), self.manipulators))
        }

    @staticmethod
    def from_dict(data: dict):
        return Mood(
            data.get("uuid"),
            data.get("name"),
            list(map(lambda x: MoodManipulator.from_dict(x), data.get("manipulators")))
        )

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return str(self.to_dict())