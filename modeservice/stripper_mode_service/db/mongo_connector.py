from typing import List
from pymongo import MongoClient

from stripper_mode_service.db.ModeTemplate import ModeParam, ColorParam, ModeTemplate


class MongoDbConfig:
    def __init__(self, ip: str, port: int, db_name: str, mode_col_name: str):
        self.ip = ip
        self.db_name = db_name
        self.port = port
        self.mode_col_name = mode_col_name

    @staticmethod
    def get_default_config():
        return MongoDbConfig("localhost", 27017, "stripper-modes", "modes")


class MongoConnector:
    def __init__(self, db_conf: MongoDbConfig):
        self.db_conf: MongoDbConfig = db_conf
        self.client: MongoClient = MongoClient(db_conf.ip, db_conf.port)
        self.mode_col = self.client.get_database(db_conf.db_name).get_collection(db_conf.mode_col_name)

    def add_or_overwrite_mode_template(self, mode_id: int, color_params: List[ColorParam], mode_param: List[ModeParam]):
        self.mode_col.update_one({"mode_id": mode_id}, ModeTemplate(mode_id, color_params, mode_param).to_dict(),
                                 upsert=True)

    def delete_mode_template_by_mod_id(self, mode_id: int):
        self.mode_col.delete_one({"mode_id": mode_id})


class AlreadyPresentException(Exception):
    pass
