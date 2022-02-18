# import libraries
import json
import requests
import utils

def wireguard_client_model():    
    return {
        "client":
            {
                "enabled":"1",
                "name":"",
                "pubkey":"",
                "psk":"",
                "tunneladdress":"",
                "serveraddress":"",
                "serverport":"",
                "keepalive":""
            }
        }
    
def wireguard_get_clients():
    uri = utils.opnsense_get_url("/api/wireguard/client/searchClient")
    auth = utils.opnsense_get_auth()
    r = requests.get(uri, verify=False, auth=auth)
    if r.status_code == 200:
        response = json.loads(r.text)
        return response['rows']
    else:
        print ('Connection / Authentication issue, response received:')
        print (r.text)
        
def wireguard_get_client(uuid):
    uri = utils.opnsense_get_url("/api/wireguard/client/getClient/" + uuid)
    auth = utils.opnsense_get_auth()
    r = requests.get(uri, verify=False, auth=auth)
    if r.status_code == 200:
        response = json.loads(r.text)
        return response
    else:
        print ('Connection / Authentication issue, response received:')
        print (r.text)
    
def wireguard_save_client(uuid, wg_client):    
    if uuid == '':
        print ("Adding WG Client")
        uri = utils.opnsense_get_url("/api/wireguard/client/addClient/")
    else:
        print ("Updating WG Client")
        uri = utils.opnsense_get_url("/api/wireguard/client/setClient/" + uuid)
    auth = utils.opnsense_get_auth()
    
    if isinstance(wg_client["client"]["tunneladdress"], dict):
        wg_client["client"]["tunneladdress"] = list(wg_client["client"]["tunneladdress"].keys())[0]
            
    r = requests.post(uri, 
        verify=False, 
        auth=auth, 
        json= 
            {
            "client":
                {
                    "enabled": wg_client["client"]["enabled"],
                    "name": wg_client["client"]["name"],
                    "pubkey": wg_client["client"]["pubkey"],
                    "psk": wg_client["client"]["psk"],
                    "tunneladdress": wg_client["client"]["tunneladdress"],
                    "serveraddress": wg_client["client"]["serveraddress"],
                    "serverport": wg_client["client"]["serverport"],
                    "keepalive": wg_client["client"]["keepalive"]
                }
            }        
        )
        
    if r.status_code == 200:
        response = json.loads(r.text)
        if response['result'] == 'saved':
            if uuid == '':
                print ('Wireguard client created :)')                
                return response['uuid']
            else:
                print ('Wireguard client saved :)')
                return uuid
        else:
            print ('Error adding wireguard client')
    else:
        print ('Connection / Authentication issue, response received:')
        print (r.text)
    
def wireguard_del_client(uuid):
    uri = utils.opnsense_get_url("/api/wireguard/client/delClient/" + uuid)
    auth = utils.opnsense_get_auth()
    r = requests.post(uri,verify=False,auth=auth,json= {})

def wireguard_get_servers():
    uri = utils.opnsense_get_url("/api/wireguard/server/searchServer")
    auth = utils.opnsense_get_auth()
    r = requests.get(uri,verify=False,auth=auth)
    if r.status_code == 200:
        response = json.loads(r.text)
        return response['rows']
    else:
        print ('Connection / Authentication issue, response received:')
        print (r.text)
    
def wireguard_get_server(uuid):
    uri = utils.opnsense_get_url("/api/wireguard/server/getServer/" + uuid)
    auth = utils.opnsense_get_auth()
    r = requests.get(uri,verify=False,auth=auth)
    if r.status_code == 200:
        response = json.loads(r.text)
        return response
    else:
        print ('Connection / Authentication issue, response received:')
        print (r.text)
    
def wireguard_server_model():    
    return {
        "server":
            {
                "enabled":"1",
                "name":"",
                "pubkey":"",
                "privkey":"",
                "port":"",
                "mtu":"",
                "dns":"",
                "tunneladdress":"",
                "peers":"",
                "disableroutes":"0",
                "gateway":""
                }
            }
        
def wireguard_save_server(uuid, wg_server):
    if uuid == '':
        print ("Adding WG Server")
        uri = utils.opnsense_get_url("/api/wireguard/server/addServer/")
    else:
        print ("Updating WG Server")
        uri = utils.opnsense_get_url("/api/wireguard/server/setServer/" + uuid)     
           
    auth = utils.opnsense_get_auth()
    
    if isinstance(wg_server["server"]["dns"], list):
        wg_server["server"]["dns"] = ''
        
    if isinstance(wg_server["server"]["peers"], dict):
        wg_server["server"]["peers"] = list(wg_server["server"]["peers"].keys())[0]
        
    if isinstance(wg_server["server"]["tunneladdress"], dict):
        wg_server["server"]["tunneladdress"] = list(wg_server["server"]["tunneladdress"].keys())[0]
    
    r = requests.post(uri, verify=False, auth=auth, json= 
        {
            "server":
            {
                "enabled": wg_server["server"]["enabled"],
                "name": wg_server["server"]["name"],
                "pubkey": wg_server["server"]["pubkey"],
                "privkey": wg_server["server"]["privkey"],
                "port": wg_server["server"]["port"],
                "mtu": wg_server["server"]["mtu"],
                "dns": wg_server["server"]["dns"],
                "tunneladdress": wg_server["server"]["tunneladdress"],
                "peers": wg_server["server"]["peers"],
                "disableroutes": wg_server["server"]["disableroutes"],
                "gateway": wg_server["server"]["gateway"]
            }
        }
    )
    
    if r.status_code == 200:
        response = json.loads(r.text)
        if response['result'] == 'saved':
            if uuid == '':
                print ('Wireguard server created :)')                
                return response['uuid']
            else:
                print ('Wireguard server saved :)')
                return uuid
            print ('Error adding wireguard server')
    else:
        print ('Connection / Authentication issue, response received:')
        print (r.text)

    
def wireguard_del_server(uuid):
    uri = utils.opnsense_get_url("/api/wireguard/server/delServer/" + uuid)
    auth = utils.opnsense_get_auth()
    r = requests.post(uri,verify=False,auth=auth,json= {})
    print (r.text)
    

    





        
    
    
