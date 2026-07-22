from sqlalchemy.orm import Session

from models.document import Document


class LibraryService:

    def get_all(
        self,
        db: Session
    ):

        documents = db.query(
            Document
        ).order_by(
            Document.uploaded_at.desc()
        ).all()

        result = []

        for doc in documents:

            result.append({

                "id": doc.id,

                "filename": doc.filename,

                "document_type": doc.document_type,

                "department": doc.department,

                "equipment": doc.equipment,

                "pages": doc.pages,

                "summary": doc.summary,

                "uploaded_at": doc.uploaded_at

            })

        return result


library_service = LibraryService()