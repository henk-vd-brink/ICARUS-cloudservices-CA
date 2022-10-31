import base64
from cryptography import x509
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


class LeafCertificateSigningRequest:
    def __init__(
        self,
        csr_uid: str,
    ):
        self.csr_uid = csr_uid

        self.events = []

    @classmethod
    def from_csr_uid_and_pem_encoded_csr(cls, csr_uid, pem_encoded_csr):
        csr = x509.load_pem_x509_csr(pem_encoded_csr)

        print(dir(csr))

        return cls(csr_uid)

    def __repr__(self):
        return f"<LeafCertificateSigningRequest {self.csr_uid}>"

    def __eq__(self, other):
        if not isinstance(LeafCertificateSigningRequest, other):
            return False
        return other.csr_uid == self.csr_uid
