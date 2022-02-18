import requests
import json

def mullvad_get_keys(pubkey, token):
    r = requests.post("https://api.mullvad.net/app/v1/wireguard-keys", 
                     headers={'Authorization': 'Token ' + token, 'Content-Type': 'application/json'},
                     json={"pubkey": pubkey })    
    j = json.loads(r.text);
            
    return j