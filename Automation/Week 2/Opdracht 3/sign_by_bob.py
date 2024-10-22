import sys
import os
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import hashlib
from cryptography.fernet import Fernet

with open("message.txt", "rb") as message_data:
    message = message_data.read()
    print(message)
    
if os.path.isfile("./private.pem") == False:
    key = RSA.generate(2048)
    private_key = key.export_key()
    with open("private.pem", "wb") as f:
        f.write(private_key)
else:
    print("")
    print("#> Private key bestaat! skipping")

if os.path.isfile("./public.pem") == False:
    public_key = key.publickey().export_key()
    with open("public.pem", "wb") as f:
        f.write(public_key)
else:
    print("")
    print("#> Public key bestaat! skipping")
    
if os.path.isfile("./fkey.key") == False:
    newfkey = Fernet.generate_key()
    with open("fkey.key", "wb") as f:
        f.write(newfkey)
else:
    print("")
    print("#> Encryption key bestaat! skipping")

fkey = open('fkey.key').read()
fernet = Fernet(fkey)
encMessage = fernet.encrypt(message)
key = RSA.import_key(open('private.pem').read())
hash = SHA256.new(encMessage)
signature = pkcs1_15.new(key).sign(hash)
fkey = open('fkey.key').read()

print("")
print("#> Encyption Key:", fkey)

print("")
print("#> Verleuteld Bericht:", encMessage)

with open("message.encrypted", "wb") as f:
    f.write(encMessage)

with open("message.signature", "wb") as message_sig:
    message_sig.write(signature)