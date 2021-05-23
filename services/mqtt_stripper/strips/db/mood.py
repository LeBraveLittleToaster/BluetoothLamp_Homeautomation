from typing import List


class MoodManipulator:
    def __init__(self, strip_uuid: str, is_on:bool, mode: dict):
        self.strip_uuid = strip_uuid
        self.is_on = is_on
        self.mode:dict = mode

    def to_dict(self):
        return {
            "strip_uuid": self.strip_uuid,
            "is:on" : self.is_on,
            "mode": None if self.mode is None else self.mode
        }

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return str(self.to_dict())

    @staticmethod
    def from_dict(data: dict):
        return MoodManipulator(
            data.get("strip_uuid"),
            data.get("is_on"),
            data.get("mode")
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