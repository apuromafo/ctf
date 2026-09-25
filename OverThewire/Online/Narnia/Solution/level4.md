# Narnia Nivel 4

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Narnia |
| **Nivel / Level** | 4 → 5 |
| **URL** | https://overthewire.org/wargames/narnia/ |
| **Conexión** | `ssh narnia4@narnia.labs.overthewire.org -p2226` |

# username / password
narnia4 / iqNWNk173q
# concept

# source code
```
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>

extern char **environ;

int main(int argc,char **argv){
    int i;
    char buffer[256];

    for(i = 0; environ[i] != NULL; i++)
        memset(environ[i], '\0', strlen(environ[i]));

    if(argc>1)
        strcpy(buffer,argv[1]);

    return 0;
}
```
# method of solve


nuevo año:

ssh narnia4@narnia.labs.overthewire.org
pwd: thaenohtai
 
 

---

## Fuentes / Sources

- OTW: https://overthewire.org/wargames/narnia/ - fecha de acceso: 2026-09-25.
- Autor notas: Apuromafo.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a OverTheWire.
> **EN:** Educational and personal use only. Not affiliated with OverTheWire.

_Fecha de edición: 2026-09-25_
