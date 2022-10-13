import requests
import base64
from cryptography import x509
from .create_certificate_request import create_certificate_request
from cryptography.hazmat.primitives import serialization

text = b"MIICXzCCAUcCAQAwGjEYMBYGA1UEAwwPbXlpb3RlZGdlZGV2aWNlMIIBIjANBgkq\nhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2ADsGWAYoVP+uhJDIE+QLfXwQ6fbARQ9\nqJAP1yRmzf2WFVLJJIsD3WQcFr/fk0B2PRfIT/I/dtwbmRvVZ+WzACEEes9ggr6M\noGhdZaEYvwG2hf8p4oQmpV8wybHTZ2fFPakzVODQ5xLEr6AUutZbkXyr/GSahHyM\nrIUAZoAVPm9vMbIrxCO9llw6i/CEhDFCnMy2o205SJUSc+3pcmBNqj+K2ZkM0GCY\nWkO17rlpzch8XMdvhEAoOAlcuoU+mrexItYfC2lqbujR4eespqsrS2izqK58V4s+\ng6roNbUkCrlwSJ3BhX+pbU9IjyLq15Y9UWFTzKEePnqL8GE00rwnqwIDAQABoAAw\nDQYJKoZIhvcNAQELBQADggEBALLmFKp31ry+IorZWqh30TU4BxVqJQ2S07Ba8VkC\nJMjmuluUFYHTH0Eb4f7qMsdsTlcxvV09pKXRFvYePPADCtjczfJuBLDji0BJiNkg\n7cGMzp41vJ3Ak9hrEqAkZjTWQY0+FxlbNpum0PWOXipzV0aImUrMqk7kVnV7B58U\nAO2GqVLQbSOcV1OmZFhBmdjbGJq5QGCW8eJ5sVaN/PFEO0zlCW7RZiDoxunqnJie\n5uAvGhC56cQ8gDTAWyZX1j3H56zi4dpL67IsAFo19j6ULVnpbkCQPqHFPD+tL3yU\nw6G6MgY6djcMjQlQ6PPnN7nIyZqXCmC4/H9CsFvtRv7pbok=\n"

cert_bytes = base64.b64decode(text)

print(cert_bytes)