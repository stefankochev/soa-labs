from fastapi import FastAPI

from src.database import Base, engine
from src.api.probes_api import router as probes_router
from src.api.notifications_api import router as notifications_router
from src.api.internal_api import router as internal_router

from src.settings import API_ROOT_PATH

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
