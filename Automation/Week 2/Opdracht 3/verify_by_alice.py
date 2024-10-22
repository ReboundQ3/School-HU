from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from cryptography.fernet import Fernet

fkey = open('fkey.key').read()
fernet = Fernet(fkey)

with open("message.encrypted", "rb") as message_data:
    encmessage = message_data.read()
    message = fernet.decrypt(encmessage).decode()
    print("#> Bericht van Bob:", message.strip())

with open("message.signature", "rb") as signature_data:
    signature = signature_data.read()

#Checken of er gekloot is met het bestand
key = RSA.import_key(open('public.pem').read())
h = SHA256.new(encmessage)

try:
    pkcs1_15.new(key).verify(h, signature)
    print("#> The signature is valid.")
except (ValueError, TypeError):
   print("#> The signature is not valid.")