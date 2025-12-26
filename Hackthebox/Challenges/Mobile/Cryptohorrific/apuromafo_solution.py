import os
import re
import base64
import math
from Crypto.Cipher import AES
# No usaremos la función unpad directa para hacerlo manual y explícito en el print

def solve():
    # --- VALORES DEL TUTORIAL ---
    AES_KEY = b"!A%D*G-KaPdSgVkY" 
    # El IV que mencionaste, aunque en ECB no se usa para el cálculo, lo mostramos:
    IV_VAL = b"QfTjWnZq4t7w!z%C" 

    print("=== CONFIGURACIÓN EXTRAÍDA ===")
    print(f"[*] KEY (Clave): {AES_KEY.decode()}")
    print(f"[*] IV (Vector):  {IV_VAL.decode()}")
    print(f"[*] Modo:         AES-128-ECB")

    # 1. Localización
    target = "challenge.plist"
    path = None
    for root, _, files in os.walk("."):
        if target in files:
            path = os.path.join(root, target)
            break
    
    if not path: return

    # 2. Extracción (con corrección de offset para bplist)
    with open(path, "rb") as f:
        content = f.read()
    
    match = re.search(rb'([A-Za-z0-9+/=]{40,})', content)
    if not match: return

    # Forzamos la limpieza del offset 1 (la 'X' intrusa)
    b64_raw = match.group(1).decode()
    ciphertext_b64 = b64_raw[1:] if len(b64_raw) % 4 != 0 else b64_raw
    encrypted_data = base64.b64decode(ciphertext_b64)

    print("\n=== PROCESO DE DESENCRIPTACIÓN Y PADDING ===")
    cipher = AES.new(AES_KEY, AES.MODE_ECB)
    
    # PASO A: Desencriptación bruta (incluye el padding)
    raw_decrypted = cipher.decrypt(encrypted_data)
    
    print(f"[*] 1. Datos desencriptados (con padding):")
    print(f"    Bytes: {raw_decrypted}")
    
    # EXPLICACIÓN DEL PADDING PKCS7:
    # Si el último byte es 0x05, significa que hay 5 bytes de relleno con el valor 0x05.
    padding_len = raw_decrypted[-1]
    padding_bytes = raw_decrypted[-padding_len:]
    
    print(f"[*] 2. Análisis de Padding detectado:")
    print(f"    - Último byte: {hex(padding_len)} (Indica que hay {padding_len} bytes de relleno)")
    print(f"    - Bytes de relleno: {padding_bytes}")

    # PASO B: Eliminación manual del padding
    flag = raw_decrypted[:-padding_len]
    
    print(f"[*] 3. Datos finales (Padding eliminado):")
    print(f"    Bytes: {flag}")

    print("\n" + "="*60)
    print(f"FLAG FINAL: {flag.decode()}")
    print("="*60)

if __name__ == "__main__":
    solve()