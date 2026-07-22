from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime

from datetime import datetime

from database.base import Base


class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)

    filename = Column(String, nullable=False)

    filepath = Column(String, nullable=False)

    document_type = Column(String)

    department = Column(String)

    equipment = Column(String)

    summary = Column(Text)

    pages = Column(Integer)

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )