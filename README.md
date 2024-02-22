# Repository and Unit of Work pattern

This is an exploration of this approach to separating business logic and storage. We build on top of [manukanne/sqlmodel-repository-pattern](https://github.com/manukanne/sqlmodel-repository-pattern) and the ralated [dev.to arcticle](https://dev.to/manukanne/a-python-implementation-of-the-unit-of-work-and-repository-design-pattern-using-sqlmodel-3mb5) by decoupling the models further and basing them on Pydantic rather than declaring them as SQL tables.

