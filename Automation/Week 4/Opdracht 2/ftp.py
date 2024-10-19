import xml.etree.ElementTree as ET
from ftplib import FTP
import ftplib

# Functie om configuratie te laden uit XML-bestand
tree = ET.parse("ftp_config.xml")
root = tree.getroot()
filename = "readme.txt"
    
# Server-informatie
xml_server = (root.find('server/ftpServer').text)
xml_username = (root.find('server/username').text)
xml_password = (root.find('server/password').text)
  
server = xml_server.strip()
username = xml_username.strip()
password = xml_password.strip()

print(server, username, password)

try:
    ftp = FTP(host=server)
    ftp.login(user=username,passwd=password)
    ftp.retrlines('LIST')
    with open(filename, "wb") as file:
        ftp.retrbinary(f"RETR {filename}", file.write)
        print("#> Readme.txt gedownload")
except ftplib.error_perm as error:
    print(error)