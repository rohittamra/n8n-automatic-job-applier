from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Boolean
from sqlalchemy import DateTime

from datetime import datetime

from db.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)

    title = Column(String)
    company = Column(String)

    url = Column(Text)

    description = Column(Text)

    score = Column(Integer)

    status = Column(String, default="pending")

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True)

    job_id = Column(Integer)

    resume_path = Column(Text)

    cover_letter_path = Column(Text)

    approved = Column(Boolean, default=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )