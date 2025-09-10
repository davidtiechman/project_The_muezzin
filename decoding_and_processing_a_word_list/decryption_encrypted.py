import base64
def decrypt_base64(encoder):
    decoder = base64.b64decode(encoder)
    return decoder

