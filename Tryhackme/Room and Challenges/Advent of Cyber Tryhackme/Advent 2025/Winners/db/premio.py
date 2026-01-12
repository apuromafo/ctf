import json

def generar_archivo_ordenado(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    winners = data['data']['winners']

    # Función para normalizar el premio para el ordenamiento
    # Si un usuario tiene varios premios, usamos el primero de su lista para ordenar
    def get_main_prize(winner):
        return winner['prizes'][0]['prizeName'] if winner['prizes'] else "Z-No Prize"

    # Ordenar la lista: Primero por premio, luego por nombre de usuario
    winners_sorted = sorted(winners, key=lambda x: (get_main_prize(x), x['username'].lower()))

    with open(output_file, 'w', encoding='utf-8') as md:
        md.write("# 🏆 Lista de Ganadores AOC 2025\n")
        md.write(f"Total de registros: **{len(winners_sorted)}**\n\n")
        md.write("| Foto | Usuario | Premio(s) |\n")
        md.write("| :---: | :--- | :--- |\n")

        for w in winners_sorted:
            alias = w.get('username', 'N/A')
            avatar = w.get('avatar', '')
            prizes = ", ".join([p['prizeName'] for p in w.get('prizes', [])])
            
            # Formato de imagen pequeña para no romper la estética de la tabla
            img = f'<img src="{avatar}" width="35" height="35" style="border-radius:50%">'
            md.write(f"| {img} | **{alias}** | {prizes} |\n")

    return len(winners_sorted)

# Ejecución
total = generar_archivo_ordenado('winners.json', 'ganadores_ordenados.md')
print(f"Procesados {total} ganadores en 'ganadores_ordenados.md'")