from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa


COUNTRY_NAME = "NL"
STATE_OR_PROVINCE_NAME = "Zuid-Holland"
LOCALITY_NAME = "Delft"
ORGANIZATION_NAME = "Prominendt B.V."
COMMON_NAME = "edge-device-1"
DNS_NAME = "prominendt.com"


def create_certificate_request():

    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    certificate_request = (
        x509.CertificateSigningRequestBuilder()
        .subject_name(
            x509.Name(
                [
                    x509.NameAttribute(NameOID.COUNTRY_NAME, COUNTRY_NAME),
                    x509.NameAttribute(
                        NameOID.STATE_OR_PROVINCE_NAME, STATE_OR_PROVINCE_NAME
                    ),
                    x509.NameAttribute(NameOID.LOCALITY_NAME, LOCALITY_NAME),
                    x509.NameAttribute(NameOID.ORGANIZATION_NAME, ORGANIZATION_NAME),
                    x509.NameAttribute(NameOID.COMMON_NAME, COMMON_NAME),
                ]
            )
        )
        .add_extension(
            x509.SubjectAlternativeName(
                [
                    x509.DNSName(DNS_NAME),
                    x509.DNSName("www." + DNS_NAME),
                ]
            ),
            critical=False,
        )
        .sign(key, hashes.SHA256())
    )

    return certificate_request


if __name__ == "__main__":
    print(
        create_certificate_request()
        .public_bytes(serialization.Encoding.PEM)
        .decode("utf-8")
    )
