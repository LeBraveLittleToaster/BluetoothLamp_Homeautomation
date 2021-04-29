from typing import List

from stripper.config.Config import Config
from stripper.model.strips import ControllableStrip
from stripper.strip_manager_utils import get_strips_as_dict_with_uuids


class StripManager:
    def __init__(self, config: Config):
        self.config = config
        self.strips: dict[str, ControllableStrip] = get_strips_as_dict_with_uuids(config.strips)

    def reload_config(self, config: Config):
        for key, c_strip in self.strips:
            print(c_strip)
        self.config = config
