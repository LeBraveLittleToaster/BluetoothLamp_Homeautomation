from typing import List

from paho.mqtt.client import basestring

data: List[str] = ["1", "2"]

data_s: str = "hello"

print(type(data))
print(type(data_s))
print("data is array: " + ("Yes" if type(data) is List[str] else "no"))
print("data is str: " + ("Yes" if type(data) is str else "no"))
print("data_s is str:" + ("Yes" if type(data_s) is str else "no"))

print(bool(data) and isinstance(data, list) and all(isinstance(elem, basestring) for elem in data))