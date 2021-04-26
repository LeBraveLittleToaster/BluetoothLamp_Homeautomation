from flask import jsonify


class PingResponse:
    def __init__(self, state: str):
        self.state: str = state

    def get_as_json_str(self):
        return jsonify({"state": self.state})

