from sqlmodel import text


def test_connection(session_factory):
    with session_factory() as session:
        tables = session.execute(text("SELECT * FROM sqlite_master WHERE type='table'"))

    assert len(tables.fetchall()) == 0


def test_create_table(session_factory):
    with session_factory() as session:
        create_table_statement = text("CREATE TABLE contacts (id INTEGER PRIMARY KEY);")
        session.execute(create_table_statement)
        tables = session.execute(text("SELECT * FROM sqlite_master WHERE type='table'"))

    assert len(tables.fetchall()) == 1
