from typing import List
from flask import jsonify


class PingAllResponse:
    def __init__(self, removed_node_ids: List[str]):
        self.removed_node_ids = removed_node_ids

    def get_as_json_str(self):
        return jsonify({"removed_nodes": self.removed_node_ids})
