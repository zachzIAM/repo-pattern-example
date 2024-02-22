from typing import Optional

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlmodel import Field, Relationship

from .base_model import BaseModel
from .team import Team


class Hero(BaseModel, table=True):
    """Hero table.
    """
    __tablename__ = "Hero"

    name: str = Field(sa_column=Column("Name", String(30), nullable=False))
    secret_name: str = Field(sa_column=Column("SecretName", String(30), nullable=False))
    age: Optional[int] = Field(sa_column=Column("Age", Integer, nullable=True, default=None))
    team_id: Optional[int] = Field(sa_column=Column("TeamId", Integer, ForeignKey("Team.Id")))

    team: Optional["Team"] = Relationship(back_populates="heroes")
