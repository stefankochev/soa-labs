from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from src.database import get_db
from src import schemas
from src import crud


router = APIRouter(tags=["items"])


@router.post("/items", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


@router.get("/items", response_model=list[schemas.Item])
def get_items(db: Session = Depends(get_db), offset: int = 0, limit: int = 100):
    items = crud.get_items(db, offset=offset, limit=limit)
    return items
