from pathlib import Path
from uuid import uuid4

ALLOWED_EXTENSIONS = {".pdf"}

MAX_FILE_SIZE = 25 * 1024 * 1024


class FileUtils:

    @staticmethod
    def validate(filename):

        ext = Path(filename).suffix.lower()

        if ext not in ALLOWED_EXTENSIONS:
            raise ValueError(
                "Only PDF files are allowed."
            )

    @staticmethod
    def unique_name(filename):

        ext = Path(filename).suffix

        return f"{uuid4()}{ext}"