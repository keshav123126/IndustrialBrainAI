from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database.dependency import get_db

from services.library_service import library_service

router = APIRouter()


@router.get("/documents")
def documents(

    db: Session = Depends(get_db)

):

    return library_service.get_all(db)