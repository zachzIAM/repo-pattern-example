from abc import ABC, abstractmethod
from typing import Optional
from sqlmodel import Session, select

from src.repo.repository.generic import GenericRepository, GenericSqlRepository
from src.repo.schemas import Hero


class HeroReposityBase(GenericRepository[Hero], ABC):
    """Hero repository.
    """
    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Hero]:
        raise NotImplementedError()


class HeroRepository(GenericSqlRepository[Hero], HeroReposityBase):
    def __init__(self, session: Session) -> None:
        super().__init__(session, Hero)

    def get_by_name(self, name: str) -> Optional[Hero]:
        stmt = select(Hero).where(Hero.name == name)
        return self._session.exec(stmt).first()
