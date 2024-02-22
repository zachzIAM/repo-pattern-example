from sqlmodel import text
from repo.model.hero import Hero
from repo.model.team import Team
from repo.repository.hero import HeroRepository
from repo.repository.team import TeamRepository


def test_add_hero(session_factory_with_models):

    new_hero = Hero(name="Joey Tribbiani", secret_name="J-Bird", age=30)

    with session_factory_with_models() as session:
        repository = HeroRepository(session)
        repository.add(new_hero)
        session.commit()

    with session_factory_with_models() as session:
        heroes = session.execute(text("SELECT * FROM Hero"))
        teams = session.execute(text("SELECT * FROM Team"))

    assert len(heroes.fetchall()) == 1
    assert len(teams.fetchall()) == 0


def test_add_team(session_factory_with_models):

    new_team = Team(name="Rockers")

    with session_factory_with_models() as session:
        repository = TeamRepository(session)
        repository.add(new_team)
        session.commit()

    with session_factory_with_models() as session:
        heroes = session.execute(text("SELECT * FROM Hero"))
        teams = session.execute(text("SELECT * FROM Team"))

    assert len(heroes.fetchall()) == 0
    assert len(teams.fetchall()) == 1


def test_add_hero_with_team(session_factory_with_models):
    new_team = Team(name="Rockers")
    new_hero = Hero(name="Joey Tribbiani", secret_name="J-Bird", age=30, team=new_team)

    with session_factory_with_models() as session:
        repository = HeroRepository(session)
        repository.add(new_hero)
        session.commit()

    with session_factory_with_models() as session:
        heroes = session.execute(text("SELECT * FROM Hero"))
        teams = session.execute(text("SELECT * FROM Team"))

    assert len(heroes.fetchall()) == 1
    assert len(teams.fetchall()) == 1
