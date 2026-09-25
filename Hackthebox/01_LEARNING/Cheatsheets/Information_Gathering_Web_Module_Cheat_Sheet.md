# Information Gathering (Web Edition) — Cheat Sheet

> **Fuente / Source:** [m4riio21/HTB-Academy-Cheatsheets](https://github.com/m4riio21/HTB-Academy-Cheatsheets) (`web-information-gathering.md`) — fecha de acceso: 2026-09-24. Módulo HTB Academy: Information Gathering - Web Edition.
> **Autor notas:** Apuromafo (curaduría local).

---

## WHOIS

| **Command** | **Description** |
|-|-|
| `export TARGET="domain.tld"` | Assign target to an environment variable. |
| `whois $TARGET` | WHOIS lookup for the target. |

---
## DNS Enumeration

| **Command** | **Description** |
|-|-|
| `nslookup $TARGET` | Identify the `A` record for the target domain. |
| `dig $TARGET @<nameserver/IP>` | Identify the `A` record for the target domain.  |
| `nslookup -query=PTR <IP>` / `dig -x <IP> @<nameserver/IP>` | Identify the `PTR` record. |
| `nslookup -query=TXT $TARGET` / `dig txt $TARGET @<nameserver/IP>` | Identify the `TXT` records. |
| `nslookup -query=MX $TARGET` / `dig mx $TARGET @<nameserver/IP>` | Identify the `MX` records. |

---
## Passive Subdomain Enumeration

| **Resource/Command** | **Description** |
|-|-|
| `VirusTotal` | https://www.virustotal.com/gui/home/url |
| `Censys` | https://censys.io/ |
| `Crt.sh` | https://crt.sh/ |
| `curl -s https://sonar.omnisint.io/subdomains/{domain} \| jq -r '.[]' \| sort -u` | All subdomains for a given domain. |
| `curl -s "https://crt.sh/?q=${TARGET}&output=json" \| jq -r '.[] \| "\(.name_value)\n\(.common_name)"' \| sort -u` | Certificate Transparency. |
| `cat sources.txt \| while read source; do theHarvester -d "${TARGET}" -b $source -f "${source}-${TARGET}";done` | theHarvester across sources (baidu, crtsh, hackertarget, otx, virustotal, etc.). |

---
## Passive / Active Infrastructure Identification

| **Resource/Command** | **Description** |
|-|-|
| `Netcraft` / `WayBackMachine` / `waybackurls` | Tech history and archived URLs. |
| `curl -I "http://${TARGET}"` | HTTP headers of the target webserver. |
| `whatweb -a https://target -v` / `Wappalyzer` / `wafw00f` | Technology identification / WAF fingerprinting. |
| `gobuster dns -q -r "${NS}" -d "${TARGET}" -w "${WORDLIST}"` | Bruteforcing subdomains. |
| `nslookup -type=any -query=AXFR $TARGET nameserver.target.domain` | Zone transfer attempt. |

---
## Virtual Hosts

| **Resource/Command** | **Description** |
|-|-|
| `curl -s http://192.168.10.10 -H "Host: randomtarget.com"` | Request a specific vhost. |
| `ffuf -w ./vhosts -u http://<IP> -H "HOST: FUZZ.target.domain" -fs 612` | Bruteforcing vhosts with ffuf. |

---
## Crawling

| **Resource/Command** | **Description** |
|-|-|
| `ZAP` (OWASP) | Web app crawling and scanning. |
| `ffuf -recursion -recursion-depth 1 -u http://192.168.10.10/FUZZ -w raft-small-directories-lowercase.txt` | Discover hidden files and folders. |

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox.

_Fecha de edición: 2026-09-24_
