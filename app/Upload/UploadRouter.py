from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from Upload import UploadService
from database import get_db

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post("/")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    await UploadService.process_csv_file(file, db)
    return {"filename": file.filename}
