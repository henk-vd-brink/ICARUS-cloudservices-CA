import logging
import schema
from cryptography import x509

from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import JSONResponse

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

    cert = certificate_signer.get_signed_x509_certificate_from_csr_as_pem(csr)

    # print(certificate_signer.get_signed_x509_certificate_from_csr_as_pem(csr).decode("utf-8"))



@app.get(
    "/.well-known/est/cacerts"
)
async def simple_enroll(
    request: Request,
    response: Response,
):
    print(request.__dict__)