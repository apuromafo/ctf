import os
import json

def normalizar_scores(directorio):
    # Listar todos los archivos JSON en la carpeta
    archivos = [f for f in os.listdir(directorio) if f.endswith('.json')]
    
    if not archivos:
        print(f"No se encontraron archivos JSON en: {directorio}")
        return

    for nombre_archivo in archivos:
        ruta_completa = os.path.join(directorio, nombre_archivo)
        
        try:
            with open(ruta_completa, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Procesar las habilidades y subir el score a 100
            if "data" in data and "skills" in data["data"]:
                for skill in data["data"]["skills"]:
                    if isinstance(skill.get("score"), (int, float)):
                        if skill["score"] < 100:
                            skill["score"] = 100
                
                # Guardar el archivo modificado
                with open(ruta_completa, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                
                print(f"✅ Procesado con éxito: {nombre_archivo}")
            
        except Exception as e:
            print(f"❌ Error procesando {nombre_archivo}: {e}")

# Instrucción de uso: 
# Cambia '.' por la ruta de tu carpeta si no están en el mismo lugar que el script
normalizar_scores('.')