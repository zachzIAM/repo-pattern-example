from sqlalchemy import (
    INTEGER,
    NVARCHAR,
    Column,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from repo.db.tables.base import Base


class Hero(Base):
    __tablename__ = "Hero"
    Id = Column(INTEGER, primary_key=True, autoincrement=True)
    Name = Column(NVARCHAR(30), nullable=False)
    SecretName = Column(NVARCHAR(30), nullable=False)
    Age = Column(INTEGER, nullable=False, default=None)
    TeamId = Column(INTEGER, ForeignKey("Team.Id"))
    Team = relationship("Team", back_populates="heroes")
