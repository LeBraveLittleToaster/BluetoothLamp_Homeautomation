from typing import List

from stripper.config.Config import Config
from stripper.model.strips import ControllableStrip
from stripper.managers.strip_manager_utils import convert_config_to_controllable_strips


class StripManager:
    def __init__(self, config: Config):
        self.config = config
        self.strips: List[ControllableStrip] = convert_config_to_controllable_strips(config.strips)

    def print(self):
        print("+++++++++++++")
        print("DEVICE_TYPES:")
        for strip in self.strips:
            print(strip)
        print("+++++++++++++")

    def reconnect_all(self):
        for strip in self.strips:
            strip.reconnect()

    def connect_all(self):
        for strip in self.strips:
            strip.connect()

    def reload_config(self, config: Config):
        for key, c_strip in self.strips:
            print(c_strip)
        self.config = config

    def set_mood_mode(self, mode):
        for strip in self.strips:
            strip.set_mode(mode)
