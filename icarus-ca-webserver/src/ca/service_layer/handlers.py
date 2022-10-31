from ..domain import model, commands


def store_leaf_certificate_request(cmd, uow):
    csr = cmd.csr
    csr_uid = cmd.csr_uid

    with uow:
        model.LeafCertificateSigningRequest.from_csr_uid_and_pem_encoded_csr(
            csr_uid, csr
        )


COMMAND_HANDLERS = {
    commands.StoreLeafCertificateRequest: store_leaf_certificate_request
}

EVENT_HANDLERS = {}
