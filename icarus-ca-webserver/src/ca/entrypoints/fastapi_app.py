import logging
import schema
import json
import uuid
import base64
from cryptography import x509

from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import (
    FastAPI,
    Request,
    Response,
    HTTPException,
    UploadFile,
    Depends,
    status,
)

from cryptography.hazmat.primitives import hashes, serialization

from .. import bootstrap

app = FastAPI()

logger = logging.getLogger(__name__)

bus = bootstrap.bootstrap()


@app.get("/certificates")
async def get_all_certificates(request: Request, response: Response):
    pass


@app.post("/certificates")
async def create_new_leaf_certificate_from_csr(request: Request, response: Response):
    csr = await request.body()
    csr_uid = str(uuid.uuid4())

    message = {"csr_uid": csr_uid, "csr": csr}

    try:
        bus.handle_message(
            "StoreLeafCertificateRequest",
            message,
        )
    except schema.SchemaError as e:
        raise HTTPException(404, detail=str(e))
    except Exception as e:
        logger.exception(e)
        raise HTTPException(500, detail="Server Error")

    response.headers.update({"location": "/certificates/" + csr_uid})
    response.status_code = 201

    return response
