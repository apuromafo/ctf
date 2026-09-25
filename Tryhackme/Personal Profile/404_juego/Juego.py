"""Echo Pwn Maze - servidor local funcional.

Uso:
    python Juego.py [--port 8000] [--no-browser]

Sirve maze.html, json/, personaje/ y expone:
    GET  /get_token    -> {"csrf_token": "..."} (un solo uso)
    POST /save_ranking -> {"user","lvl","csrf_token"} guarda en ranking/scores.db (base64)
    GET  /api/ranking  -> {"scores": [b64, ...]}
"""
import argparse
import base64
import functools
import http.server
import json
import os
import secrets
import socketserver
import sys
import webbrowser
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RANKING_DIR = BASE_DIR / "ranking"
RANKING_FILE = RANKING_DIR / "scores.db"

valid_tokens = set()


class EchoHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def log_message(self, fmt, *args):
        sys.stderr.write("[%s] %s\n" % (self.address_string(), fmt % args))

    def _send_json(self, obj, code=200):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/get_token":
            token = secrets.token_hex(16)
            valid_tokens.add(token)
            self._send_json({"csrf_token": token})
        elif self.path == "/api/ranking":
            scores = []
            try:
                if RANKING_FILE.exists():
                    scores = [
                        line.strip()
                        for line in RANKING_FILE.read_text(encoding="utf-8").splitlines()
                        if line.strip()
                    ]
            except OSError as e:
                self._send_json({"error": f"no se pudo leer ranking: {e}"}, code=500)
                return
            self._send_json({"scores": scores})
        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path != "/save_ranking":
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")
            return
        length = self.headers.get("Content-Length")
        if not length:
            self.send_response(411)
            self.end_headers()
            self.wfile.write(b"Content-Length requerido")
            return
        try:
            content_length = int(length)
        except ValueError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Content-Length invalido")
            return
        if content_length <= 0 or content_length > 10_000:
            self.send_response(413)
            self.end_headers()
            self.wfile.write(b"Payload invalido")
            return
        try:
            raw = self.rfile.read(content_length)
            data = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"JSON invalido")
            return

        user_token = data.get("csrf_token")
        if not user_token or user_token not in valid_tokens:
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"CSRF Token Invalid or Already Used")
            return
        valid_tokens.discard(user_token)

        user = str(data.get("user", "")).strip().replace("\n", " ").replace("\r", " ")[:32]
        try:
            lvl = int(data.get("lvl", 0))
        except (TypeError, ValueError):
            lvl = 0
        if not user or not (1 <= lvl <= 10):
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Campos user/lvl invalidos")
            return

        stamp = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d")
        entry = f"{stamp} - User: {user} - Lvl: {lvl}"
        b64_entry = base64.b64encode(entry.encode("utf-8")).decode("ascii")

        try:
            RANKING_DIR.mkdir(parents=True, exist_ok=True)
            # Si el archivo existe pero no termina en newline, separarlo
            # (el scores.db original venía sin \n final y un append directo
            # concatenaba dos entradas en una sola línea corrupta).
            need_nl = (
                RANKING_FILE.exists()
                and RANKING_FILE.stat().st_size > 0
                and not RANKING_FILE.read_bytes().endswith(b"\n")
            )
            with open(RANKING_FILE, "a", encoding="utf-8") as f:
                if need_nl:
                    f.write("\n")
                f.write(b64_entry + "\n")
        except OSError as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Error guardando ranking: {e}".encode("utf-8"))
            return

        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"OK")


def find_server(port, tries=10):
    """Intenta enlazar port..port+tries-1, devuelve (servidor, puerto)."""
    last_err = None
    for p in range(port, port + tries):
        try:
            handler = functools.partial(EchoHandler)
            httpd = socketserver.ThreadingTCPServer(("127.0.0.1", p), handler)
            httpd.allow_reuse_address = True
            return httpd, p
        except OSError as e:
            last_err = e
    raise last_err


def main():
    ap = argparse.ArgumentParser(description="Servidor Echo Pwn Maze")
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--no-browser", action="store_true")
    args = ap.parse_args()

    for needed in ("maze.html", "json", "personaje"):
        if not (BASE_DIR / needed).exists():
            print(f"[!] Falta {needed} en {BASE_DIR}", file=sys.stderr)

    try:
        httpd, port = find_server(args.port)
    except OSError as e:
        print(f"[!] No se pudo enlazar puerto {args.port}: {e}", file=sys.stderr)
        sys.exit(1)

    url = f"http://localhost:{port}/maze.html"
    print(f"[*] Servidor funcional en {url}")
    print(f"[*] Sirviendo desde {BASE_DIR}")
    if not args.no_browser:
        try:
            webbrowser.open(url)
        except Exception as e:
            print(f"[!] No se pudo abrir el navegador: {e}", file=sys.stderr)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Servidor detenido.")
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
