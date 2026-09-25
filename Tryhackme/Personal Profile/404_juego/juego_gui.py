"""Echo Pwn Maze - launcher con GUI (tkinter). Plan B al navegador automático.

Uso:
    python juego_gui.py [--port 8000]

Abre una ventanita para iniciar/detener el servidor (Juego.py),
ver la URL, abrirla en el navegador y ver el log en vivo.
"""
import argparse
import queue
import subprocess
import sys
import threading
import webbrowser
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SERVER = BASE_DIR / "Juego.py"


class Launcher:
    def __init__(self, root, port):
        import tkinter as tk
        from tkinter import ttk, messagebox
        self.tk = tk
        self.messagebox = messagebox
        self.root = root
        self.port_var = tk.StringVar(value=str(port))
        self.url_var = tk.StringVar(value="Servidor detenido")
        self.proc = None
        self.log_q = queue.Queue()
        self.reader = None

        root.title("Echo Pwn Maze - Launcher")
        root.resizable(False, False)
        frm = ttk.Frame(root, padding=12)
        frm.grid(sticky="nsew")

        ttk.Label(frm, text="Puerto:").grid(row=0, column=0, sticky="w")
        self.port_entry = ttk.Entry(frm, textvariable=self.port_var, width=8)
        self.port_entry.grid(row=0, column=1, sticky="w")

        self.btn_start = ttk.Button(frm, text="Iniciar", command=self.start)
        self.btn_start.grid(row=0, column=2, padx=4)
        self.btn_stop = ttk.Button(frm, text="Detener", command=self.stop, state="disabled")
        self.btn_stop.grid(row=0, column=3, padx=4)

        ttk.Label(frm, textvariable=self.url_var, foreground="green").grid(
            row=1, column=0, columnspan=4, sticky="w", pady=(8, 4))

        row = ttk.Frame(frm)
        row.grid(row=2, column=0, columnspan=4, sticky="ew", pady=4)
        ttk.Button(row, text="Abrir navegador", command=self.open_browser).pack(side="left")
        ttk.Button(row, text="Copiar URL", command=self.copy_url).pack(side="left", padx=4)

        self.log = tk.Text(frm, width=72, height=12, state="disabled", font=("Consolas", 9))
        self.log.grid(row=3, column=0, columnspan=4, pady=(4, 0))
        root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.poll_log()

    def server_url(self):
        return f"http://localhost:{self.port_var.get().strip()}/maze.html"

    def start(self):
        if self.proc and self.proc.poll() is None:
            return
        try:
            port = int(self.port_var.get().strip())
        except ValueError:
            self.messagebox.showerror("Puerto", "Puerto inválido.")
            return
        if not SERVER.exists():
            self.messagebox.showerror("Servidor", f"No se encuentra {SERVER}")
            return
        self.proc = subprocess.Popen(
            [sys.executable, str(SERVER), "--port", str(port), "--no-browser"],
            cwd=str(BASE_DIR), stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, text=True, bufsize=1)
        self.log_q.put(f"[*] Servidor lanzado (pid {self.proc.pid})\n")
        self.reader = threading.Thread(target=self._drain, daemon=True)
        self.reader.start()
        self.url_var.set(self.server_url())
        self.btn_start.config(state="disabled")
        self.btn_stop.config(state="normal")
        self.port_entry.config(state="disabled")

    def _drain(self):
        for line in self.proc.stdout:
            self.log_q.put(line)
        self.log_q.put(f"[*] Servidor terminado (exit {self.proc.poll()})\n")

    def poll_log(self):
        while True:
            try:
                line = self.log_q.get_nowait()
            except queue.Empty:
                break
            self.log.config(state="normal")
            self.log.insert("end", line)
            self.log.see("end")
            self.log.config(state="disabled")
            if "Servidor terminado" in line and self.proc and self.proc.poll() is not None:
                self.url_var.set("Servidor detenido")
                self.btn_start.config(state="normal")
                self.btn_stop.config(state="disabled")
                self.port_entry.config(state="normal")
        self.root.after(200, self.poll_log)

    def stop(self):
        if self.proc and self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.proc.kill()

    def open_browser(self):
        if self.proc and self.proc.poll() is None:
            webbrowser.open(self.server_url())
        else:
            self.messagebox.showinfo("Servidor", "Primero inicia el servidor.")

    def copy_url(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.server_url())

    def on_close(self):
        self.stop()
        self.root.destroy()


def main():
    ap = argparse.ArgumentParser(description="Launcher GUI Echo Pwn Maze")
    ap.add_argument("--port", type=int, default=8000)
    args = ap.parse_args()
    try:
        import tkinter as tk
    except ImportError:
        print("[!] tkinter no disponible; usa: python Juego.py", file=sys.stderr)
        sys.exit(1)
    root = tk.Tk()
    Launcher(root, args.port)
    root.mainloop()


if __name__ == "__main__":
    main()
