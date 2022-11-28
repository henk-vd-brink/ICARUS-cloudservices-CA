import inspect
from . import config

from .adapters import certificate_signer as cs


def bootstrap(
    certificate_signer=cs.CertificateSigner(
        path_to_root_ca_cert="/home/docker_user/certs/root_ca.pem",
        path_to_root_ca_key="/home/docker_user/certs/root_ca.key",
    )
):

    return {"certificate_signer": certificate_signer}
