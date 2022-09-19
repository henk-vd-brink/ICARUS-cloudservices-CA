import logging
import schema
import json
import base64
from cryptography import x509

from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import JSONResponse
from cryptography.hazmat.primitives import hashes, serialization

from .. import bootstrap

app = FastAPI()

logger = logging.getLogger(__name__)

bootstrap_items = bootstrap.bootstrap()

certificate_signer = bootstrap_items.get("certificate_signer")

@app.post(
    "/.well-known/est/simpleenroll"
)
async def simple_enroll(
    request: Request,
    response: Response,
):  
    csr = await request.body()

    csr = x509.load_pem_x509_csr(csr)

    cert = certificate_signer.get_signed_x509_certificate_from_csr(csr)
    # cert_bytes = cert.public_bytes(serialization.Encoding.DER)
    # return base64.urlsafe_b64encode(cert_bytes)
    return base64.b64encode(
        serialization.pkcs7.serialize_certificates([cert], serialization.Encoding.DER))
