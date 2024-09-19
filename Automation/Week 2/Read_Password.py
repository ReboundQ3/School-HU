with open("password.txt","r") as pf:
    for line in pf:
        password = line
    
password_input = input('Please input your password: ')
if password == password_input:
    print("Password OK")
    quit()
else:
    print("Password FOUT")
    quit()