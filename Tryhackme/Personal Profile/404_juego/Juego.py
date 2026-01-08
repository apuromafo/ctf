import http.server
import socketserver
import webbrowser
import json
import os
import base64
import secrets # Para generar tokens seguros

PORT = 8000

# Diccionario para almacenar tokens válidos temporalmente
valid_tokens = set()

class EchoHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Endpoint para obtener un token CSRF al ganar
        if self.path == '/get_token':
            token = secrets.token_hex(16)
            valid_tokens.add(token)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"csrf_token": token}).encode())
        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == '/save_ranking':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            
            # --- VALIDACIÓN CSRF ---
            user_token = data.get('csrf_token')
            if not user_token or user_token not in valid_tokens:
                self.send_response(403) # Prohibido
                self.end_headers()
                self.wfile.write(b'CSRF Token Invalid or Already Used')
                return

            # Consumir el token (evita duplicados)
            valid_tokens.remove(user_token)
            
            # Guardar en el ranking (Base64)
            entry = f"2026-01-08 - User: {data['user']} - Lvl: {data['lvl']}"
            b64_entry = base64.b64encode(entry.encode()).decode()
            
            if not os.path.exists('ranking'): os.makedirs('ranking')
            with open('ranking/scores.db', 'a') as f:
                f.write(b64_entry + '\n')
            
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')

print(f"[*] Servidor Protegido en http://localhost:{PORT}")
webbrowser.open(f"http://localhost:{PORT}/maze.html")

with socketserver.TCPServer(("", PORT), EchoHandler) as httpd:
    httpd.serve_forever()
    
    #nota  para los scores es solo una base64  pwn_scores se llama el valor base antes de usar (json)