from concurrent.futures import Future, ThreadPoolExecutor
import socket
from typing import Optional, List

import requests
from pymongo.collection import Collection
from pymongo.results import InsertOneResult
from requests import Response

from de.pschiessle.stripper.shared.db_objects.MongoDbObjects import DbNode


def do_register_node(node_col: Collection, node_name: str) -> Optional[str]:
    result: InsertOneResult = node_col.insert_one(
        DbNode(node_name, socket.gethostbyname(socket.gethostname())).get_as_db_obj())
    if result.acknowledged:
        return result.inserted_id
    else:
        print("Failed to register node!")
    return None


def get_all_registered_nodes(node_col: Collection) -> List[str]:
    removed_node_ids: List[str] = []

    futures: List[(dict, Future[bool])] = []
    with ThreadPoolExecutor() as executor:
        for doc in node_col.find():
            futures.append((doc, executor.submit(check_if_alive, doc.get("ip"))))
        for doc, future in futures:
            try:
                if future.result() is not True:
                    print("Node " + doc.get("name") + " down!")
                    remove_node(node_col, doc.get("_id"))
                    removed_node_ids.append(str(doc.get("_id")))
            except Exception as expect:
                print(expect)
    return removed_node_ids


def check_if_alive(ip: str) -> bool:
    try:
        rsp: Response = requests.get("http://" + ip + ":1234/ping")
        return rsp.status_code == 200
    except Exception as exc:
        return False


def remove_node(node_col: Collection, node_id:str):
    node_col.delete_one({"_id": node_id})
