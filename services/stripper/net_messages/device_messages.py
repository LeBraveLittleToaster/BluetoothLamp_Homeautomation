import json
from typing import List

from stripper.config.Config import ConfigMood
from stripper.model.strips import ControllableStrip


def get_device_list_message(strips: List[ControllableStrip]) -> str:
    strips = list(map(lambda x: x.to_dict(), strips))
    strips_out = []
    for i in range(0, 3):
        for s in strips:
            strips_out.append(s)
    msg = {
        "m_type": "DEVICE_ALL",
        "data": strips_out,
    }
    return json.dumps(msg)


def get_moods_list_message(moods: List[ConfigMood]) -> str:
    moods = list(map(lambda x: x.to_dict(), moods))
    moods_out = []
    for i in range(0, 1):
        for s in moods:
            moods_out.append(s)
    msg = {
        "m_type": "MOODS_ALL",
        "data": moods_out,
    }
    return json.dumps(msg)
