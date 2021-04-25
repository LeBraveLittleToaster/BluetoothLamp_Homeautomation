from typing import List

from flask import jsonify


def parse_ping_get():
    return jsonify({"state": "RUNNING"})


def parse_node_ping_all_get(removed_node_ids: List[str]):
    return jsonify({"removed_nodes": removed_node_ids})
