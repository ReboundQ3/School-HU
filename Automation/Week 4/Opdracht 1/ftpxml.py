import xml.etree.ElementTree as ET
import pprint

file = ET.parse('./network.xml')
root = file.getroot()
print("=============================================================================")

def print_clients():
    print("#> Clients:")
    clients = root.find('clients')
    for client in clients.findall('client'):
        name = client.find('name').text
        ip_address = client.find('ipAddress').text
        os = client.find('os').text
        print(f"#> Naam: {name} | IP-adres: {ip_address} | OS: {os}")
        
def print_servers():
    print("#> Servers")
    servers = root.find('servers')
    for server in servers.findall('server'):
        name = server.find('name').text
        ip_address = server.find('ipAddress').text
        os = server.find('os').text
        print(f"#> Naam: {name} | IP-adres: {ip_address} | OS: {os}")
        
print_clients()
print("=============================================================================")
print_servers()
print("=============================================================================")