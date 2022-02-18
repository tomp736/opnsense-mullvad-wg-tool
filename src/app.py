import utils
import mullvad_api
import opnsense_api_wireguard

def add_wg_mullvad(relay_name):
    
    print ("Configuring Mullvad Relay using " + relay_name + " :) Hang on!")
    
    # read relays file
    mullvad_relays = utils.mullvad_get_relays()

    relayFound = False
    
    # load relay
    for relay_data in mullvad_relays:
        if relay_data["hostname"] == relay_name:
            mullvad_relay = relay_data
            relayFound = True


    if relayFound == False:
        print ("Relay " + relay_name + " does not exist. Nothing will not be configured.")
        return
    
    mv_hostname = mullvad_relay["hostname"].replace("-","")
    mv_pubkey = mullvad_relay["pubkey"]
    mv_ipv4 = mullvad_relay["ipv4_addr_in"]
    mv_port = mullvad_relay["multihop_port"]
    mv_keepalive = "25"

    # print (mullvad_relay)

    response_wg_servers = opnsense_api_wireguard.wireguard_get_servers()
    response_wg_clients = opnsense_api_wireguard.wireguard_get_clients()

    server_exists = False
    client_exists = False

    for response_wg_server in response_wg_servers:
        if response_wg_server["name"] == mv_hostname:
            wg_server_uuid = response_wg_server["uuid"]
            wg_server = opnsense_api_wireguard.wireguard_get_server(wg_server_uuid)
            server_exists = True
            print ("Existing server using " + mv_hostname + " already exists, updating existing.")
            
    for response_wg_client in response_wg_clients:
        if response_wg_client["name"] == mv_hostname:
            wg_client_uuid = response_wg_client["uuid"]
            wg_client = opnsense_api_wireguard.wireguard_get_client(wg_client_uuid)
            client_exists = True
            print ("Existing client using " + mv_hostname + " already exists, updating existing.")
            
    if server_exists == False:
        wg_server = opnsense_api_wireguard.wireguard_server_model()
        wg_server["server"]["name"] = mv_hostname
        wg_server_uuid = opnsense_api_wireguard.wireguard_save_server('', wg_server)
        wg_server = opnsense_api_wireguard.wireguard_get_server(wg_server_uuid)
    
    if client_exists == False:
        wg_client = opnsense_api_wireguard.wireguard_client_model()
        wg_client["client"]["name"] = mv_hostname 
        wg_client["client"]["pubkey"] = mv_pubkey
        wg_client["client"]["tunneladdress"] = "0.0.0.0/0"
        wg_client_uuid = opnsense_api_wireguard.wireguard_save_client('', wg_client)
        wg_client = opnsense_api_wireguard.wireguard_get_client(wg_client_uuid)
            
    serverpubkey = wg_server["server"]["pubkey"].strip()
    keys = mullvad_api.mullvad_get_keys(serverpubkey, utils.mullvad_token())
    
    wg_client["client"]["pubkey"] = mv_pubkey
    wg_client["client"]["serveraddress"] = mv_ipv4
    wg_client["client"]["serverport"] = mv_port
    wg_client["client"]["keepalive"] = mv_keepalive   
    opnsense_api_wireguard.wireguard_save_client(wg_client_uuid, wg_client);

    wg_server["server"]["tunneladdress"] = keys["ipv4_address"]
    wg_server["server"]["port"] = 51820 + int(wg_server["server"]["instance"])
    wg_server["server"]["gateway"] = utils.getGatewayAddress(keys["ipv4_address"])
    wg_server["server"]["peers"] = wg_client_uuid
    opnsense_api_wireguard.wireguard_save_server(wg_server_uuid, wg_server);
    
    print()