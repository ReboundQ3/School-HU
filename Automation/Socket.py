import socket
import sys
import subprocess
import errno
import os
import datetime
from time import sleep

HOST = '' # Alle beschikbare interfaces
PORT = 8888 # Willekeurige poort (denk aan firewall bij Windows Systemen)
time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
log = open("socket.log","a")
sys.stdout = log

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # avoid TIME_WAIT error
    s.bind((HOST, PORT))
    s.listen(10)
    print('#>' '['+time+']'' ##SCRIPT START##')
    print('#>' '['+time+']'' Socket luistert op poort:',PORT)
except socket.error as e:
    if e.errno == errno.EADDRINUSE:
        print('#>' '['+time+']'' Port al in gebruik')
        print('#>' '['+time+']'' Script wordt afgesloten')
        quit()
    else:
        print(e)

#login credentials
username = "koen"
password = "nacho"

# Wacht op connecties (blocking)
conn, addr = s.accept()

# Er is een client verbonden met de server
print('#>' '['+time+']'' Verbonden met ' + addr[0] + ':' + str(addr[1]))

# De server meldt zich aan de client
conn.sendall(b'#> Welkom Op Mijn Server\r\n')

while True:
    conn.sendall(b'#> Username: ')
    username_input = conn.recv(1024)
    username_input=str(username_input.decode('ascii')).rstrip()
    conn.sendall(b'#> Password: ')
    password_input = conn.recv(1024)
    password_input=str(password_input.decode('ascii')).rstrip()
    if password_input == password and username_input == username:
        conn.sendall(b'#> Login success welkom\r\n')
        print('#>' '['+time+'] ''LOGIN GOED YAY')
        break
    elif password_input != password or username_input != username:
        conn.sendall(b'#> Login gefaald probeer het opnieuw\r\n')
        print('#>' '['+time+'] ''LOGIN FOUT')


# Wacht op input van de client en geef deze ook weer terug (echo service)
while 1 == 1:
    data = conn.recv(1024)
    data=str(data.decode('ascii')).rstrip() # # Remove \r | \n | \r\n
    print('#>' '['+time+'] ''Client data ontvangen:'+data+'.')
    conn.sendall(b'#> '+data.encode())
    conn.sendall(b'\r\n')
    if data == "stop":
        print('#>' '['+time+'] ''STOP commando ontvangen socket sluit')
        conn.sendall(b'#> STOP commando ontvangen tot ziens\r\n')
        sleep(2)
        conn.close()
        s.close()
        quit()
    if data == "calc":
        print('#>' '['+time+'] ''CALC commando ontvangen calculator opent')
        conn.sendall(b'#> CALC commando ontangen calculator opent\r\n')
        sleep(2)
        os.system("kcalc")
    if data == "notepad":
        print('#>' '['+time+'] ''notepad commando ontangen notepad opent')
        conn.sendall(b'#> Notepad commando ontvangen notepad opent\r\n')
        sleep(2)
        os.system("kwrite")
        
# Verbreek de verbinding en sluit de socket
conn.close()
s.close()
log.close()