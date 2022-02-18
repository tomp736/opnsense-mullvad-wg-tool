import configparser
import json
import ipaddress

def mullvad_token():
    configParser = configparser.RawConfigParser() 
    configParser.read(r'/etc/opnsense/apikey.txt')
    return configParser.get('mullvad', 'token')
    
def mullvad_get_relays():
    f = open(r"mullvad_relays.json")
    relays_data = json.load(f);
    return relays_data

def opnsense_get_auth():
    configParser = configparser.RawConfigParser() 
    configParser.read(r'/etc/opnsense/apikey.txt')
    api_key = configParser.get('opnsense', 'key')
    api_secret = configParser.get('opnsense', 'secret')
    return (api_key, api_secret)

def opnsense_get_url(apiPath):
    configParser = configparser.RawConfigParser() 
    configParser.read(r'/etc/opnsense/apikey.txt')
    hostname = configParser.get('opnsense', 'hostname')
    return hostname + apiPath

def getGatewayAddress(tunneladdress):
    a = ipaddress.ip_network(tunneladdress);    
    return str(ipaddress.IPv4Address(str(a.network_address)) - 1)