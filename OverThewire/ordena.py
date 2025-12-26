import os
import shutil

def organizar_laboratorio():
    base_path = "." # Directorio actual
    target_online = os.path.join(base_path, "Online")
    
    # Mapeo de carpetas actuales a su destino correcto en Online
    # Esto corrige minúsculas a la estructura del script anterior
    carpetas_a_mover = {
        "bandit": "Bandit",
        "krypton": "Krypton",
        "leviathan": "Leviathan",
        "narnia": "Narnia",
        "natas": "Natas",
        "vortex": "Vortex"
    }

    print("--- Organizando directorios existentes hacia 'Online' ---")

    for actual, destino_nombre in carpetas_a_mover.items():
        ruta_actual = os.path.join(base_path, actual)
        ruta_destino = os.path.join(target_online, destino_nombre)

        if os.path.exists(ruta_actual):
            try:
                # Si la carpeta destino ya existe (creada por el script anterior)
                # movemos el contenido, si no, renombramos/movemos la carpeta
                if os.path.exists(ruta_destino):
                    print(f"[*] Fusionando contenido: {actual} -> {ruta_destino}")
                    for item in os.listdir(ruta_actual):
                        s = os.path.join(ruta_actual, item)
                        d = os.path.join(ruta_destino, item)
                        shutil.move(s, d)
                    os.rmdir(ruta_actual)
                else:
                    shutil.move(ruta_actual, ruta_destino)
                    print(f"[+] Movido: {actual} -> {ruta_destino}")
            except Exception as e:
                print(f"[!] Error moviendo {actual}: {e}")
        else:
            print(f"[?] No se encontró la carpeta: {actual}")

    print("--- Organización completada ---")

if __name__ == "__main__":
    organizar_laboratorio()