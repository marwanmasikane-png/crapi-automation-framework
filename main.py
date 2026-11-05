import json
import requests
# Kuagiza vipande vyetu vya udukuzi kutoka kwenye folder la modules
from modules.bola import run_bola
from modules.broken_auth import run_broken_auth
from modules.ssrf import run_ssrf

def login_to_crapi(base_url):
    """Kazi ya hii function ni kupata Token ya JWT ili script nyingine zitumie"""
    login_url = f"{base_url}/identity/api/auth/login"
    login_data = {"email": "marwan_test@example.com", "password": "Password123!"}
    
    try:
        response = requests.post(login_url, json=login_data)
        if response.status_code == 200:
            return response.json().get("token")
    except Exception as e:
        print(f"[-] Imeshindwa kuunganisha na crAPI Seva: {e}")
    return None

if __name__ == "__main__":
    print("=== CRAPI AUTOMATION SECURITY TESTING FRAMEWORK ===")
    
    # 1. Soma anuani kutoka kwenye config.json
    with open("config.json") as f:
        config = json.load(f)
    CRAPI_URL = config["base_url"]
    
    # 2. Pata token ya ulinzi kabla ya kuanza mashambulizi
    token = login_to_crapi(CRAPI_URL)
    
    if not token:
        print("[-] Login Imefeli! Hakikisha mtumiaji yupo na crAPI inarun.")
    else:
        print("[+] Login Imefanikiwa! Token Imezalishwa.")
        
        # 3. KUWASHA MAJARIBIO YA KIOTOMATIKI (AUTOMATION)
        run_bola(CRAPI_URL, token)
        run_ssrf(CRAPI_URL, token)
        run_broken_auth(CRAPI_URL)
        
        print("\n=== UTARATIBU WA MAJARIBIO UMEMALIZIKA ===")
