'''
Reto: HTB{08FU5C473D_4ND_UNKN0WN}
Descripción: Modificación de memoria cifrada.
Origen: https://www.kn0sky.com/?p=6d09d68d-54b7-4d59-804f-24a5b6aa39b8
'''

def decode(val: int) -> int:
    """
    Simula la función decode de C++:
    1. Desplaza 'val' 9 bits a la izquierda y trunca a 32 bits.
    2. Convierte a 64 bits y desplaza otros 32 bits a la izquierda.
    3. Divide por la clave (key) y devuelve el cociente entero.
    """
    # Simulación de instrucción _shlx_u32 (desplazamiento lógico)
    tmp = (val << 9) & 0xFFFFFFFF  
    key = 0x6208CECB
    
    # Eleva el valor a rango de 64 bits para la división
    tmp = tmp << 32               
    
    # División de entero largo (común en algoritmos de dispersión/hashing)
    tmp //= key                   
    return tmp


# -------- Bloque Principal (Main) --------
if __name__ == "__main__":
    val = 0x248F
    key = 0x6208CECB

    # --- 1. Multiplicación de precisión extendida ---
    # En ensamblador, mul eax devuelve el resultado en EDX:EAX (64 bits)
    full_prod = (val & 0xFFFFFFFF) * (key & 0xFFFFFFFF)
    
    result_lo = full_prod & 0xFFFFFFFF         # Parte baja (EAX)
    result_hi = (full_prod >> 32) & 0xFFFFFFFF # Parte alta (EDX)

    print(f"Resultado Multiplicación -> HI: {result_hi:X}, LO: {result_lo:X}")

    # --- 2. Simulación de instrucción _sarx_i32 ---
    # SARX es un desplazamiento aritmético a la derecha (preserva el signo).
    # Convertimos el valor hexadecimal a un entero con signo de 32 bits.
    if result_hi < 0x80000000:
        signed_hi = result_hi
    else:
        signed_hi = result_hi - 0x100000000
    
    # Desplazamiento aritmético de 9 bits
    res = signed_hi >> 9
    
    # Aplicamos máscara para volver a ver el resultado como un registro de 32 bits
    print(f"Resultado SARX (HI >> 9): {res & 0xFFFFFFFF:X}")

    # --- 3. Ejecución de decode ---
    inp = decode(19)
    print(f"Resultado de decode(19): {inp:X}")