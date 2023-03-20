from fastapi import FastAPI

from src.database import Base, engine
from src.api.probes_api import router as probes_router
from src.api.items_api import router as items_router
from src.settings import API_ROOT_PATH

# database init (creating tables)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Items Service",
    root_path=API_ROOT_PATH,
    servers=[{"url": API_ROOT_PATH}],
)

app.include_router(probes_router)
app.include_router(items_router)
