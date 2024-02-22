from sqlmodel import text
from repo.model.hero import Hero
from repo.model.team import Team
from repo.service.uow import UnitOfWork


def test_uow_add_hero(session_factory_with_models):

    new_hero = Hero(name="Joey Tribbiani", secret_name="J-Bird", age=30)
    uow = UnitOfWork(session_factory_with_models)

    with uow as w:
        w.heroes.add(new_hero)
        w.commit()

    with uow as w:
        heroes = w.heroes.list()
        teams = w.teams.list()

    assert len(heroes) == 1
    assert len(teams) == 0


def test_uow_add_team(session_factory_with_models):

    new_team = Team(name="Rockers")
    uow = UnitOfWork(session_factory_with_models)

    with uow as w:
        w.teams.add(new_team)
        w.commit()

    with uow as w:
        heroes = w.heroes.list()
        teams = w.teams.list()

    assert len(heroes) == 0
    assert len(teams) == 1


def test_uow_add_hero_with_team(session_factory_with_models):
    new_team = Team(name="Rockers")
    new_hero = Hero(name="Joey Tribbiani", secret_name="J-Bird", age=30, team=new_team)
    uow = UnitOfWork(session_factory_with_models)

    with uow as w:
        w.heroes.add(new_hero)
        w.commit()

    with uow as w:
        heroes = w.heroes.list()
        teams = w.teams.list()

    assert len(heroes) == 1
    assert len(teams) == 1
