# Semtex Nivel 10 - 11

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Semtex (offline) |
| **Nivel / Level** | 10 - 11 |
| **URL** | https://overthewire.org/wargames/semtex/ |

Semtex Level 10 → Level 11
Deja vue
/rdx/vl1b is vortex semtex1 with a slight modification to make things a little bit harder.

Thanks to andrewg for inspiration.

Suggested reading
manpages: popen, dup2

Included file: semtex11.c
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>


// code by andrewg, modified by aton

#define e(); if(((unsigned int)ptr & 0xff000000)==0xca000000) { setresuid(geteuid(), geteuid(), geteuid()); execlp("/bin/sh", "sh", "-i", NULL); }

void print(unsigned char *buf, int len)
{
        int i;

        printf("[ ");
        for(i=0; i < len; i++) printf("%x ", buf[i]);
        printf(" ]\n");
}

int main()
{
        unsigned char buf[512];
        unsigned char *ptr = buf + (sizeof(buf)/2);
        unsigned int x;

        while((x = getchar()) != EOF) {
                switch(x) {
                        case '\n': print(buf, sizeof(buf)); continue; break;
                        case '\\': ptr--; break;
                        default: e(); if(ptr > buf + sizeof(buf)) continue; ptr++; break;
                }
        }
        printf("All done\n");
}

---

## Fuentes / Sources

- OTW: https://overthewire.org/wargames/semtex/ - fecha de acceso: 2026-09-25.
- Autor notas: Apuromafo.

---

## Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a OverTheWire.
> **EN:** Educational and personal use only. Not affiliated with OverTheWire.

_Fecha de edición: 2026-09-25_
