import json


def build_node_register_object(node_name: str, node_ip: str) -> dict:
    return {"name": node_name, "ip": node_ip}
