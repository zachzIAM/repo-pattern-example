import pytest

from repo.db.tables import Base
from repo.settings import Settings
from repo.db import create_sqlmodel_engine, sqlmodel_session_maker


@pytest.fixture(scope="function")
def session_factory():
    db_settings = Settings(database_connection_str="sqlite://")
    engine = create_sqlmodel_engine(db_settings)
    session_factory = sqlmodel_session_maker(engine)

    return session_factory


@pytest.fixture(scope="function")
def session_factory_with_models():
    db_settings = Settings(database_connection_str="sqlite://")
    engine = create_sqlmodel_engine(db_settings)
    session_factory = sqlmodel_session_maker(engine)

    with session_factory() as session:
        Base.metadata.create_all(session.get_bind())

    return session_factory
