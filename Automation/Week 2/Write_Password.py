import hashlib

with open("password.txt","w") as pf:
    password = input('Please input your password: ')
    hashed_password = hashlib.sha1(password.encode())
    print(hashed_password.hexdigest())
    pf.write(hashed_password.hexdigest())