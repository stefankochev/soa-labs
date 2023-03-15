from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from src.database import get_db
from src import schemas
from src import crud


router = APIRouter(tags=["notifications"])


@router.post("/notifications", response_model=schemas.Notification)
def create_notification(item: schemas.NotificationCreate, db: Session = Depends(get_db)):
    return crud.create_notification(db=db, item=item)


@router.get("/notifications", response_model=list[schemas.Notification])
def get_notifications(db: Session = Depends(get_db), offset: int = 0, limit: int = 100):
    items = crud.get_notifications(db, offset=offset, limit=limit)
    return items
