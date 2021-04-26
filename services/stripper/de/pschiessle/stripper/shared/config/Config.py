from typing import List

import yaml


class Config:
    def __init__(self, file_path):
        self.node_name: str = None
        self.mongo_ip: str = None
        self.mongo_port: int = None
        self.mongo_uname: str = None
        self.mongo_password: str = None
        self.mongo_db: str = None
        self.mongo_col_nodes: str = None
        self.mongo_col_devices: str = None
        self.load_config(file_path)

    def load_config(self, file_path: str):
        with open(file_path, "r") as stream:
            try:
                config = yaml.safe_load(stream)
                self.node_name = config.get("node_name")
                self.mongo_ip = config.get("mongo_ip")
                self.mongo_port = config.get("mongo_port")
                self.mongo_uname = config.get("mongo_uname")
                self.mongo_password = config.get("mongo_password")
                self.mongo_db = config.get("mongo_db")
                self.mongo_col_nodes = config.get("mongo_col_nodes")
                self.mongo_col_devices = config.get("mongo_col_devices")
            except yaml.YAMLError as exc:
                print(exc)

    def check_config(self) -> [str]:
        missing: List[str] = []
        if self.node_name is None: missing.append("node_name")
        if self.mongo_ip is None: missing.append("mongo_ip")
        if self.mongo_port is None: missing.append("mongo_port")
        if self.mongo_uname is None: missing.append("mongo_uname")
        if self.mongo_password is None: missing.append("mongo_password")
        if self.mongo_db is None: missing.append("mongo_db")
        if self.mongo_col_nodes is None: missing.append("mongo_col_nodes")
        if self.mongo_col_devices is None: missing.append("mongo_col_devices")
        return missing
