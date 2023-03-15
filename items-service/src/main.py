from fastapi import FastAPI

from src.database import Base, engine
from src.api.probes_api import router as probes_router
from src.api.items_api import router as items_router

# database init (creating tables)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(probes_router)
app.include_router(items_router)




