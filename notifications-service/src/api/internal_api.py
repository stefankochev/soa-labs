from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from src.database import get_db
from src import schemas
from src import crud


router = APIRouter(prefix="/internal", tags=["internal"])


@router.post("/notifications", response_model=dict)
def send_notifications_bulk(
    notifications: list[schemas.NotificationCreate], db: Session = Depends(get_db)
):
    """Bulk send notifications."""
    crud.create_notifications_bulk(db=db, notifications=notifications)
    return {"status": "ok"}
