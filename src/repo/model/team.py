from typing import List

from sqlalchemy import Column, String
from sqlmodel import Field, Relationship

from src.repo.model.base_model import BaseModel


class Team(BaseModel, table=True):
    """Team table.
    """
    __tablename__ = "Team"

    name: str = Field(sa_column=Column("Name", String(30), nullable=False, unique=True))

    heroes: List["Hero"] = Relationship(back_populates="team")
