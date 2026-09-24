# Brooklyn

> **ES:** Arena Battlegrounds de HackTheBox. Intento de escalada vía UDF de MySQL documentado abajo.
> **EN:** HackTheBox Battlegrounds arena. MySQL UDF escalation attempt documented below.

## 📝 Nota original / Original note

```sql
show variables like "%plugin%";

plugin_dir /opt/lampp/lib/mysql/plugin/
plugin_maturity gamma

show variables like 'version_compile_%'

version_compile_machine x86_64
version_compile_os Linux

Can't create/write to file '/opt/lampp/lib/mysql/plugin/mysqludf.so' (Errcode: 13 "Permission denied")
```

> **ES:** El directorio de plugins no es escribible (`Permission denied`): la vía UDF clásica está bloqueada, buscar alternativa.
> **EN:** The plugin dir is not writable (`Permission denied`): the classic UDF path is blocked, look for an alternative.

## 🎯 Objetivo / Objective

> **ES:** Escalar privilegios vía MySQL (u otra vía si UDF está bloqueado) hasta root.
> **EN:** Escalate privileges via MySQL (or another path if UDF is blocked) to root.

## 🛠️ Herramientas / Tools

- `mysql` client
- `nmap`, `linpeas.sh`

## 📝 Pasos / Steps

### 1. Enumeración MySQL / MySQL enumeration

```bash
mysql -u <user> -p -e 'show variables like "%plugin%";'
```

**Resultado / Result:** `plugin_dir /opt/lampp/lib/mysql/plugin/`, no escribible.

### 2. Escalada / Escalation — pendiente de documentar vía alternativa / pending documentation via alternative path

## 📚 Fuentes / Sources

- Nota previa local (bloque SQL + paráfrasis, esta misma ficha)
- HTB Battlegrounds: Brooklyn — fecha de acceso: 2026-09-24
- Autor notas: Apuromafo

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de contenido activo.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish active content flags.

_Fecha de edición: 2026-09-24_
