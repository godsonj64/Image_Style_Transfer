from __future__ import annotations

from collections.abc import Generator
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.storage.models import Base


def build_engine(sqlite_path: str):
    return create_engine(f"sqlite+pysqlite:///{sqlite_path}", future=True)


def init_db(sqlite_path: str) -> None:
    engine = build_engine(sqlite_path)
    Base.metadata.create_all(engine)


def build_session_factory(sqlite_path: str):
    engine = build_engine(sqlite_path)
    return sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)


@contextmanager
def session_scope(session_factory: sessionmaker) -> Generator[Session, None, None]:
    session = session_factory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
