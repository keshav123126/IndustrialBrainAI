from uuid import uuid4

from sqlalchemy.orm import Session

from ai.document_processor import document_processor
from ai.metadata_extractor import metadata_extractor
from ai.document_classifier import document_classifier
from ai.summarizer import summarizer

from rag.chunker import chunker
from rag.embedder import embedder
from rag.vector_store import vector_store

from models.document import Document


class DocumentService:

    def process_upload(
        self,
        db: Session,
        file_path,
        filename
    ):

        extracted = document_processor.extract_text(
            file_path
        )

        text = extracted["text"]

        pages = extracted["pages"]

        extracted_metadata = metadata_extractor.extract(
            text,
            pages
        )

        classification = document_classifier.classify(
    text
)

        summary = summarizer.summarize(
    text
)

        document = Document(

    filename=filename,

    filepath=file_path,

    document_type=classification,

    department="Unknown",

    equipment="Unknown",

    summary=summary,

    pages=pages

)

        db.add(document)

        db.commit()

        db.refresh(document)

        chunks = chunker.chunk(text)

        embeddings = embedder.generate(
            chunks
        )

        ids = []

        chunk_metadata = []

        document_id = str(uuid4())

        for i, chunk in enumerate(chunks):

            ids.append(
                f"{document_id}_{i}"
            )

            chunk_metadata.append({

                "document_id": str(document.id),

                "chunk": i,

                "filename": filename

            })

        vector_store.add(

            ids,

            chunks,

            embeddings,

            chunk_metadata

        )

        return {

            "document_id": document.id,

            "summary": summary,

            "classification": classification,

            "metadata": extracted_metadata,

            "chunks": len(chunks)

        }


document_service = DocumentService()