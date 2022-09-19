import requests
import base64
from cryptography import x509
from .create_certificate_request import create_certificate_request
from cryptography.hazmat.primitives import hashes, serialization


def decode_est_response(content):
    cert_bytes = base64.b64decode(cert_pk7)
    return serialization.pkcs7.load_der_pkcs7_certificates(cert_bytes)[0]

if __name__ == "__main__":
    csr = create_certificate_request()
    
    headers = {
        "Content-Type": "application/pkcs10",
        "Content-Transfer-Encoding": "base64"
    }
    
    data = create_certificate_request().public_bytes(serialization.Encoding.PEM)

    resp = requests.post(
            "http://localhost:8000/.well-known/est/simpleenroll",
            headers=headers,
            data=data,
            auth=("estuser", "estpwd"),
            verify=False
    )
    cert_pk7 = resp.content

    print(resp.headers)


    cert_decoded = decode_est_response(cert_pk7)

    # print(cert_decoded.public_bytes(serialization.Encoding.PEM).decode("utf-8"))



