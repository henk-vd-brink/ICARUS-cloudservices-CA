import base64
from datetime import datetime
from cryptography import x509
from cryptography.hazmat.primitives import serialization


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
    def __init__(self, csr_uid: str, common_name: str, csr: str):
        self.csr_uid = csr_uid
        self.common_name = common_name
        self.csr = csr

        self.events = []

    @staticmethod
    def get_decoded_base64_der_encoded_csr(base64_der_encoded_csr):
        der_encoded_csr = base64.b64decode(base64_der_encoded_csr)
        return x509.load_der_x509_csr(der_encoded_csr)

    @classmethod
    def from_csr_uid_and_base64_der_encoded_csr(cls, csr_uid, base64_der_encoded_csr):
        csr = cls.get_decoded_base64_der_encoded_csr(base64_der_encoded_csr)
        pem_encoded_csr = csr.public_bytes(serialization.Encoding.PEM).decode("utf-8")

        csr_subject = dict(
            [attr.split("=") for attr in csr.subject.rfc4514_string().split(",")]
        )

        csr_common_name = csr_subject.get("CN")

        return cls(csr_uid, csr_common_name, pem_encoded_csr)

    def __repr__(self):
        return f"<LeafCertificateSigningRequest {self.csr_uid}>"

    def __eq__(self, other):
        if not isinstance(LeafCertificateSigningRequest, other):
            return False
        return other.csr_uid == self.csr_uid
