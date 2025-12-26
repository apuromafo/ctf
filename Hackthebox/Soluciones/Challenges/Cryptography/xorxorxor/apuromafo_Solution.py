import re

def extract_ciphertext(filename):
    """Paso 1: Leer el archivo y extraer la cadena hexadecimal."""
    try:
        with open(filename, 'r') as f:
            content = f.read()
        # Buscamos el patrón 'Flag: ' seguido de caracteres hexadecimales 
        match = re.search(r'Flag:\s*([0-9a-fA-F]+)', content)
        if match:
            hex_str = match.group(1)
            print(f"[+] Hexadecimal extraído: {hex_str[:20]}...")
            return bytes.fromhex(hex_str)
        else:
            raise ValueError("No se encontró el formato 'Flag: <hex>' en el archivo.")
    except FileNotFoundError:
        print(f"[-] Error: No se encontró el archivo {filename}")
        exit()

def recover_key(ciphertext, known_prefix):
    """Paso 2: Known Plaintext Attack (KPA)."""
    # Como la clave es de 4 bytes, hacemos XOR entre 
    # los primeros 4 bytes del cifrado y el prefijo conocido 'HTB{'
    key = bytes([ciphertext[i] ^ known_prefix[i] for i in range(len(known_prefix))])
    print(f"[+] Clave recuperada (XOR entre Ciphertext y '{known_prefix.decode()}'):")
    print(f"    Hex: {key.hex()} | Bytes: {key}")
    return key

def decrypt_data(ciphertext, key):
    """Paso 3: Desencriptación cíclica."""
    # Aplicamos la clave repetidamente usando el operador módulo % 
    decrypted = b""
    key_len = len(key)
    for i in range(len(ciphertext)):
        # ciphertext[i] XOR key[0, 1, 2, 3, 0, 1...]
        decrypted_byte = ciphertext[i] ^ key[i % key_len]
        decrypted += bytes([decrypted_byte])
    return decrypted

def main():
    print("--- Iniciando Proceso de Desencriptación ---")
    
    # 1. Obtener datos
    encrypted_bytes = extract_ciphertext('output.txt')
    
    # 2. Definir lo que sabemos (Known Plaintext)
    # Sabemos que el flag de HTB siempre empieza así:
    prefix = b"HTB{" 
    
    # 3. Romper la clave
    recovered_key = recover_key(encrypted_bytes, prefix)
    
    # 4. Obtener el resultado final
    final_flag = decrypt_data(encrypted_bytes, recovered_key)
    
    print("\n" + "="*40)
    print(f"RESULTADO: {final_flag.decode()}")
    print("="*40)

if __name__ == "__main__":
    main()