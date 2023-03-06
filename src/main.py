from fastapi import FastAPI

from src.database import Base, engine
from src.api import router as items_router

# database init (creating tables)
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(items_router)




