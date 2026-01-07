import os
import shutil
import re

def organize_existing_mds():
    # Directorio donde están tus archivos actuales (puedes cambiarlo a '.' si es la carpeta actual)
    source_dir = "." 
    
    # Buscamos archivos que empiecen con números (ej: 01_RASTA.md)
    files = [f for f in os.listdir(source_dir) if f.endswith('.md') and re.match(r'^\d+_', f)]

    if not files:
        print("❌ No se encontraron archivos .md numerados para organizar.")
        return

    for file_name in files:
        # Extraemos el nombre sin la extensión .md para la carpeta (ej: 01_RASTA)
        folder_name = os.path.splitext(file_name)[0]
        new_folder_path = os.path.join(source_dir, folder_name)

        # 1. Crear la carpeta si no existe
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
            print(f"📁 Carpeta creada: {folder_name}")

        # 2. Definir la ruta de destino (puedes dejar el nombre original o cambiarlo a README.md)
        old_path = os.path.join(source_dir, file_name)
        new_path = os.path.join(new_folder_path, file_name)

        # 3. Mover el archivo
        try:
            shutil.move(old_path, new_path)
            print(f"➡️  Movido: {file_name} -> {folder_name}/")
        except Exception as e:
            print(f"⚠️  Error moviendo {file_name}: {e}")

    print(f"\n✅ Organización completada. Se procesaron {len(files)} archivos.")

if __name__ == "__main__":
    organize_existing_mds()