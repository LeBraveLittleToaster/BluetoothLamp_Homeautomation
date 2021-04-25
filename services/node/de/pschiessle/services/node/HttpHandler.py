import json
from typing import Optional

import requests as requests

from de.pschiessle.services.node.APIObjects import parse_ping_get


def handle_ping_get() -> str:
    return parse_ping_get()

