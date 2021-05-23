from enum import Enum
from typing import List


class ParamType(Enum):
    ARRAY = 1
    SINGLE_VALUE = 2


class ColorParamType(Enum):
    HSV_B = 1


class ModeParamType(Enum):
    SINGLE_VALUE = 1
    RANGE_VALUE = 2
    SINGLE_SELECT = 3
    MULTI_SELECT = 4


class ColorParam:
    def __init__(self, color_param_type: ColorParamType, json_key: str, param_type: ParamType):
        self.color_param_type = color_param_type
        self.json_key = json_key
        self.param_type = param_type

    def to_dict(self):
        return None if self is None else {
            "color_param_type": self.color_param_type,
            "json_key": self.json_key,
            "param_type": self.param_type
        }

    @staticmethod
    def from_dict(source: dict):
        return None if source is None else ColorParam(
            ColorParamType[source.get("color_param_type")],
            source.get("json_key"),
            source.get("param_type")
        )


class ModeParam:
    def __init__(self, mode_param_type: ModeParamType, json_key: str, param_type: ParamType):
        self.mode_param_type = mode_param_type
        self.json_key = json_key
        self.param_type = param_type

    def to_dict(self):
        return None if self is None else {
            "mode_param_type": self.param_type,
            "json_key": self.json_key,
            "param_type": self.param_type
        }

    @staticmethod
    def from_dict(source: dict):
        return None if source is None else ModeParam(
            ModeParamType[source.get("mode_param_type")],
            source.get("json_key"),
            source.get("param_type")
        )


class ModeTemplate:
    def __init__(self, mode_id: int, color_params: List[ColorParam], mode_params: List[ModeParam]):
        self.mode_id = mode_id
        self.color_params: List[ColorParam] = color_params
        self.mode_params: List[ModeParam] = mode_params

    def to_dict(self):
        return None if self is None else {
            "mode_id": self.mode_id,
            "color_params": list(map(lambda x: x.to_dict(), self.color_params)),
            "mode_params": list(map(lambda x: x.to_dict(), self.mode_params))
        }

    @staticmethod
    def from_dict(source: dict):
        return None if source is None else ModeTemplate(
            source.get("mode_id"),
            list(map(ColorParam.from_dict, source.get("color_params"))),
            list(map(ModeParam.from_dict, source.get("mode_params")))
        )
