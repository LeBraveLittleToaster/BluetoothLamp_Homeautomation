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


class ColorParam:
    def __init__(self, color_param_type: ColorParamType, label:str, json_key: str, param_type: ParamType):
        self.color_param_type = color_param_type
        self.label = label
        self.json_key = json_key
        self.param_type = param_type

    def to_dict(self):
        return None if self is None else {
            "color_param_type": str(self.color_param_type.name),
            "label" : self.label,
            "json_key": self.json_key,
            "param_type": str(self.param_type.name)
        }

    @staticmethod
    def from_dict(source: dict):
        return None if source is None else ColorParam(
            ColorParamType[source.get("color_param_type")],
            source.get("label"),
            source.get("json_key"),
            ParamType[source.get("param_type")]
        )


class ModeParam:
    def __init__(self, mode_param_type: ModeParamType, label:str, json_key: str, param_type: ParamType):
        self.mode_param_type = mode_param_type
        self.label = label
        self.json_key = json_key
        self.param_type = param_type

    def to_dict(self):
        return None if self is None else {
            "mode_param_type": str(self.mode_param_type.name),
            "label" : self.label,
            "json_key": self.json_key,
            "param_type": str(self.param_type.name)
        }

    @staticmethod
    def from_dict(source: dict):
        return None if source is None else ModeParam(
            ModeParamType[source.get("mode_param_type")],
            source.get("label"),
            source.get("json_key"),
            ParamType[source.get("param_type")]
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


class ModeTemplateValidator:

    @staticmethod
    def validate_with_template(data: dict, template: ModeTemplate) -> bool:
        if data is None or template is None:
            return False
        try:
            color_params_check: List[bool] = list(
                map(ModeTemplateValidator.validate_color_param, data.get("color_params")))
            mode_params_check: List[bool] = list(
                map(ModeTemplateValidator.validate_mode_param, data.get("mode_params")))
            return False if color_params_check.count(False) > 0 or mode_params_check.count(False) > 0 else True
        except KeyError:
            print("Color or mode params missing")
            return False

    @staticmethod
    def validate_color_param(data: dict, color_param_template: ColorParam) -> bool:
        try:
            param_value = data.get(color_param_template.json_key)
            if color_param_template.param_type == ParamType.SINGLE_VALUE:
                return isinstance(param_value, str)
            elif color_param_template.param_type == ParamType.ARRAY:
                return ModeTemplateValidator.is_list_of_str(param_value)
        except KeyError:
            return False

    @staticmethod
    def validate_mode_param(data: dict, mode_param_template: ModeParam) -> bool:
        try:
            param_value = data.get(mode_param_template.json_key)
            if mode_param_template.param_type == ParamType.SINGLE_VALUE:
                return isinstance(param_value, str)
            elif mode_param_template.param_type == ParamType.ARRAY:
                return ModeTemplateValidator.is_list_of_str(param_value)
        except KeyError:
            return False

    @staticmethod
    def is_list_of_str(param_value) -> bool:
        return bool(param_value) and isinstance(param_value, list) and all(
            isinstance(elem, str) for elem in param_value)
