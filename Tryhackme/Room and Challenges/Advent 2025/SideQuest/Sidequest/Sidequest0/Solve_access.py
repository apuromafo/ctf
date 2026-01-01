import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256

def pwn_hopper_vault(encrypted_str, password):
    # 1. Decodificar Base64
    try:
        raw_data = base64.b64decode(encrypted_str)
    except Exception as e:
        return f"Error decodificando Base64: {e}"

    # 2. Segmentación de bytes (según el JS proporcionado)
    # r = n.slice(0, 16)  -> SALT
    # l = n.slice(16, 28) -> IV (12 bytes para AES-GCM)
    # u = n.slice(28, 44) -> TAG (16 bytes)
    # o = n.slice(44)     -> CIPHERTEXT
    
    salt = raw_data[0:16]
    iv = raw_data[16:28]
    tag = raw_data[28:44]
    ciphertext = raw_data[44:]

    print(f"[*] Datos extraídos:")
    print(f"    - Salt: {salt.hex()}")
    print(f"    - IV:   {iv.hex()}")
    print(f"    - Tag:  {tag.hex()}")
    print(f"    - Longitud Ciphertext: {len(ciphertext)} bytes")

    # 3. Derivación de la clave (PBKDF2)
    # La Web Crypto API suele usar 100,000 iteraciones por defecto para AES-256
    print(f"[*] Derivando clave con PBKDF2...")
    
    key = PBKDF2(
        password.encode('utf-8'), 
        salt, 
        dkLen=32,          # 32 bytes para AES-256
        count=100000,      # Iteraciones estándar
        hmac_hash_module=SHA256
    )

    # 4. Desencriptación AES-GCM
    try:
        cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
        # decrypt_and_verify espera el tag por separado
        decrypted_bytes = cipher.decrypt_and_verify(ciphertext, tag)
        return decrypted_bytes.decode('utf-8')
    except ValueError as e:
        return f"[!] Error de autenticación: Contraseña incorrecta o parámetros de derivación fallidos. ({e})"
    except Exception as e:
        return f"[!] Error inesperado: {e}"

# --- EJECUCIÓN ---
target_data = "hlRAqw3zFxnrgUw1GZusk+whhQHE0F+g7YjWjoJvpZRSCoDzehjXsEX1wQ6TTlOPyEJ/k+AEiMOxdqywh/86AOmhTaXNyZAvbHUVjfMdTqdzxmLXZJwI5ynI"  #from  https://assets.tryhackme.com/additional/aoc2025/files/hopper-origins.txt   
invitation_code = "THM{There.is.no.EASTmas.without.Hopper}"#from Sidequest 1, when send the 3 flags with have some "THM{flag}"

print(f"[*] decoding.")
resultado = pwn_hopper_vault(target_data, invitation_code)

print("-" * 50)
print("RESULTADO:")
print(resultado)
print("-" * 50)