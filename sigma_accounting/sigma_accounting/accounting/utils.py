from django.core import signing
from django.conf import settings


SECRET_KEY = settings.SECRET_KEY  # Replace this with your actual secret key


def encrypt_cookie(data):
    """
    Encrypts the provided data and returns it as a string suitable for storing in a cookie.
    """
    return signing.dumps(data, key=SECRET_KEY)

def decrypt_cookie(encrypted_data):
    """
    Decrypts the provided encrypted data and returns the original data.
    """
    try:
        return signing.loads(encrypted_data, key=SECRET_KEY)
    except signing.BadSignature:
        # Handle the case where decryption fails (e.g., due to tampering or expired data)
        return None
