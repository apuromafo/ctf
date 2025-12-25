import collections
import random

def realizar_quiz_ciberseguridad():
    # --- DISCLAIMER INICIAL ---
    print("\n" + "!"*70)
    print("[!] AVISO: Este test es una herramienta de orientación basada en preferencias.")
    print("[!] Los resultados sugieren roles en ciberseguridad, pero no limitan tu potencial.")
    print("!"*70 + "\n")

    print("="*75)
    print("   TRYHACKME CAREER QUIZ - VERSIÓN PYTHON")
    print(" Inspirado en https://tryhackme.com/careers/quiz ")
    print("="*75)

    # Perfiles con sus links y descripciones exactas del código fuente
    perfiles = {
        "a": {
            "title": "Penetration Tester",
            "url": "https://tryhackme.com/careers/penetration-tester",
            "desc": "El rol de un penetration tester es probar la seguridad de los sistemas y el software mediante intentos sistemáticos de descubrir fallas y vulnerabilidades a través del hacking. Explotas estas vulnerabilidades para evaluar el riesgo en cada instancia."
        },
        "e": {
            "title": "Security Analyst",
            "url": "https://tryhackme.com/careers/cyber-security-analyst",
            "desc": "Los analistas de seguridad son integrales para construir medidas de seguridad, protegiendo a la empresa de ataques. Exploran y evalúan las redes de la compañía para descubrir datos accionables y recomendaciones para medidas preventivas."
        },
        "b": {
            "title": "Security Engineer",
            "url": "https://tryhackme.com/careers/security-engineer",
            "desc": "Los ingenieros de seguridad desarrollan e implementan soluciones utilizando datos de amenazas y vulnerabilidades. Trabajan evitando una amplia gama de ataques, incluyendo aplicaciones web y amenazas de red."
        },
        "d": {
            "title": "Red Teamer",
            "url": "https://tryhackme.com/careers/red-teamer",
            "desc": "A diferencia del pentesting, los red teamers prueban las capacidades de detección y respuesta de la empresa. Requiere imitar acciones de criminales cibernéticos, emular ataques maliciosos, mantener el acceso y evitar la detección."
        },
        "c": {
            "title": "Incident Responder",
            "url": "https://tryhackme.com/careers/incident-responder",
            "desc": "Responden de manera productiva a las brechas de seguridad. Creas planes, políticas y protocolos. Es una posición de alta presión con respuestas requeridas en tiempo real mientras los ataques se desarrollan."
        }
    }

    # Las 10 preguntas del objeto K (0-9)
    banco_preguntas = [
        {"q": "¿Qué aspecto de la ciberseguridad te interesa más?", "options": [("a", "Encontrar vulnerabilidades y explotarlas."), ("b", "Construir y mantener sistemas seguros."), ("c", "Responder y mitigar incidentes de seguridad."), ("d", "Simular ataques reales para mejorar defensas."), ("e", "Monitorear y analizar eventos en tiempo real.")]},
        {"q": "¿Cuál es tu mayor fortaleza?", "options": [("a", "Experimentar con diferentes herramientas y técnicas."), ("b", "Aprender nuevas tecnologías e implementar medidas."), ("c", "Resolución de problemas y pensar rápido bajo presión."), ("d", "Planificación y estrategia para escenarios complejos."), ("e", "Analizar datos e identificar patrones.")]},
        {"q": "¿Qué tipo de entorno de trabajo te sienta mejor?", "options": [("a", "Trabajar de forma independiente en tareas específicas."), ("b", "Colaborar con un equipo para diseñar soluciones."), ("c", "Situaciones de alta presión y manejo de emergencias."), ("d", "Participar en simulaciones adversarias."), ("e", "Ser parte de un equipo de monitoreo continuo.")]},
        {"q": "¿Cómo manejas los desafíos o contratiempos?", "options": [("a", "Superar obstáculos con soluciones creativas."), ("b", "Analizar la situación, aprender y mejorar."), ("c", "Mantener la calma y resolver eficientemente."), ("d", "Ver desafíos como oportunidades para perfeccionar técnicas."), ("e", "Mantener la calma y seguir los procedimientos (SOP).")]},
        {"q": "¿Qué habilidad consideras más importante?", "options": [("a", "Competencia técnica y herramientas de hacking."), ("b", "Conocimiento de arquitectura de redes y sistemas."), ("c", "Pensamiento crítico y decisiones bajo estrés."), ("d", "Pensamiento estratégico y tácticas del adversario."), ("e", "Atención al detalle y detección de anomalías.")]},
        {"q": "Si tuvieras un gadget de espía, ¿cuál elegirías?", "options": [("a", "Reportinator: Genera reportes automáticos de hallazgos."), ("b", "Varita de Implementación: Aplica las mejores defensas al instante."), ("c", "Trace2Face: Rastrea la huella digital hasta el culpable."), ("d", "Rent-a-brain: Te permite pensar como una amenaza APT."), ("e", "CyberLens: Reconoce falsos positivos al instante.")]},
        {"q": "¿Qué escenario estimularía más tu cerebro?", "options": [("a", "Puzzles para romper medidas de seguridad."), ("b", "Construir sistemas resilientes y seguros."), ("c", "Gestión de crisis e incidentes urgentes."), ("d", "Encontrar agujeros simulando ser un atacante."), ("e", "Analizar datos para detectar amenazas ocultas.")]},
        {"q": "¿Cómo te sientes trabajando en equipo?", "options": [("a", "Prefiero trabajar de forma independiente."), ("b", "Colaborar para lograr objetivos comunes."), ("c", "Prosperar en equipo durante situaciones de presión."), ("d", "Trabajar en equipo para planear y ejecutar ataques."), ("e", "Mezcla de trabajo independiente y colaboración.")]},
        {"q": "¿Qué es lo más gratificante de esta carrera?", "options": [("a", "Descubrir vulnerabilidades críticas."), ("b", "Construir sistemas que protegen activos valiosos."), ("c", "Mitigar incidentes y brechas de seguridad."), ("d", "Superar defensas y probar medidas de seguridad."), ("e", "Proveer protección continua mediante el análisis.")]},
        {"q": "¿Cómo abordas el aprendizaje constante?", "options": [("a", "Experimentando con herramientas de forma práctica."), ("b", "Investigación y formación sobre nuevos desarrollos."), ("c", "Aprendiendo de incidentes reales y sus lecciones."), ("d", "Ejercicios prácticos y simulaciones de combate."), ("e", "Leyendo blogs técnicos entre alertas de seguridad.")]}
    ]

    random.shuffle(banco_preguntas)
    respuestas_usuario = []

    for i, p in enumerate(banco_preguntas):
        print(f"\n[{i+1}/10] {p['q']}")
        opciones = p['options'][:]
        random.shuffle(opciones)
        
        for idx, (letra, texto) in enumerate(opciones):
            print(f"  {idx + 1}. {texto}")
        
        while True:
            try:
                sel = int(input("\nRespuesta (1-5): "))
                if 1 <= sel <= 5:
                    respuestas_usuario.append(opciones[sel-1][0])
                    break
                else: print("Error: Selecciona entre 1 y 5.")
            except ValueError: print("Error: Ingresa un número válido.")

    # Resultado Final
    conteo = collections.Counter(respuestas_usuario)
    ganador = conteo.most_common(1)[0][0]
    perfil = perfiles[ganador]

    print("\n" + "#"*75)
    print(f" RESULTADO FINAL: {perfil['title'].upper()}")
    print("-" * 75)
    print(f" DESCRIPCIÓN: {perfil['desc']}")
    print(f" MÁS INFORMACIÓN: {perfil['url']}")
    print("#"*75)

if __name__ == "__main__":
    realizar_quiz_ciberseguridad()