import sys
import os
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import hashlib

with open("message.txt", "rb") as message_data:
    message = message_data.read()
    print(message)

    
if os.path.isfile("./private.pem") == False:
    key = RSA.generate(2048)
    private_key = key.export_key()
    with open("private.pem", "wb") as f:
        f.write(private_key)
else:
    print("#> Private key bestaat! skipping")

if os.path.isfile("./public.pem") == False:
    public_key = key.publickey().export_key()
    with open("public.pem", "wb") as f:
        f.write(public_key)
else:
    print("#> Public key bestaat! skipping")

key = RSA.import_key(open('private.pem').read())
hash = SHA256.new(message)
signature = pkcs1_15.new(key).sign(hash)

with open("message.signature", "wb") as message_sig:
    message_sig.write(signature)