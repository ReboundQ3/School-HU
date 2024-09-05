import socket
import sys
import subprocess
import errno
import os
from time import sleep

HOST = '' # Alle beschikbare interfaces
PORT = 8888 # Willekeurige poort (denk aan firewall bij Windows Systemen)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # avoid TIME_WAIT error
    s.bind((HOST, PORT))
    s.listen(10)
    print('#> Socket luistert op poort:',PORT)
except socket.error as e:
    if e.errno == errno.EADDRINUSE:
        print('#> Port al in gebruik')
        print("#> Script wordt afgesloten")
        sleep(3)
        quit()
    else:
        print(e)
        
username = "Koen"
Password = "nacho"

# Wacht op connecties (blocking)
conn, addr = s.accept()

# Er is een client verbonden met de server
print('#> Verbonden met ' + addr[0] + ':' + str(addr[1]))

# De server meldt zich aan de client
conn.sendall(b'#> Welkom Op Mijn Server\r\n')
conn.sendall(b'#> Username: ')
username_input = conn.recv(1024)
username_input = str(username_input.decode('ascii')).rstrip()
conn.sendall(b'#> Password: ')
Password_input = conn.recv(1024)
Password_input = str(Password_input.decode('ascii')).rsplit()

if Password_input == Password:
    conn.sendall(b'#> Welkom'+username_input+'')
elif Password_input != Password:
    conn.sendall(b'#> Optiefen gouw\r\n')
    quit()

# Wacht op input van de client en geef deze ook weer terug (echo service)
while 1 == 1:
    data = conn.recv(1024)
    data=str(data.decode('ascii')).rstrip() # # Remove \r | \n | \r\n
    print('#> Client data ontvangen:'+data+'.')
    conn.sendall(b'#> '+data.encode())
    conn.sendall(b'\r\n')
    if data == "stop":
        print('#> STOP commando ontvangen socket sluit')
        conn.sendall(b'#> STOP commando ontvangen tot ziens\r\n')
        sleep(2)
        conn.close()
        s.close()
        quit()
    if data == "calc":
        print('#> CALC commando ontvangen calculator opent')
        conn.sendall(b'#> CALC commando ontangen calculator opent\r\n')
        sleep(2)
        os.system("kcalc")
    if data == "notepad":
        print('#> notepad commando ontangen notepad opent')
        conn.sendall(b'#> Notepad commando ontvangen notepad opent\r\n')
        sleep(2)
        os.system("kwrite")
        
# Verbreek de verbinding en sluit de socket
conn.close()
s.close()