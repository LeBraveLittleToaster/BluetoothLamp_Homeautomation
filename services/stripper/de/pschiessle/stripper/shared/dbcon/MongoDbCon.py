from typing import Optional, List

import pymongo
from pymongo import MongoClient, collection, database
from pymongo.results import InsertManyResult

from de.pschiessle.stripper.shared.config.Config import NodeConfig, DeviceConfig
from de.pschiessle.stripper.shared.dbcon.MongoNodeHandler import do_register_node, get_all_registered_nodes


class MongoDbCon:
    def __init__(self, config: NodeConfig):
        self.node_name = config.node_name
        self.client: MongoClient = pymongo.MongoClient(
            "mongodb://" + config.mongo_ip + ":" + str(config.mongo_port) + "/", username=config.mongo_uname,
            password=config.mongo_password)
        self.db: database = self.client[config.mongo_db]
        self.node_col: collection = self.db[config.mongo_col_nodes]
        self.devices_col: collection = self.db[config.mongo_col_devices]
        self.node_id: Optional[str] = None
        self.node_port = config.node_port

    def do_register_node(self) -> bool:
        node_id: Optional[str] = do_register_node(self.node_col, self.node_name, self.node_port)
        if node_id is not None:
            self.node_id = node_id
        return node_id is not None

    def get_all_registered_and_alive_node_ids(self) -> List[str]:
        return get_all_registered_nodes(self.node_col)

    def do_register_devices(self, device_conf: DeviceConfig) -> Optional[List[str]]:
        for device in device_conf.devices:
            device.node_id = str(self.node_id)
        result: InsertManyResult = self.devices_col.insert_many(
            list(map(lambda d: d.get_as_db_obj(), device_conf.devices)))
        if result.acknowledged:
            return result.inserted_ids
        return None
