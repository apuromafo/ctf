# Introduction to Flask

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `introductiontoflask` | [TryHackMe - Introduction to Flask](https://tryhackme.com/room/introductiontoflask) | `01 Level Easy` | THM | Flask, Jinja2, SSTI, LFI | Easy · Educativo (lab) |

> **Objeto:** Comprender el funcionamiento del micro-framework web Flask (Python) y explotar una vulnerabilidad de Server-Side Template Injection (SSTI) en su motor de plantillas Jinja2 para escalar a Local File Inclusion (LFI) y leer el flag de la máquina.

---

**Contexto:**

> **ES:** Migración al formato Bandit enriquecido de la room "Introduction to Flask" (nivel Easy, tipo walkthrough). Se recorre la configuración y despliegue de Flask, la sintaxis básica de rutas, los métodos HTTP y el renderizado de plantillas Jinja2, hasta llegar a la explotación de una vulnerabilidad SSTI que permite la lectura local de archivos (LFI) y la obtención del flag.
>
> **EN:** How it works and how can I exploit it?

## Solucionario

### Respuestas originales (verbatim)

Contenido original del archivo migrado, conservado íntegramente:

```
1. No answer needed
2. FLASK_APP
3. 1. 5000
   2. yay
4. 1. yay
   2. HTML
5. No answer needed
6. THM{flask_1njected}
7. No answer needed
```

---

### Task 1: Introducción / Introduction

**Explicación:** La room presenta Flask como un micro-framework web escrito en Python, clasificado como microframework por no requerir herramientas ni librerías particulares. Este laboratorio forma parte de la serie dedicada a los frameworks de Python y su utilidad para pentesters: aprender cómo funcionan y cómo pueden explotarse. Es la primera tarea de solo lectura.

- `1. No answer needed`

---

### Task 2: Instalación y conceptos de despliegue / Installation and Deployment basics

**Explicación:** Se instala Flask y se configura la aplicación. Instalación con `pip3 install Flask`. Después se crea el archivo de la aplicación (script con el código Flask) y se indica a Flask qué aplicación ejecutar mediante la variable de entorno `FLASK_APP`.

- Windows: `set FLASK_APP=hello.py`
- Linux: `export FLASK_APP=hello.py`

Para desplegar la aplicación se ejecuta `flask run` (local) o `flask run --host=0.0.0.0` (pública dentro de la red).

- Respuesta original: `2. FLASK_APP`

Pregunta (verbatim): Which environment variable do you need to change in order to run Flask?
Respuesta: `FLASK_APP`

---

### Task 3: Sintaxis básica y enrutado / Basic syntax and routing

**Explicación:** Se importa la librería Flask y se define la variable `app` como proyecto Flask. Mediante `@app.route` se asignan funciones a las direcciones de la página: la ruta `/` muestra "Hello, TryHackMe!" y, añadiendo otra ruta con el mismo decorador, se pueden crear páginas y URLs dinámicas (p. ej. `/admin`). Al navegar a `http://127.0.0.1:5000/` o `http://127.0.0.1:5000/admin` se obtienen mensajes distintos. Por defecto el servidor de desarrollo de Flask se despliega en el puerto 5000, configurable por el usuario.

- Respuestas originales: `3. 1. 5000` / `2. yay`

Preguntas (verbatim):
- What's the default deployment port used by Flask? → `5000`
- Is it possible to change that port? (yay/nay) → `yay`

---

### Task 4: Métodos HTTP y renderizado de plantillas / HTTP Methods and Template Rendering

**Explicación:** Las aplicaciones web utilizan distintos métodos HTTP (GET y POST). Por defecto una ruta solo responde a GET, pero empleando el argumento `methods` en `route()` se pueden manejar varios métodos (p. ej. `@app.route('/login', methods=['GET', 'POST'])`), separando el comportamiento según el método recibido (por ejemplo `do_the_login()` para POST y `show_the_login_form()` para el resto). Además, `render_template` permite a Flask renderizar automáticamente archivos HTML/Template como sitio web, facilitando su manejo: se añade la función y el resultado queda renderizado en el navegador.

- Respuestas originales: `4. 1. yay` / `2. HTML`

Preguntas (verbatim):
- Does Flask support POST requests? (yay/nay) → `yay`
- What markdown language can you use to make templates for Flask? → `HTML`

---

### Task 5: Subida de archivos / File Upload

**Explicación:** Flask permite manejar archivos subidos por el usuario. Se accede a ellos mediante el atributo `files` del objeto `request`, que se comporta como un objeto de archivo estándar de Python y añade el método `save()`, que permite almacenar el archivo en el sistema de archivos del servidor. Se puede crear una página de subida (`/upload`) que espera un POST y guarda el archivo, sin olvidar el atributo `enctype="multipart/form-data"` en el formulario HTML, de lo contrario el navegador no transmite los archivos.

```python
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['filename']
        f.save('uploads/' + secure_filename(f.filename))
    return render_template('upload.html')
```

- `5. No answer needed`

---

### Task 6: Inyección en Flask / Flask Injection

**Explicación:** Tarea con máquina desplegable. Una simple mala configuración puede tener consecuencias graves de seguridad. En Flask, el motor de plantillas Jinja2 permite a los desarrolladores introducir vulnerabilidades de Server-Side Template Injection (SSTI): un atacante puede ejecutar código dentro del contexto del servidor y, en algunos casos, llegar a un Remote Code Execution (RCE). En este laboratorio se explota una mala configuración concreta para conseguir una Local File Inclusion (LFI). La causa es que Jinja2 usa llaves `{{ }}` para rodear las variables de la plantilla; en el código vulnerable la plantilla está dentro de delimitadores `''' '''`, lo que permite abusar del mecanismo de plantillas de Jinja. La variable tras "hello" parsea el nombre de la variable `person`, pero al ser código vulnerable se puede hacer que muestre la contraseña.

Código vulnerable:

```python
from flask import Flask, request, render_template_string, render_template

app = Flask(__name__)

@app.route('/vuln')
def hello_ssti():
	person = {'name':"HackerTHM", 'password':"123456789"}
	if request.args.get('name'):
		person['name'] = request.args.get('name')
	
	template = '''<h2>Hello %s!</h2>''' % person['name'] # Problem
	
	return render_template_string(template, person=person)

def get_user_file(f_name):
	with open(f_name) as f:
		return f.readlines()

app.jinja_env.globals['get_user_file'] = get_user_file

if __name__ == "__main__":
	app.run(debug=True)
```

Fuga de credenciales: ir a `http://MACHINE_IP:5000/vuln?name=` y añadir al final `{{ person.password }}` para ver la contraseña en texto plano.

Escalada a LFI: `{{ get_user_file("/etc/passwd") }}` permite leer el archivo especificado (o cualquier otro cambiando el nombre).

Payload para el flag:

```
http://MACHINE_IP:5000/vuln?name={{ get_user_file("/home/flask/flag.txt") }}
```

La vulnerabilidad se mitiga fácilmente usando una sola comilla (`' '`) en la variable de la plantilla (en lugar de `''' '''`).

- Respuesta original: `6. THM{flask_1njected}`

Pregunta (verbatim): What's inside /home/flask/flag.txt ?
Respuesta: `THM{flask_1njected}`

---

### Task 7: Referencias y fuentes / References and Sources

**Explicación:** La room recopila las referencias y fuentes utilizadas: la documentación oficial de Flask para toda la room (TutorialSploit), "Injecting Flask" de nVisium para la task 6, y "Flask Uploads" para la task 5. Tarea de solo lectura.

- `7. No answer needed`

---

### Tabla unificada de preguntas / respuestas

| Task | Pregunta (verbatim EN) | Respuesta |
|---|---|---|
| 1 | — (tarea de solo lectura) | `No answer needed` |
| 2 | Which environment variable do you need to change in order to run Flask? | `FLASK_APP` |
| 3 | What's the default deployment port used by Flask? | `5000` |
| 3 | Is it possible to change that port? (yay/nay) | `yay` |
| 4 | Does Flask support POST requests? (yay/nay) | `yay` |
| 4 | What markdown language can you use to make templates for Flask? | `HTML` |
| 5 | — (tarea de solo lectura) | `No answer needed` |
| 6 | What's inside /home/flask/flag.txt ? | `THM{flask_1njected}` |
| 7 | — (tarea de solo lectura) | `No answer needed` |

---

**Metodología:**

1. **Reconocimiento:** identificar la aplicación Flask expuesta en el puerto 5000 y cartografiar sus rutas (endpoint `/vuln`).
2. **Detección de SSTI:** inyectar delimitadores de plantilla de Jinja2 (`{{ ... }}`) en el parámetro `name` para confirmar que la entrada se evalúa como plantilla.
3. **Prueba de concepto:** abusar de la variable `person` del contexto (`{{ person.password }}`) para exfiltrar la credencial en texto plano.
4. **Escalada a LFI:** emplear la función global de Jinja2 `get_user_file()` registrada por la aplicación para leer archivos del sistema (`/etc/passwd`).
5. **Exfiltración del flag:** leer `/home/flask/flag.txt` y obtener `THM{flask_1njected}`.
6. **Remediación:** no concatenar la entrada del usuario en el código de la plantilla; pasar las variables como datos del motor de plantillas.

### Cadena de ataque / Attack Chain

1. Aplicación Flask vulnerable expuesta → puerto 5000, ruta `/vuln`.
2. Plantilla construida por concatenación insegura con `''' '''` (`template = '''<h2>Hello %s!</h2>''' % person['name']`) → SSTI en `render_template_string`.
3. `{{ person.password }}` → fuga de la credencial `123456789` en texto claro.
4. `{{ get_user_file("/etc/passwd") }}` → Local File Inclusion (LFI).
5. `{{ get_user_file("/home/flask/flag.txt") }}` → flag `THM{flask_1njected}`.

**Learning chain:**

Flask microframework → instalación y despliegue (`FLASK_APP`, `flask run`) → rutas y métodos HTTP (GET/POST) → renderizado de plantillas Jinja2 → `render_template_string` inseguro → Server-Side Template Injection (SSTI) → Local File Inclusion (LFI) → mitigación (pasar los datos como datos, nunca como código).

**Lección:**

*Aprender a programar con frameworks es clave para un pentester, pero un simple error de configuración en Flask puede convertirse en SSTI y, posteriormente, en LFI o incluso RCE. Nunca concatene la entrada del usuario dentro del código de una plantilla: pase los valores como argumentos del motor de plantillas (por ejemplo, usando comillas simples en la variable de la plantilla), y las llaves `{{ }}` jamás serán evaluadas como código.*

**MITRE ATT&CK:**

| Técnica | Uso en esta room |
|---|---|
| T1190 – Exploit Public-Facing Application | Acceso inicial explotando la aplicación web Flask expuesta. |
| T1505.006 – Server-Side Template Injection | Abuso del motor de plantillas Jinja2 vía `render_template_string`. |
| T1005 – Data from Local System | Lectura de archivos locales del servidor (LFI). |
| T1552.001 – Unsecured Credentials: Credentials In Files | Exposición de la credencial `password` del objeto `person`. |

**Fuente:** [TryHackMe - Introduction to Flask](https://tryhackme.com/room/introductiontoflask)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.