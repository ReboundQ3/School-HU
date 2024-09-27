import xml.etree.ElementTree as ET
from ftplib import FTP

# Functie om configuratie te laden uit XML-bestand
tree = ET.parse("ftp_config.xml")
root = tree.getroot()
    
# Server-informatie
server = root.find('server/ftpServer').text,
username = root.find('server/username').text,
password = root.find('server/password').text,
port = int(root.find('options/port').text),
  
print(root.find('server/ftpServer').text)
print(root.find('server/username').text)
print(root.find('server/password').text)
print(root.find('options/port').text)

FTP.connect(host=server, port=port)
FTP.login(user=username, passwd=password)
FTP.retrlines('LIST')

with open ('README', 'wb') as file:
    FTP.retrbinary('RETR README', file.write)
FTP.quit()