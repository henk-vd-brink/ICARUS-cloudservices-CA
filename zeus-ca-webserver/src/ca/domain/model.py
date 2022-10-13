import uuid
from datetime import datetime


class RootCertificate:
    def __init__(
        self,
        common_name: str,
        creation_date: datetime,
        expiration_date: datetime,
    ):
        self.common_name = common_name
        self.creation_date = creation_date
        self.expiration_date = expiration_date
        self.revoked = False
        self.leaf_certificates = set()

        self.events = []


class LeafCertificate:
    def __init__(
        self,
        common_name: str,
        creation_date: datetime,
        expiration_date: datetime,
    ):
        self.uuid = self._create_uuid()
        self.common_name = common_name
        self.creation_date = creation_date
        self.expiration_date = expiration_date
        self.revoked = False

        self.events = []

    def _create_uuid(self):
        return str(uuid.uuid4())

    def __repr__(self):
        return f"<LeafCertificate {self.uuid}>"

    def __eq__(self, other):
        if not isinstance(LeafCertificate, other):
            return False
        return other.uuid == self.uuid
