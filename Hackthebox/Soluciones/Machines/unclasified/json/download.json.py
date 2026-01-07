import requests
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# --- CONFIGURACIÓN ---
TOKEN = "***TOKEN-ELIMINADO***"
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