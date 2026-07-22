import os

from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import HTTPException
from fastapi import UploadFile

from sqlalchemy.orm import Session

from database.dependency import get_db
from services.document_service import document_service
from utils.file_utils import FileUtils

router = APIRouter()


@router.post("/upload")
async def upload_document(
    db: Session = Depends(get_db),
    file: UploadFile = File(...)
):

    try:

        FileUtils.validate(
            file.filename
        )

        filename = FileUtils.unique_name(
            file.filename
        )

        os.makedirs(
            "uploads",
            exist_ok=True
        )

        save_path = os.path.join(
            "uploads",
            filename
        )

        with open(
            save_path,
            "wb"
        ) as f:

            f.write(
                await file.read()
            )

        result = document_service.process_upload(
            db=db,
            file_path=save_path,
            filename=filename
        )

        return {

            "status": "success",

            "filename": filename,

            "result": result

        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )