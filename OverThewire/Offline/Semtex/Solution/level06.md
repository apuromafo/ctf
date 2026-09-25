# Semtex Nivel 6 - 7

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Semtex (offline) |
| **Nivel / Level** | 6 - 7 |
| **URL** | https://overthewire.org/wargames/semtex/ |

Semtex Level 6 → Level 7
Multi-vitamin
Getting out of the restricted shell shouldn’t take you more than five minutes. Then have a look at /rdx/multivitamin. Try to analyse the algorithm very carefully. There is a weakness that really speeds up your quest…\

Multiplication is easy, and so is division…? You might want to look at http://gmplib.org/ if you use c.

Included file: semtex7.c
/*
 *      multivitamin.c 2006 by aton@packetdropped.org
 *
 *      rules: no patching.
 *      compile: gcc multivitamin.c -o multivitamin -lgmp
 *
 *      -> multiplication is simple, and so is division...?
 */


#define _GNU_SOURCE
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <gmp.h>

#define ADDVALUE 27137

int main(int argc, char *argv[])
{
        mpz_t longjohn, mul, cmpval;
        char userstr[512+1];
        int n=0;

        mpz_init(longjohn);
        mpz_set_ui(longjohn, 1);
        mpz_init(mul);
        mpz_init(cmpval);
        mpz_set_str(cmpval, "insert-here-the-password-hash-from-your-home-directory-on-semtex-7", 10);

        if (argc<2)
        {
                printf("%s <string>\n", argv[0]);
                return -1;
        }

        strncpy(userstr, argv[1], 512);

        for (n=0;n<strlen(userstr);n++)
        {
                mpz_set_ui(mul, (unsigned long)(userstr[n]+ADDVALUE));
                mpz_mul(longjohn, longjohn, mul);
        }

        if (!(n=mpz_cmp(longjohn, cmpval)))
        {
                setresuid(geteuid(), geteuid(), geteuid());
                execlp("/bin/bash", "bash", NULL);
        }
        else
                printf("err... booom!\n");

        return 0;
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
