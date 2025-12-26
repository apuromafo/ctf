#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def decryption_with_stats(msg_bytes):
    pt = []
    # Encabezado con anchos fijos: < es izquierda, ^ es centrado
    header = f"{'IDX':^5} | {'HEX':^6} | {'DEC':^5} | {'ECUACIÓN (paso a paso)':^32} | {'RES':^5} | {'CHAR':^5}"
    print(header)
    print("-" * len(header))

    for i, char in enumerate(msg_bytes):
        # Operación
        transformed = ((char - 18) * 179) % 256
        pt.append(transformed)
        
        if i < 20: # Mostramos los primeros 20 para validar el flag
            c_in = f"0x{char:02x}"  # Hexadecimal con 2 dígitos (ej: 0x0a)
            d_in = f"{char:3}"      # Decimal con 3 espacios
            
            # Formateamos la ecuación para que siempre ocupe el mismo espacio
            eq_str = f"({char:3} - 18) * 179 % 256"
            res_val = f"{transformed:3}"
            
            # Carácter imprimible
            char_display = chr(transformed) if 32 <= transformed <= 126 else '·'
            
            print(f"{i:^5} | {c_in:^6} | {d_in:^5} | {eq_str:^32} | {res_val:^5} | {char_display:^5}")
        elif i == 20:
            print(f"{'...':^75}")

    return bytes(pt)

def main():
    try:
        with open('msg.enc', 'r') as f:
            ct = bytes.fromhex(f.read().strip())
        
        print(f"\n[+] Datos cargados. Iniciando análisis de transformación:\n")
        pt_bytes = decryption_with_stats(ct)
        
        print("\n" + "="*60)
        print("DECODED:")
        print("-" * 60)
        print(pt_bytes.decode('utf-8', errors='replace'))
        print("="*60 + "\n")
            
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    main()