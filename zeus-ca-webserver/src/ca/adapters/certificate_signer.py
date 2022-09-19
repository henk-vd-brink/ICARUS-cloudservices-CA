import datetime
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend

class CertificateSigner:
    def __init__(self, path_to_root_ca_cert, path_to_root_ca_key):
        self._root_ca_cert = self._load_root_ca_cert(path_to_root_ca_cert)
        self._root_ca_key = self._load_root_ca_key(path_to_root_ca_key)

    def _load_root_ca_cert(self, path_to_root_ca_cert, backend=default_backend()):
        with open(path_to_root_ca_cert, "rb") as file:
            root_ca_cert_as_bytes = file.read()
        return x509.load_pem_x509_certificate(root_ca_cert_as_bytes, backend)

    def _load_root_ca_key(self, path_to_root_ca_key):
        with open(path_to_root_ca_key, "rb") as file:
            root_ca_key_as_bytes = file.read()
        return serialization.load_pem_private_key(root_ca_key_as_bytes, password=None)

    def get_signed_x509_certificate_from_csr(self, csr_cert):
        return x509.CertificateBuilder().subject_name(
            csr_cert.subject
        ).issuer_name(
            self._root_ca_cert.subject
        ).public_key(
            csr_cert.public_key()
        ).serial_number(
            x509.random_serial_number()
        ).not_valid_before(
            datetime.datetime.utcnow()
        ).not_valid_after(
            datetime.datetime.utcnow() + datetime.timedelta(days=10)
        ).sign(self._root_ca_key, hashes.SHA256())

    def get_signed_x509_certificate_from_csr_as_pem(self, csr_cert):
        cert = self.get_signed_x509_certificate_from_csr(csr_cert=csr_cert)
        return cert.public_bytes(serialization.Encoding.PEM)
