from typing import List, Optional, Mapping, Dict

from utils.Config import Config, Strip


class StripValue:

    def __init__(self, strip_id: int, hue=0, brightness=0, speed=0):
        self.hue = hue
        self.brightness = brightness
        self.speed = speed
        self.strip_id = strip_id

    def update_all_values(self, hue: int, brightness: int, speed: int):
        self.hue = hue
        self.brightness = brightness
        self.speed = speed


class StripManager:
    def __init__(self, strips: List[Strip], strip_values=None):
        self.strips: List[Strip] = strips
        self.selected_id: Optional[int] = None
        self.strip_values: Dict[int, StripValue] = strip_values \
            if strip_values is not None \
            else self.generate_empty_values(self.strips)

    def select_id(self, strip_id: int) -> None:
        self.selected_id = strip_id

    def set_strip_value(self, strip_id: int, hue: int, brightness: int, speed: int):
        strip_value = self.strip_values.get(strip_id, StripValue(strip_id))
        strip_value.update_all_values(hue, brightness, speed)

    def get_or_add_strip_value_by_id(self, strip_id: int) -> StripValue:
        strip_value: Optional[StripValue] = self.strip_values.get(strip_id, None)
        if strip_value is None:
            strip_value = StripValue(strip_id)
            self.strip_values[strip_id] = strip_value
        return strip_value

    def get_strip_by_id(self, strip_id: int) -> Optional[Strip]:
        for strip in self.strips:
            if strip.strip_id == strip_id:
                return strip
        return None

    @staticmethod
    def generate_empty_values(strips: List[Strip]):
        values: Dict[int, StripValue] = dict()
        for strip in strips:
            values[strip.strip_id] = StripValue(strip.strip_id)
        return values
