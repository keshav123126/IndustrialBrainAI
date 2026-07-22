from sqlalchemy import Column
from sqlalchemy import Integer

from database.base import Base


class Analytics(Base):

    __tablename__ = "analytics"

    id = Column(Integer, primary_key=True)

    total_documents = Column(Integer, default=0)

    total_questions = Column(Integer, default=0)

    total_pages = Column(Integer, default=0)