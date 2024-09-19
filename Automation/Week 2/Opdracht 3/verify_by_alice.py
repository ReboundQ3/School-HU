from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

with open("message.txt", "rb") as message_data:
    message = message_data.read()
    print(message.strip())
    
with open("message.signature", "rb") as signature_data:
    signature = signature_data.read()

key = RSA.import_key(open('public.pem').read())
h = SHA256.new(message)

try:
    pkcs1_15.new(key).verify(h, signature)
    print("The signature is valid.")
except (ValueError, TypeError):
   print("The signature is not valid.")