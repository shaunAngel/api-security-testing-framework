import requests
from datetime import datetime

# Use your own IP
BASE_URL = "http://192.168.185.129:5000"

report = []

# LOGIN
def login():
    print("[*] Logging in...")

    data = {
        "username": "user",
        "password": "password"
    }

    r = requests.post(f"{BASE_URL}/login", json=data)

    if r.status_code == 200:
        token = r.json()["token"]
        print("[+] Login successful")
        report.append("Login: SUCCESS")
        return token
    else:
        print("[-] Login failed")
        report.append("Login: FAILED")
        return None


# BOLA TEST
def test_bola(token):
    print("\n[*] Testing BOLA...")

    headers = {"Authorization": f"Bearer {token}"}
    vulnerable = False

    for i in range(1,5):
        url = f"{BASE_URL}/profile/{i}"
        r = requests.get(url, headers=headers)

        if r.status_code == 200:
            print(f"[!] Accessed user {i}")
            report.append(f"BOLA: Accessed user {i}")
            vulnerable = True
        else:
            print(f"[SAFE] User {i}")

    return vulnerable


# RATE LIMIT TEST
def test_rate_limit():
    print("\n[*] Testing Rate Limiting...")

    blocked = False

    for i in range(10):
        r = requests.get(f"{BASE_URL}/limited")

        if r.status_code == 429:
            print(f"[+] Blocked at request {i}")
            report.append(f"Rate Limit: Blocked at request {i}")
            blocked = True
            break
        else:
            print(f"[{i}] Allowed")

    return blocked


# AUTH TEST
def test_auth():
    print("\n[*] Testing Unauthorized Access...")

    r = requests.get(f"{BASE_URL}/users")

    if r.status_code == 401:
        print("[+] Protected endpoint secured")
        report.append("Auth: Protected endpoint secured")
        return True
    else:
        print("[!] Endpoint accessible without auth")
        report.append("Auth: Vulnerable (No protection)")
        return False


# REPORT OUTPUT
def save_report():
    filename = "report.txt"

    with open(filename, "w") as f:
        f.write("API SECURITY REPORT\n")
        f.write("="*30 + "\n")
        f.write(f"Target: {BASE_URL}\n")
        f.write(f"Date: {datetime.now()}\n\n")

        for line in report:
            f.write(line + "\n")

    print(f"\n[+] Report saved as {filename}")


# MAIN
def main():

    print("=== API SECURITY SCANNER ===\n")

    token = login()

    if not token:
        return

    bola = test_bola(token)
    rate = test_rate_limit()
    auth = test_auth()

    report.append("\n=== SUMMARY ===")
    report.append(f"BOLA: {'VULNERABLE' if bola else 'SAFE'}")
    report.append(f"Rate Limiting: {'ENFORCED' if rate else 'NOT IMPLEMENTED'}")
    report.append(f"Auth Protection: {'SECURE' if auth else 'WEAK'}")

    save_report()


if __name__ == "__main__":
    main()
