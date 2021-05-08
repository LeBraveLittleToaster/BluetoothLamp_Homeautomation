from typing import List, Optional, Any

from pymongo import MongoClient

from mqtt_stripper.strips.db.device import Device
from mqtt_stripper.strips.db.mood import MoodManipulator, Mood


class MongoDbConfig:
    def __init__(self, ip: str, port: int, db_name: str, device_col_name: str, mood_col_name: str):
        self.ip = ip
        self.db_name = db_name
        self.port = port
        self.device_col_name = device_col_name
        self.mood_col_name = mood_col_name

    @staticmethod
    def get_default_config():
        return MongoDbConfig("localhost", 27017, "stripper", "devices", "moods")


class MongoConnector:
    def __init__(self, db_conf: MongoDbConfig):
        self.db_conf: MongoDbConfig = db_conf
        self.client: MongoClient = MongoClient(db_conf.ip, db_conf.port)
        self.device_col = self.client.get_database(db_conf.db_name).get_collection(db_conf.device_col_name)
        self.mood_col = self.client.get_database(db_conf.db_name).get_collection(db_conf.mood_col_name)

    def get_device_list(self) -> List[Device]:
        return list(map(lambda x: Device.from_dict(x), list(self.device_col.find())))

    def add_device(self, uuid: str, name: str, location: str, input_topic: str, output_topic: str):
        if self.device_col.count({"uuid": uuid}) == 0:
            self.device_col.insert_one(Device(
                uuid, name, location, input_topic, output_topic
            ).to_dict())
        else:
            raise AlreadyPresentException()

    def get_device(self, uuid: str) -> Optional[Device]:
        doc: Optional[Any] = self.device_col.find_one({"uuid": uuid})
        return None if doc is None else Device.from_dict(doc)

    def get_devices_in_id_list(self, id_list: List[str]) -> [Device]:
        return list(map(lambda x: Device.from_dict(x), list(self.device_col.find({'uuid': {'$in': id_list}}))))

    def remove_device(self, d_uuid):
        self.device_col.delete_many({"uuid": d_uuid})

    def add_mood(self, uuid: str, name: str, manipulators: List[MoodManipulator]):
        if self.mood_col.count({"uuid": uuid}) == 0:
            self.mood_col.insert_one(Mood(uuid, name, manipulators).to_dict())
        else:
            raise AlreadyPresentException()

    def get_mood_list(self) -> List[Mood]:
        return list(map(lambda x: Mood.from_dict(x), list(self.mood_col.find())))

    def get_mood(self, uuid: str) -> Optional[Mood]:
        doc: Optional[Any] = self.mood_col.find_one({"uuid": uuid})
        return None if doc is None else Mood.from_dict(doc)

    def remove_mood(self, m_uuid):
        self.mood_col.delete_many({"uuid": m_uuid})


class AlreadyPresentException(Exception):
    pass
