import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidKey


backend = default_backend()

salt = os.urandom(16)

kdf = PBKDF2HMAC(
     algorithm=hashes.SHA256(),
     length=32,
     salt=salt,
     iterations=100000,
     backend=backend
 )

key = kdf.derive(b"my great password")
print(key)

kdf = PBKDF2HMAC(
     algorithm=hashes.SHA256(),
     length=32,
     salt=salt,
     iterations=100000,
     backend=backend
 )

try:
    kdf.verify(b"my great password", key)
    print("same password")
except InvalidKey:
    print("not the same password")