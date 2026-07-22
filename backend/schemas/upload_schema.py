from pydantic import BaseModel


class UploadResponse(BaseModel):

    id: int

    filename: str

    pages: int

    summary: str

    document_type: str