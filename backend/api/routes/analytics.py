from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database.dependency import get_db

from services.analytics_service import analytics_service

router = APIRouter()


@router.get("/analytics")
def analytics(

    db: Session = Depends(get_db)

):

    return analytics_service.get_dashboard(
        db
    )