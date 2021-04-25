from threading import Thread
from typing import List

import flask

from flask import jsonify

from de.pschiessle.services.distributer.MongoDbCon import MongoDbCon
from de.pschiessle.services.distributer.api.APIObjs import parse_ping_get, parse_node_ping_all_get


def handle_node_ping_all_get(db_handler: MongoDbCon) -> str:
    removed_node_ids: List[str] = db_handler.get_all_registered_nodes()
    return parse_node_ping_all_get(removed_node_ids)
