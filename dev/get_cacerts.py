import requests
import base64
from .create_certificate_request import create_certificate_request
from cryptography.hazmat.primitives import serialization


def decode_est_response(content):
    cert_bytes = base64.b64decode(content)
    return serialization.pkcs7.load_der_pkcs7_certificates(cert_bytes)[0]

def get_cacerts():
    headers = {
        "Content-Type": "application/pkcs10",
        "Content-Transfer-Encoding": "base64"
    }

    resp = requests.get(
            "http://localhost:8000/.well-known/est/cacerts",
            headers=headers,
            auth=("estuser", "estpwd"),
            verify=False
    )
    cert_pk7 = resp.content
    cert_decoded = decode_est_response(cert_pk7)
    print(cert_decoded.public_bytes(serialization.Encoding.PEM).decode("utf-8"))


if __name__ == "__main__":
    csr = create_certificate_request()
    get_cacerts()

    # print(cert_decoded.public_bytes(serialization.Encoding.PEM).decode("utf-8"))