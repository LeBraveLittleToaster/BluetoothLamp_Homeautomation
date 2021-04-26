from de.pschiessle.stripper.node.api.NodeApiObjs import PingResponse


def handle_ping_get() -> PingResponse:
    return PingResponse("RUNNING")

