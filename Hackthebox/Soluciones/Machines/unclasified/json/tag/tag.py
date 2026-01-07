import requests
import json
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# --- CONFIGURACIÓN ---
TOKEN = "***TOKEN-ELIMINADO***"
OUTPUT_DIR = "htb_tags_dump"
MAX_THREADS = 15  # Balanceado para un rango corto de 100
RANGE_START = 1
RANGE_END = 3000

# Headers extraídos de tu CURL
HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "es-419,es;q=0.9,es-US;q=0.8",
    "authorization": f"Bearer {TOKEN}",
    "origin": "https://app.hackthebox.com",
    "priority": "u=1, i",
    "referer": "https://app.hackthebox.com/",
    "sec-ch-ua": '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
}

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def pwn_tags(machine_id):
    url = f"https://labs.hackthebox.com/api/v4/machine/tags/{machine_id}"
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        
        # Guardar respuesta completa
        try:
            content = response.json()
        except:
            content = {"raw_error": response.text}

        result = {
            "id": machine_id,
            "status": response.status_code,
            "data": content,
            "url": url
        }
        
        file_path = os.path.join(OUTPUT_DIR, f"tag_{machine_id}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4, ensure_ascii=False)
            
        return machine_id, response.status_code
    except Exception as e:
        return machine_id, str(e)

def run_brute():
    print(f"[*] Iniciando volcado de TAGS en ./{OUTPUT_DIR}")
    print(f"[*] Rango: {RANGE_START} - {RANGE_END}")
    
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = {executor.submit(pwn_tags, i): i for i in range(RANGE_START, RANGE_END + 1)}
        
        for future in as_completed(futures):
            m_id, status = future.result()
            if status == 200:
                print(f"[+] ID {m_id:3} | Status {status} | JSON Guardado", end="\r")
            else:
                print(f"\n[-] ID {m_id:3} | Status {status}")

if __name__ == "__main__":
    run_brute()
    print(f"\n\n[V] Finalizado. Los 100 archivos están en la carpeta '{OUTPUT_DIR}'.")