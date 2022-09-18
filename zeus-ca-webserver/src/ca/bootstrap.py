import inspect
from . import config

from .adapters import certificate_signer as cs

def bootstrap(
    certificate_signer = cs.CertificateSigner(
        path_to_root_ca_cert="/home/prominendt/repos/ZEUS-services-CA/dev/certs/root_ca.pem",
        path_to_root_ca_key="/home/prominendt/repos/ZEUS-services-CA/dev/certs/root_ca.key"
    )
):

    return {"certificate_signerToken": certificate_signer}