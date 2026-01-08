import json, os, random

def generar_niveles_completos():
    if not os.path.exists('json'): os.makedirs('json')
    for i in range(1, 11):
        maze = [[1 for _ in range(15)] for _ in range(15)]
        
        def abrir_camino(p1, p2):
            curr = list(p1)
            while curr != p2:
                eje = 0 if curr[0] != p2[0] and (random.random() > 0.5 or curr[1] == p2[1]) else 1
                curr[eje] += 1 if p2[eje] > curr[eje] else -1
                maze[curr[1]][curr[0]] = 0
                if curr[1]+1 < 14: maze[curr[1]+1][curr[0]] = 0 # Pasillo ancho

        spawn, star, exit_n = [1, 1], [random.randint(2,12), random.randint(2,12)], [13, 13]
        abrir_camino(spawn, star)
        abrir_camino(star, exit_n)

        data = {
            "lvl": i, "name": f"NODE_STABLE_{i:02d}",
            "spawn": spawn, "exit": exit_n, "star": star,
            "enemy_spawn": [7, 7] if i > 1 else [-1, -1],
            "maze": maze
        }
        with open(f'json/nivel{i}.json', 'w') as f:
            json.dump(data, f, indent=4)
    print("[+] Niveles generados con rutas garantizadas y metadatos.")

if __name__ == "__main__":
    generar_niveles_completos()