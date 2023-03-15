import socket
from fastapi import APIRouter


router = APIRouter(tags=["probes"])


@router.get("/healthcheck")
def healthcheck_probe():
    ip_address = socket.gethostbyname(socket.gethostname())
    return {"status": f"ok from {ip_address}"}
