class RunnerConfig:
    def __init__(self, http_port: int, mqtt_ip: str, mqtt_port: int, mqtt_username: str, mqtt_password: str):
        self.http_port = http_port
        self.mqtt_ip = mqtt_ip
        self.mqtt_port = mqtt_port
        self.mqtt_username = mqtt_username
        self.mqtt_password = mqtt_password

    @staticmethod
    def from_dict(data: dict):
        return RunnerConfig(
            data.get("port"),
            data.get("mqtt_ip"),
            data.get("mqtt_port"),
            data.get("mqtt_username"),
            data.get("mqtt_password"))
