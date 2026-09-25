import json, os, random
from collections import deque
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ADJ = ((1, 0), (-1, 0), (0, 1), (0, -1))

SIZE = 15

def inside(x, y):
    return 1 <= x <= SIZE - 2 and 1 <= y <= SIZE - 2

def carve(maze, x, y):
    if inside(x, y):
        maze[y][x] = 0

def abrir_camino(maze, p1, p2, ancho=True):
    """Ruta entre dos puntos. Con ancho=True abre pasillo doble (2 celdas)."""
    maze[p1[1]][p1[0]] = 0
    curr = list(p1)
    prev_dir = None
    while curr != list(p2):
        eje = 0 if curr[0] != p2[0] and (random.random() > 0.5 or curr[1] == p2[1]) else 1
        paso = 1 if p2[eje] > curr[eje] else -1
        curr[eje] += paso
        carve(maze, curr[0], curr[1])
        if ancho:
            # ensanchar perpendicular al avance: hay sitio para esquivar
            if eje == 0:
                carve(maze, curr[0], curr[1] + 1)
            else:
                carve(maze, curr[0] + 1, curr[1])
    carve(maze, p2[0], p2[1])

def bfs_dist(maze, a, blocked=()):
    blk = set(blocked)
    dist = {tuple(a): 0}; prev = {}; q = deque([tuple(a)])
    while q:
        x, y = q.popleft()
        for dx, dy in ADJ:
            nx, ny = x + dx, y + dy
            if 0 <= nx < SIZE and 0 <= ny < SIZE and (nx, ny) not in dist and (nx, ny) not in blk and maze[ny][nx] == 0:
                dist[(nx, ny)] = dist[(x, y)] + 1; prev[(nx, ny)] = (x, y); q.append((nx, ny))
    return dist, prev

def ruta(maze, a, b):
    dist, prev = bfs_dist(maze, a)
    if tuple(b) not in dist:
        return None
    path = [tuple(b)]
    while path[-1] != tuple(a):
        path.append(prev[path[-1]])
    return path[::-1]

def tallar_bypass(maze, a, b, bloqueado):
    """Segundo pasillo: abre un rodeo de a->b sin pasar por bloqueado."""
    blk = set(bloqueado)
    prev = {tuple(a): None}; q = deque([tuple(a)])
    while q:
        x, y = q.popleft()
        if (x, y) == tuple(b):
            break
        for dx, dy in ADJ:
            nx, ny = x + dx, y + dy
            if inside(nx, ny) and (nx, ny) not in prev and (nx, ny) not in blk:
                prev[(nx, ny)] = (x, y); q.append((nx, ny))
    if tuple(b) not in prev:
        return None
    path = [tuple(b)]
    while path[-1] != tuple(a):
        path.append(prev[path[-1]])
    for x, y in path[::-1]:
        carve(maze, x, y)
        carve(maze, x + 1, y)  # bypass también doble
    return True

def generar_nivel(i):
    for intento in range(50):
        maze = [[1 for _ in range(SIZE)] for _ in range(SIZE)]
        spawn, exit_n = [1, 1], [13, 13]
        star = [random.randint(2, 12), random.randint(2, 12)]
        # ruta principal (doble ancho)
        abrir_camino(maze, spawn, star)
        abrir_camino(maze, star, exit_n)
        # segunda ruta por el lado opuesto: garantiza alternativa y loops
        wp = [random.randint(2, 12), random.randint(2, 12)]
        abrir_camino(maze, spawn, wp)
        abrir_camino(maze, wp, exit_n)
        if not ruta(maze, spawn, star) or not ruta(maze, star, exit_n):
            continue
        r2 = ruta(maze, star, exit_n)
        if i == 1:
            enemy = [-1, -1]
        else:
            enemy = list(r2[len(r2) // 2])
            a = r2[max(0, len(r2) // 2 - 2)]; b = r2[min(len(r2) - 1, len(r2) // 2 + 2)]
            if not tallar_bypass(maze, a, b, [tuple(enemy)]):
                continue
        # verificación final: con el enemigo bloqueado sigue habiendo paso
        d_ok, _ = bfs_dist(maze, star, [tuple(enemy)] if enemy[0] != -1 else [])
        if enemy[0] != -1 and tuple(exit_n) not in d_ok:
            continue
        return {"lvl": i, "name": f"NODE_STABLE_{i:02d}", "spawn": spawn,
                "exit": exit_n, "star": star, "enemy_spawn": enemy, "maze": maze}
    raise RuntimeError(f"nivel {i}: no se pudo generar mapa válido")

def generar_niveles_completos():
    json_dir = BASE_DIR / 'json'
    json_dir.mkdir(parents=True, exist_ok=True)
    for i in range(1, 11):
        data = generar_nivel(i)
        with open(json_dir / f'nivel{i}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    print("[+] Niveles generados: doble pasillo, rutas garantizadas y bypass del enemigo.")

if __name__ == "__main__":
    generar_niveles_completos()
