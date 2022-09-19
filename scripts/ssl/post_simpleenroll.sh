#!/bin/bash

    curl --insecure -s http://localhost:8000/.well-known/est/simpleenroll --user estuser:estpwd --output cert.p7 --header "Content-Type: application/pkcs10" --header "Content-Transfer-Encoding: base64" --data-binary @/home/prominendt/repos/ZEUS-services-CA/dev/certs/testcsr.pem