from typing import List

from de.pschiessle.stripper.distributor.api.DistApiJsonObjs import PingAllResponse
from de.pschiessle.stripper.shared.dbcon.MongoDbCon import MongoDbCon


def handle_node_ping_all_get(db_handler: MongoDbCon) -> PingAllResponse:
    removed_node_ids: List[str] = db_handler.get_all_registered_and_alive_node_ids()
    return PingAllResponse(removed_node_ids)
