from abc import ABC, abstractmethod
from typing import Optional
from sqlmodel import Session, select

from repo.repository.generic import GenericRepository, GenericSqlRepository
from repo.model.team import Team


class TeamRepositoryBase(GenericRepository[Team], ABC):
    """Team repository.
    """
    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Team]:
        raise NotImplementedError()


class TeamRepository(GenericSqlRepository[Team], TeamRepositoryBase):
    def __init__(self, session: Session) -> None:
        super().__init__(session, Team)

    def get_by_name(self, name: str) -> Optional[Team]:
        stmt = select(Team).where(Team.name == name)
        return self._session.exec(stmt).first()