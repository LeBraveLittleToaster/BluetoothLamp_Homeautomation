from typing import Optional

import pymongo
from pymongo import MongoClient, collection, database
import socket

from pymongo.results import InsertOneResult

from de.pschiessle.services.node.Config import Config
from de.pschiessle.services.node.MongoDbObjects import build_node_register_object


class MongoDbCon:
    def __init__(self, config: Config):
        self.node_name = config.node_name
        self.client: MongoClient = pymongo.MongoClient(
            "mongodb://" + config.mongo_ip + ":" + str(config.mongo_port) + "/", username=config.mongo_uname,
            password=config.mongo_password)
        self.db: database = self.client[config.mongo_db]
        self.node_col: collection = self.db[config.mongo_col_nodes]
        self.devices_col: collection = self.db[config.mongo_col_devices]
        self.id: Optional[str] = None

    def do_register_node(self) -> bool:
        result: InsertOneResult = self.node_col.insert_one(
            build_node_register_object(self.node_name, socket.gethostbyname(socket.gethostname())))
        if result.acknowledged:
            self.id = result.inserted_id
        else:
            print("Failed to register node!")
        return result.acknowledged
