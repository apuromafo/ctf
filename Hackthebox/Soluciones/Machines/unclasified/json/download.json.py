import requests
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# --- CONFIGURACIÓN ---
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI2IiwianRpIjoiZmFlNmQxOTQwMDAwY2ExYzIzOGYxMzdmNTg5Yjg5OWE1NmQ0OGJlMjhjN2EzMGE1NWU3NDEwYjExNzExY2VhNmVhZTEzZGZhZDI4ZjBhMDYiLCJpYXQiOjE3NjY3ODY1MzguOTg5NzI1LCJuYmYiOjE3NjY3ODY1MzguOTg5NzI3LCJleHAiOjE3NjcwNDU3MzguOTgwMywic3ViIjoiMjcxNjQ0Iiwic2NvcGVzIjpbXX0.lUh90soImZ8HXCD4iOaYGkGldX9RIj0XpKZI5fwufha-X_3E-5WEbpGWZu1MpIfRpyWNP-VfRvo8Ny3YfIBN90q7ow-cAvi0D1wKCmPfpwSNDqiYb23_tajVb9xSVwCuBqeRbbfUJIYdnV-BHfICEJacuKlhShm4P0yQ6CT6m-1GiXbXdRT7h_LNUVigHpMHK62y8dpjrUi4wpPhDfBuYwSjqyWKcPbSdeVG1bKYhq0k6ilMrPEV-rVM-8reopjB5Xso0LnlqsZFUuN-27HKoSJaQC520OodndriqT4vvCMHkv1v0Y_XQTUZEvXojXsPre1-wd1BAUHKjveD-j_DIZ0rV1wHMZhlnex6IyF3idZrlmgqjxIOp_KD3EhPl75vIZqN50tgVtJGAz_YImjeV07ndjBB8-v_cSUc5zKk6TtvMk8dljuEAB3LASX241a8C6cGRDz0x6QWA0FPlUAbWtRn0DkzlMRegBjWJUVYZj9KkCgNgCGzLS43eW0M7CEQaQexEIiXavB6GpOpVxdG1pRwtPm5z7esbs_GLu3V9mbbd5tcy6knrt40s276VFQ-HeqSN2KhIwoSxEJjz2dZ2pEBdaQpeEAM18VQy9VaV2z_iB28SD3xZfNoTAzlvpEl1PuJNN2PQj8mSyMk_IkgZhpHn9TON4QHVmfNaDEzkVk"
OUTPUT_DIR = "htb_responses"
MAX_THREADS = 20  # Ajusta según tu conexión y el rate limit de HTB
RANGE_START = 1
RANGE_END = 3000

# Crear directorio si no existe
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Authorization": f"Bearer {TOKEN}",
    "Origin": "https://app.hackthebox.com",
    "Referer": "https://app.hackthebox.com/",
    "Sec-Ch-Ua-Platform": '"Windows"'
}

def fetch_machine_task(machine_id):
    url = f"https://labs.hackthebox.com/api/v4/machines/{machine_id}/tasks"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        # Guardamos la respuesta independientemente del código para análisis posterior
        result = {
            "id": machine_id,
            "status_code": response.status_code,
            "content": response.json() if response.status_code == 200 else str(response.text)
        }
        
        # Nombre de archivo individual por ID
        file_path = os.path.join(OUTPUT_DIR, f"machine_{machine_id}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4)
            
        return machine_id, response.status_code
    except Exception as e:
        return machine_id, f"Error: {str(e)}"

def run_pwn():
    print(f"[*] Iniciando escaneo multihilo ({MAX_THREADS} hilos)...")
    print(f"[*] Guardando resultados en: ./{OUTPUT_DIR}/")
    
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        # Mapeo de tareas
        futures = {executor.submit(fetch_machine_task, i): i for i in range(RANGE_START, RANGE_END + 1)}
        
        for future in as_completed(futures):
            m_id, status = future.result()
            if status == 200:
                print(f"[+] Machine {m_id:4}: OK (Guardado)")
            else:
                # Solo imprimimos errores críticos o códigos no comunes para no ensuciar la pantalla
                if status != 404:
                    print(f"[-] Machine {m_id:4}: Status {status}")

if __name__ == "__main__":
    run_pwn()