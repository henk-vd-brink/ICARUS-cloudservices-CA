import abc
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session


from .. import config
from ..adapters import repository


class AbstractUnitOfWork(abc.ABC):

    images: repository.AbstractRepository

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError

    def collect_new_events(self):
        for image in self.images.seen:
            while image.events:
                yield image.events.pop(0)
        for transaction in self.transactions.seen:
            while transaction.events:
                yield transaction.events.pop(0)
        for pos_event in self.pos_events.seen:
            while pos_event.events:
                yield pos_event.events.pop(0)


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        config.get_postgres_uri(),
        isolation_level="REPEATABLE READ",
    )
)


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()  # type: Session
        self.images = repository.ImageSqlAlchemyRepository(self.session)
        self.transactions = repository.TransactionSqlAlchemyRepository(self.session)
        self.pos_events = repository.PosEventSqlAlchemyRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
