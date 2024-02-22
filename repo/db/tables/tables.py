from sqlalchemy import MetaData, Column, INTEGER, NVARCHAR, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    metadata = MetaData(
            naming_convention={
                "ix": "ix_%(column_0_label)s",
                "uq": "uq_%(table_name)s_%(column_0_name)s",
                "ck": "ck_%(table_name)s_%(constraint_name)s",
                "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
                "pk": "pk_%(table_name)s",
            },
        )


class Hero(Base):
    __tablename__ = "Hero"
    Id = Column(INTEGER, primary_key=True, autoincrement=True)
    Name = Column(NVARCHAR(30), nullable=False)
    SecretName = Column(NVARCHAR(30), nullable=False)
    Age = Column(INTEGER, nullable=False, default=None)
    TeamId = Column(INTEGER, ForeignKey("Team.Id"))
    Team = relationship("Team", back_populates="heroes")


class Team(Base):
    __tablename__ = "Team"
    Id = Column(INTEGER, primary_key=True, autoincrement=True)
    Name = Column(NVARCHAR(30), nullable=False, unique=True)
    heroes = relationship("Hero", back_populates="Team")
