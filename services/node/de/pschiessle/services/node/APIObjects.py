from flask import jsonify


def parse_ping_get():
    return jsonify({"state": "RUNNING"})
