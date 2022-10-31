import requests
import base64
from cryptography import x509
from .create_certificate_request import create_certificate_request
from cryptography.hazmat.primitives import serialization


def decode_est_response(content):
    cert_bytes = base64.b64decode(content)
    return serialization.pkcs7.load_der_pkcs7_certificates(cert_bytes)[0]


if __name__ == "__main__":
    csr = create_certificate_request()

    headers = {
        "content-type": "application/pkcs10",
        "content-transfer-encoding": "base64",
    }

    data = create_certificate_request().public_bytes(serialization.Encoding.DER)
    data = base64.b64encode(data)

    resp = requests.post(
        "http://localhost:8000/.well-known/est/simpleenroll",
        headers=headers,
        data=data,
        auth=("estuser", "estpwd"),
        verify=False,
    )
    cert_pk7 = resp.content
    cert_decoded = decode_est_response(cert_pk7)
    print(resp.headers)

    print(cert_decoded.public_bytes(serialization.Encoding.PEM).decode("utf-8"))
