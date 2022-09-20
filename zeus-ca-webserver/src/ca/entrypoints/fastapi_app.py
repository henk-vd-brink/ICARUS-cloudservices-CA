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


@app.post("/.well-known/est/simpleenroll")
async def simple_enroll(
    request: Request,
    response: Response,
):
    csr_b64 = await request.body()
    csr = base64.b64decode(csr_b64)

    csr = x509.load_der_x509_csr(csr)

    cert = certificate_signer.get_signed_x509_certificate_from_csr(csr)

    return Response(
        content=base64.b64encode(
            serialization.pkcs7.serialize_certificates(
                [cert], serialization.Encoding.DER
            )
        ),
        status_code=200,
        headers={"status": "200 OK", "content-transfer-encoding": "base64"},
        media_type="application/pkcs7-mime; smime-type=certs-only",
    )


@app.get("/.well-known/est/cacerts")
async def simple_enroll(
    request: Request,
    response: Response,
):
    cert = certificate_signer.get_root_ca_certificate()

    return Response(
        content=base64.b64encode(
            serialization.pkcs7.serialize_certificates(
                [cert], serialization.Encoding.DER
            )
        ),
        status_code=200,
        headers={"status": "200 OK", "content-transfer-encoding": "base64"},
        media_type="application/pkcs7-mime",
    )
