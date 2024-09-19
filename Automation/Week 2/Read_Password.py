import hashlib

with open("password.txt","r") as pf:
    for line in pf:
        password = line
        print(password)
        
password_input = input('Please input your password: ')
if password == hashlib.sha1(password_input.encode()).hexdigest():
    print("Password OK")
    quit()
else:
    print("Password FOUT")
    quit()