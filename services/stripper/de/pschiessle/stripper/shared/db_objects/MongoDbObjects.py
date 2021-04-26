class DbNode:
    def __init__(self, node_name: str, node_ip: str):
        self.node_name: str = node_name
        self.node_ip: str = node_ip

    def get_as_db_obj(self):
        return {
            "name": self.node_name,
            "ip": self.node_ip
        }


class DbDevice:
    def __init__(self, device_type: str, device_addr:str, device_name: str, device_location: str):
        self.node_id = None
        self.device_state: int = 0
        self.device_addr = device_addr
        self.device_type: str = device_type
        self.device_name: str = device_name
        self.device_location: str = device_location

    def get_as_db_obj(self):
        return {
            "d_node_id": self.node_id,
            "d_address": self.device_addr,
            "d_type": self.device_type,
            "d_state": self.device_state,
            "d_name": self.device_name,
            "d_location": self.device_location
        }
