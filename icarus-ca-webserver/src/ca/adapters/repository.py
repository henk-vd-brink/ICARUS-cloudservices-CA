import abc
import typing

from ..domain import model


class AbstractRepository(abc.ABC):
    def __init__(self) -> None:
        self.seen = set()


class LeafCertificateSigningRequestSqlAlchemyRepository(AbstractRepository):
    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def get_from_csr_uid(self, csr_uid):
        csr = (
            self.session.query(model.LeafCertificateSigningRequest)
            .filter_by(csr_ui=csr_uid)
            .first()
        )

        if csr:
            self.seen.add(csr)

        return csr
