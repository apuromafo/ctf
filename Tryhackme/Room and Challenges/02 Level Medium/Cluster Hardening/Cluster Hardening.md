# Cluster Hardening [MEDIUM]

https://tryhackme.com/room/clusterhardening

1. No answer needed
2. 1. Kubernetes cluster
   2. Security-first
3. 1. security benchmarks
   2. 4.2.1
   3. Kube-bench
4. 1. 10250
   2. authentication:anonymous:enabled
   3. API Bearer Token
5. 1. Kube-apiserver
   2. 1.2.24 - 27
6. 1. Mutating
   2. EventRateLimit
   3. Admission Controller Webhooks 
   4. ValidatingAdmissionWebhook, MutatingAdmissionWebhook
7. 1. NetworkPolicy
   2. spec:PodSelector:matchLabels:app
8. U3BlYzoKICBQb2RTZWxlY3RvcjogICAgIGFwcD1iYWNrZW5kLXNlcnZpY2UyCiAgQWxsb3dpbmcgaW5ncmVzcyB0cmFmZmljOgogICAgVG8gUG9ydDogODg4OC9UQ1AKICAgIEZyb206CiAgICAgIFBvZFNlbGVjdG9yOiBhcHA9YmFja2VuZC1zZXJ2aWNlMQogIE5vdCBhZmZlY3RpbmcgZWdyZXNzIHRyYWZmaWMKICBQb2xpY3kgVHlwZXM6IEluZ3Jlc3M=

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
