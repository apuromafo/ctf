# Advent 2025\SideQuest\Sidequest\Sidequest3\img_decode [N/A]

## Clave de acceso a la misión secundaria Carrotbane of My Existence / Carrotbane of My Existence Side Quest Access key

[Carrotbane of My Existence Side Quest Access key -  Full Walkthrough 2025](https://youtu.be/8OQX9d6igKA)

**Cyberchef decoding recipe:**

```
Extract_RGBA(' ',false)
Find_/_Replace({'option':'Regex','string':'(\\d+) \\d+ \\d+ ?'},'$1\\n',true,false,true,false)
From_Decimal('Line feed',false)
Find_/_Replace({'option':'Regex','string':'(={1,6})'},'$1\\\\n',true,false,true,false)
Fork('\\n','\\n',false)
From_Base32('A-Z2-7=',true)
XOR({'option':'UTF8','string':'h0pp3r'},'Standard',false)
Zlib_Inflate(0,0,'Adaptive',false,false)
Merge(true)
Label('decoder_loop')
Find_/_Replace({'option':'Simple string','string':'H0\\\\n'},'H0',true,false,true,false)
ROT13(true,true,false,19)
Jump('decoder_loop',8)
From_Base64('A-Za-z0-9+/=',true,false)
Render_Image('Raw')
```

**Cyberchef Original Encoded recipe:**

```
To_Base64('A-Za-z0-9+/=')
Label('encoder1')
ROT13(true,true,false,7)
Split('H0','H0\\n')
Jump('encoder1',8)
Fork('\\n','\\n',false)
Zlib_Deflate('Dynamic Huffman Coding')
XOR({'option':'UTF8','string':'h0pp3r'},'Standard',false)
To_Base32('A-Z2-7=')
Merge(true)
Generate_Image('Greyscale',1,512)
```

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
