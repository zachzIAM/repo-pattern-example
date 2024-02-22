from sqlalchemy import (
    INTEGER,
    NVARCHAR,
    Column,
)
from sqlalchemy.orm import relationship
from repo.db.tables.base import Base


class Team(Base):
    __tablename__ = "Team"
    Id = Column(INTEGER, primary_key=True, autoincrement=True)
    Name = Column(NVARCHAR(30), nullable=False, unique=True)
    heroes = relationship("Hero", back_populates="Team")
