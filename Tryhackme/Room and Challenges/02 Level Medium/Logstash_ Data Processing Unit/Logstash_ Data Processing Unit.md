# Logstash_ Data Processing Unit [MEDIUM]

1. No answer needed
2. No answer needed
3. 1. 9200
   2. 8.8.1
   3. systemctl status elasticsearch.service
   4. 192.168.0.1
4. 1. 3s
   2. 8.8.1
5. 1. 5601
   2. 3
   3. No answer needed
6. 1. Mutate
   2. drop
   3. grok
7. 1. nay
   2. path
   3. columns
   4. elasticsearch
8. 1. tcp
   2. csv
9. 1. prune
   2. mutate
   3. rename => { "src_ip" => "source_ip" }
10. 1. yay
    2. stdout
    3. syslog,host,port
11. 1. logstash -f logstash.conf
    2. stdin,csv,stdout
12. No answer needed

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
