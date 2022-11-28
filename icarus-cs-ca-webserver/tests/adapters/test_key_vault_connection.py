import os
import dotenv

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

if dotenv.find_dotenv():
    dotenv.load_dotenv()

key_vault_name = os.environ.get("AZURE_KEY_VAULT_NAME")
key_vault_uri = f"https://{key_vault_name}.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=key_vault_uri, credential=credential)


retrieved_secret = client.get_secret("test-secret")
