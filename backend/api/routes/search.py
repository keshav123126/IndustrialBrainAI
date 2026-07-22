from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database.dependency import get_db

from services.search_service import search_service

router = APIRouter()


@router.get("/search")
def search(

    query: str,

    db: Session = Depends(get_db)

):

    return search_service.search(
        db,
        query
    )