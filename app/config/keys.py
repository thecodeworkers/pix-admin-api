from cryptography.hazmat.primitives import hashes, hmac
from cryptography.exceptions import InvalidSignature

default_econde = 'utf-8'

def create_application_token(app_key, app_name):
    cypher = hmac.HMAC(app_key.encode(default_econde), hashes.SHA256())
    cypher.update(app_name.encode(default_econde))
    token = cypher.finalize()

    return token.hex()

def verify_application_token(app_key, app_name, token):
    try:
        cypher = hmac.HMAC(app_key.encode(default_econde), hashes.SHA256())
        cypher.update(app_name.encode(default_econde))
        cypher.verify(bytes.fromhex(token))

        return True

    except InvalidSignature:
        return False
    except Exception:
        return False
