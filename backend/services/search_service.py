from sqlalchemy.orm import Session
from sqlalchemy import or_

from models.document import Document


class SearchService:

    def search(
        self,
        db: Session,
        query: str
    ):

        documents = db.query(Document).filter(

            or_(

                Document.filename.ilike(f"%{query}%"),

                Document.department.ilike(f"%{query}%"),

                Document.equipment.ilike(f"%{query}%"),

                Document.document_type.ilike(f"%{query}%")

            )

        ).all()

        result = []

        for doc in documents:

            result.append({

                "id": doc.id,

                "filename": doc.filename,

                "department": doc.department,

                "equipment": doc.equipment,

                "document_type": doc.document_type,

                "summary": doc.summary

            })

        return result


search_service = SearchService()