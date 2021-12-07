from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Dashboard import DashBoardService
from database import get_db

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    return DashBoardService.get_stats(db)
