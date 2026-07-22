from sqlalchemy.orm import Session
from sqlalchemy import func

from models.document import Document


class AnalyticsService:

    def get_dashboard(
        self,
        db: Session
    ):

        total_documents = db.query(
            func.count(Document.id)
        ).scalar()

        total_pages = db.query(
            func.sum(Document.pages)
        ).scalar()

        return {

            "total_documents": total_documents or 0,

            "total_pages": total_pages or 0

        }


analytics_service = AnalyticsService()