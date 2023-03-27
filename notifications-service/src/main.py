import asyncio

from fastapi import FastAPI

from src.database import Base, engine
from src.api.probes_api import router as probes_router
from src.api.notifications_api import router as notifications_router
from src.api.internal_api import router as internal_router

from src.settings import API_ROOT_PATH

from src.pubsub.consumer import get_consumer, consume


# database init (creating tables)
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Notifications Service",
    root_path=API_ROOT_PATH,
    servers=[{"url": API_ROOT_PATH}],
)

app.include_router(probes_router)
app.include_router(notifications_router)
app.include_router(internal_router)


@app.on_event("startup")
async def startup_event():
    loop = asyncio.get_event_loop()
    loop.create_task(consume())


@app.on_event("shutdown")
async def shutdown_event():
    consumer = get_consumer()
    await consumer.stop()
