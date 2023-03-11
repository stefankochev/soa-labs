from fastapi import APIRouter


router = APIRouter(tags=["probes"])


@router.get("/healthcheck")
def healthcheck_probe():
    return {"status": "ok"}

