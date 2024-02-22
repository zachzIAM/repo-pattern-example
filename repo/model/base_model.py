from typing import Optional

from sqlalchemy import Column, Integer
from sqlmodel import SQLModel, Field


class BaseModel(SQLModel):
    """Base SQL model class.
    """

    id: Optional[int] = Field(sa_column=Column("Id", Integer, primary_key=True, autoincrement=True))

    class Config:
        alias_generator = lambda s: s.upper()
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
