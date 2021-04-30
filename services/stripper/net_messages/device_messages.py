import json
from typing import List

from stripper.model.strips import ControllableStrip


def get_device_list_message(strips: List[ControllableStrip]) -> str:
    msg = {
        "m_type": "DEVICE_ALL",
        "data": list(map(lambda x: x.to_dict(), strips))
    }
    return json.dumps(msg)
