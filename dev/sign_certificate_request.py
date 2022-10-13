import datetime
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend


def load_root_certificate(path_to_root_ca_cert, backend=default_backend()):
    with open(path_to_root_ca_cert, "rb") as file:
        root_certificate = file.read()

    return x509.load_pem_x509_certificate(root_certificate, backend)


def load_root_key(path_to_root_key, backend=default_backend()):
    with open(path_to_root_key, "rb") as file:
        root_key = file.read()

    return serialization.load_pem_private_key(root_key, password=None)


def sign_certificate_request(csr_cert, ca_cert, private_ca_key):
    cert = (
        x509.CertificateBuilder()
        .subject_name(csr_cert.subject)
        .issuer_name(ca_cert.subject)
        .public_key(csr_cert.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.utcnow())
        .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=10))
        .sign(private_ca_key, hashes.SHA256())
    )

    return cert


if __name__ == "__main__":
    from .create_certificate_request import create_certificate_request

    csr_cert = create_certificate_request()

    ca_cert = load_root_certificate(
        "/home/prominendt/repos/ZEUS-services-CA/dev/certs/root_ca.pem"
    )
    private_ca_key = load_root_key(
        "/home/prominendt/repos/ZEUS-services-CA/dev/certs/root_ca.key"
    )

    cert = sign_certificate_request(
        csr_cert=csr_cert, ca_cert=ca_cert, private_ca_key=private_ca_key
    )
    print(cert.subject)
    # print(ca_cert.public_bytes(serialization.Encoding.PEM).decode("utf-8"))
    # print(cert.public_bytes(serialization.Encoding.PEM).decode("utf-8"))
