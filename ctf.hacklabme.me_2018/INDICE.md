# ÍNDICE — ctf.hacklabme.me_2018 / INDEX

ES: Inventario del archivo `ctf.hacklabme.me_2018/` por nombres de carpetas +
`Description.txt`/`Descripcion.txt` pequeños (<1 KB). No se abrieron binarios
ni se extrajeron zips. Cobertura `Solucion/` = existe carpeta de solución
(no valida calidad del contenido).
EN: Short inventory of `ctf.hacklabme.me_2018/` from folder names + small
`Description.txt` files (<1 KB). No binaries opened, no zips extracted.
`Solucion/` coverage = solution folder exists (does not validate quality).

Fuente raíz / Root note: `Descripcion.txt` (85 B): "Estos son los retos y
solucion que realicé para ctf.hacklabme.me — Saludos Apuromafo".

## Tabla por categoría / Table by category

| Categoría / Category | Nº retos | Puntos (según nombre / per folder name) | Cobertura Solucion/ | Huecos honestos / Honest gaps |
|---|---|---|---|---|
| Crypto | 9 | 3300 (100+100+200+300+500+600+600+200+700) | 9/9 | 08 sin `Description.txt` (solo `flag.txt`+`fix.txt` en 06); 07 `Solucion/solucion.txt` mide 466 B hoy (AGENT.md decía 0 B — discrepancia sin verificar) |
| Forensics | 2 | 400 (200+200) | 2/2 | Sin `Description.txt` propios; 01 trae `Cypress.docx` + carpeta `Cypress/` extraída; `Solucion/` de 01 son imágenes + txt corto |
| Gral | 3 | 700 (200+200+300) | 3/3 | Carpeta `Idénticos` con encoding roto (`Id�nticos`); 02-Spam: `Description.txt` (1032 B) es el propio reto (spam) |
| IoT | 4 (anidados en `IoT/IoT/`) | 1250 (200+300+350+400) | 4/4 anidados | `IoT.rar` (22 MB) duplica `IoT/IoT/` (redundante); retos sobre Telnet/firmware `.bin` no abiertos |
| Malware | 5 | 1650 (250+300+350+400+350) | 5/5 | Muestras no ejecutadas/extraídas (solo metadatos); `Lenguaje de programación` con encoding roto; ver aviso abajo |
| OSINT | 11 | 3200 (200+300+300+300+350+350+400+400+200+200+200) | 11/11 | 03-Primer Tweet y 11-Call Me SIN archivos de reto ni `Descripcion` (solo `Solucion/`); `Quién es` y `Cámara` con encoding roto |
| Reversing | 3 | 950 (200+250+500) | 3/3 | `Código 1/2` con encoding roto; binarios `.exe` no ejecutados (solo nombre+tamaño) |
| Steganography | 6 | 2000 (200+300+350+400+450+300) | 6/6 | 06-Radar referencia host muerto `pcte.co/radar`; 02 normalizada a `Solucion/` |
| Web | 2 | s/p en nombre (Descriptions: 300+200=~500) | 2/2 | Sin puntos en nombres; referencian hosts muertos (`pcte.co`); 02 incluye `BarCampSE.html` (1003 B) |
| **Total** | **45** | **13450 nominales (+~500 Web no nominal)** | **45/45 carpetas Solucion** | Ver notas |

## Retos / Challenges (nombres exactos de carpetas / exact folder names)

- Crypto (9): `01 - Binary 100pts`, `02 - esab46 100pts`, `03 - Punto 200pts`,
  `04 - Password 300pts`, `05 - HacKLabText 500pts`, `06 - Fixme 600pts`,
  `07 - 8^2 600pts`, `08 - For Dummies 200pts`, `09 - Crypto Bot 700pts`
  (09-Crypto Bot: servicio en `129.213.122.66:8888`, muerto).
- Forensics (2): `01 - Cypress 200pts`, `02 - QR 200pts`.
- Gral (3): `01 - ctfxp 200pts`, `02 - Spam 200pts`, `03 - Idénticos 300pts`.
- IoT (4, bajo `IoT/IoT/`): `01 - Telnet User 200pts`, `02 - Telnet Password 300pts`,
  `03 - Telnet (User_Pass) 350pts`, `04 - Email 400pts`.
- Malware (5): `01 - Dominio Malicioso 250pts`, `02 - Packer 300pts`,
  `03 - Lenguaje de programación 350pts`, `04 - Proceso 400pts`,
  `05 - Portable Document Format 350pts`.
- OSINT (11): `01 - Terroristas 200pts`, `02 - Alias El Guitarrista Ruso 300pts`,
  `03 - Primer Tweet 300pts`, `04 - Quién es 300pts`, `05 - Stuxnet 350pts`,
  `06 - La Camisa Negra en Oslo 350pts`, `07 - Placa 400pts`, `08 - Cámara 400pts`,
  `09 - Twitter Client 200pts`, `10 - ElTiempo.com 200pts`, `11 - Call Me 200pts`.
- Reversing (3): `01 - Código 1 200pts`, `02 - Código 2 250pts`, `03 - Serial 500pts`.
- Steganography (6): `01 - Stranger Things 200pts`, `02 - Epica 300pts`,
  `03 - PIMP 350pts`, `04 - NWA 400pts`, `05 - Kush Ups 450pts`, `06 - Radar 300pts`.
- Web (2): `01 - Web`, `02 - KeyWord`.

## Notas / Notes

- ES: Puntos sumados solo si aparecen en el nombre; Web no los trae en el
  nombre (se citan de sus `Description.txt`). Cobertura 100 % significa
  "carpeta presente", no "solución verificada". No se fabrican flags ni URLs.
  EN: Points summed only when present in folder names; Web points come from
  `Description.txt`. 100 % coverage means "folder present", not "verified".
  No flags or URLs fabricated.
- ES: Encoding roto (mojibake `�`) en: `Idénticos`, `Quién es`, `Cámara`,
  `Código 1/2`, `Lenguaje de programación`. No renombrar (alcance read-only).
  EN: Broken encoding (`�`) in those folders. Do not rename (read-only scope).

---

*ES: Archivo educativo de CTF; `Malware/` e IoT `.bin` en cuarentena: no
ejecutar ni extraer. EN: Educational CTF archive; keep `Malware/` and IoT
`.bin` quarantined — do not execute or extract. 2026-09-26.*
