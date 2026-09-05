import requests
import matplotlib.pyplot as plt
import json
import os

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

# --- CONFIGURACIÓN ---
USUARIO = "apuromafo"
# La cookie se lee del '.env' (Personal Profile/.env). Suelen expirar cada 24h aprox.
SESSION_COOKIE = ENV.get("THM_CONNECT_SID", "")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Referer": f"https://tryhackme.com/p/{USUARIO}?tab=skills-matrix"
}

def fetch_free_rooms(exclude_windows=False):
    base_url = "https://tryhackme.com/api/v2/hacktivities/extended-search"
    free_rooms = []
    
    print("Obteniendo lista de salas gratuitas...")
    # Bajamos el rango a 5 páginas para evitar rate-limit o tardar demasiado, ajusta si necesitas más
    for page in range(1, 6):
        params = {
            "kind": "all",
            "difficulty": "all",
            "order": "relevance",
            "roomType": "all",
            "contentSubType": "free",
            "limit": 50,
            "page": page
        }
        
        response = requests.get(base_url, params=params, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            docs = data.get('data', {}).get('docs', [])
            if not docs: break
            
            for room in docs:
                if exclude_windows:
                    tags = [t['label'].lower() for t in room.get('tagDocs', [])]
                    if 'windows' not in tags:
                        free_rooms.append(room)
                else:
                    free_rooms.append(room)
        else:
            print(f"Error en página {page}: {response.status_code}")
            
    return free_rooms

def fetch_progress_data(room_codes):
    if not room_codes: return {}
    
    # La API prefiere comas normales, requests se encarga del encoding
    room_codes_str = ",".join(room_codes)
    url = f"https://tryhackme.com/api/v2/hacktivities/search-progress"
    
    cookies = {"connect.sid": SESSION_COOKIE}
    params = {"roomCodes": room_codes_str}
    
    print(f"Consultando progreso de {len(room_codes)} salas...")
    response = requests.get(url, params=params, headers=HEADERS, cookies=cookies)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener progreso: {response.status_code}")
        return {}

# --- EJECUCIÓN PRINCIPAL ---
exclude_windows = False
rooms = fetch_free_rooms(exclude_windows)
room_codes = [r['code'] for r in rooms]

# Fragmentamos la petición de progreso si son demasiadas salas (evita URL too long)
progress_list = []
batch_size = 30 
for i in range(0, len(room_codes), batch_size):
    batch = room_codes[i:i + batch_size]
    data = fetch_progress_data(batch)
    batch_progress = data.get('data', {}).get('roomProgress', [])
    progress_list.extend(batch_progress)

if not SESSION_COOKIE:
    print("No se encontró la cookie. Define THM_CONNECT_SID en 'Personal Profile/.env'.")
elif not progress_list:
    print("No se encontró información de progreso. Revisa tu cookie 'connect.sid' en 'Personal Profile/.env'.")
else:
    # Procesamiento de estadísticas
    total = len(progress_list)
    completed = sum(1 for r in progress_list if r['progressPercentage'] == 100)
    in_progress = sum(1 for r in progress_list if 0 < r['progressPercentage'] < 100)
    not_started = total - completed - in_progress

    # Gráfico
    labels = [f'Completado ({completed})', f'En Progreso ({in_progress})', f'Sin Empezar ({not_started})']
    sizes = [completed, in_progress, not_started]
    colors = ['#4caf50', '#ffeb3b', '#f44336']

    plt.figure(figsize=(10, 7))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title(f'Progreso de Salas Gratuitas de {USUARIO}')
    plt.axis('equal')
    
    plt.savefig('progreso_thm.png')
    print("Gráfico guardado como 'progreso_thm.png'")
    plt.show()

    # Guardar JSON
    with open('progress_data_sorted.json', 'w') as f:
        json.dump(progress_list, f, indent=4)