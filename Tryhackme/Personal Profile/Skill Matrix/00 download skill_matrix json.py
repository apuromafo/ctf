import requests
import json
import os
import time

# --- CONFIGURACIÓN DE USUARIO ---
usuario = "apuromafo"  # Cambia este valor según necesites

# --- CONFIGURACIÓN DE SESIÓN ---
# Se recomienda usar Session para persistir cookies y headers
session = requests.Session()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def _load_env():
    env = {}
    for directory in (BASE_DIR, os.path.dirname(BASE_DIR)):
        path = os.path.join(directory, ".env")
        if not os.path.isfile(path):
            continue
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                env[key.strip()] = value.strip().strip('"').strip("'")
    return env

ENV = _load_env()

# Cookies mínimas necesarias para autenticación (se leen de 'Personal Profile/.env')
COOKIES=({
    'connect.sid': ENV.get("THM_CONNECT_SID", ""),
})

# Headers globales (el Referer se actualiza dinámicamente)
HEADERS=({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Referer": f"https://tryhackme.com/p/{usuario}?tab=skills-matrix"
})
# --- PARÁMETROS DE BÚSQUEDA ---
segments = ["entry", "junior", "mid", "senior"]
roles = ["Foundational", "Security Analyst", "Penetration Tester", "Security Engineer"]
base_folder = "json"

def fetch_all_skills():
    # Crear la carpeta principal 'json'
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)
        print(f"[*] Carpeta '{base_folder}' creada.")

    session = requests.Session()
    session.cookies.update(COOKIES)
    
    total_files = len(segments) * len(roles)
    count = 0

    print(f"{'SEGMENTO':<10} | {'ROLE':<20} | {'ESTADO':<10} | {'ARCHIVO'}")
    print("-" * 70)

    for segment in segments:
        for role in roles:
            count += 1
            params = {'role': role, 'segment': segment}
            url = "https://tryhackme.com/api/v2/users/skills"
            
            # Nombre de archivo limpio
            safe_role = role.replace(' ', '_').lower()
            filename = f"{segment}_{safe_role}.json"
            filepath = os.path.join(base_folder, filename)

            try:
                response = session.get(url, headers=HEADERS, params=params, timeout=10)
                
                if response.status_code == 200:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        json.dump(response.json(), f, indent=4)
                    status = "OK [200]"
                else:
                    status = f"ERROR [{response.status_code}]"
            except Exception as e:
                status = "EXCEPT"
                print(f"\n[!] Error crítico: {str(e)}")

            # Output detallado por cada request
            print(f"{segment:<10} | {role:<20} | {status:<10} | {filename}")
            
            # Anti-WAF delay
            time.sleep(0.7)

    print("-" * 70)
    print(f"[+] Finalizado. {count}/{total_files} archivos procesados en ./{base_folder}/")

if __name__ == "__main__":
    fetch_all_skills()