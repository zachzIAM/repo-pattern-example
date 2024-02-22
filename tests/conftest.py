import pytest
from repo.settings import Settings
from repo.db import create_sqlmodel_engine, sqlmodel_session_maker


@pytest.fixture(scope="function")
def session_factory():
    db_settings = Settings(database_connection_str="sqlite://")
    engine = create_sqlmodel_engine(db_settings)
    session_factory = sqlmodel_session_maker(engine)

    return session_factory

