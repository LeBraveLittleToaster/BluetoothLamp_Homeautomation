from typing import Optional, List

import pymongo
from pymongo import MongoClient, collection, database

from de.pschiessle.stripper.shared.config.Config import Config
from de.pschiessle.stripper.shared.dbcon.MongoNodeHandler import do_register_node, get_all_registered_nodes


class MongoDbCon:
    def __init__(self, config: Config):
        self.node_name = config.node_name
        self.client: MongoClient = pymongo.MongoClient(
            "mongodb://" + config.mongo_ip + ":" + str(config.mongo_port) + "/", username=config.mongo_uname,
            password=config.mongo_password)
        self.db: database = self.client[config.mongo_db]
        self.node_col: collection = self.db[config.mongo_col_nodes]
        self.devices_col: collection = self.db[config.mongo_col_devices]
        self.node_id: Optional[str] = None

    def do_register_node(self) -> bool:
        node_id: Optional[str] = do_register_node(self.node_col, self.node_name)
        if node_id is not None:
            self.node_id = node_id
        return node_id is not None

    def get_all_registered_and_alive_node_ids(self) -> List[str]:
        return get_all_registered_nodes(self.node_col)
