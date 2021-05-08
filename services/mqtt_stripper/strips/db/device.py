class Device:
    def __init__(self, uuid: str, name: str, location: str, input_topic: str, output_topic: str):
        self.uuid = uuid
        self.name = name
        self.location = location
        self.input_topic = input_topic
        self.output_topic = output_topic

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "uuid": self.uuid,
            "name": self.name,
            "location": self.location,
            "input_topic": self.input_topic,
            "output_topic": self.output_topic
        }

    @staticmethod
    def from_dict(data: dict):
        return Device(data.get("uuid"), data.get("name"), data.get("location"), data.get("input_topic"),
                      data.get("output_topic"))
