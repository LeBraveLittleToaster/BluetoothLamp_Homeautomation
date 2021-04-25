from concurrent.futures import Future, ThreadPoolExecutor
from typing import Optional, Dict, List, Any

import pymongo
import requests
from pymongo import MongoClient, collection, database
from requests import Response
from urllib3.exceptions import MaxRetryError

from de.pschiessle.services.distributer.Config import Config


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

    @staticmethod
    def check_if_alive(ip: str) -> bool:
        try:
            rsp: Response = requests.get("http://" + ip + ":1234/ping")
            return rsp.status_code == 200
        except Exception as exc:
            return False

    def remove_node(self, node_id):
        self.node_col.delete_one({"_id": node_id})

    def get_all_registered_nodes(self) -> List[str]:
        removed_node_ids: List[str] = []

        futures: List[(dict, Future[bool])] = []
        with ThreadPoolExecutor() as executer:
            for doc in self.node_col.find():
                futures.append((doc, executer.submit(self.check_if_alive, doc.get("ip"))))
            for doc, future in futures:
                try:
                    if future.result() is not True:
                        print("Node " + doc.get("name") + " down!")
                        self.remove_node(doc.get("_id"))
                        removed_node_ids.append(str(doc.get("_id")))
                except Exception as expc:
                    print(expc)
        return removed_node_ids
