class RunnerConfig:
    def __init__(self, port: int):
        self.port = port

    @staticmethod
    def from_dict(data: dict):
        return RunnerConfig(data.get("port", -1))

