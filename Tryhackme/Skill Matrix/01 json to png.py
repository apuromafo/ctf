import matplotlib.pyplot as plt
import numpy as np
import json
import os

# Configuración de rutas
input_folder = "json"
output_folder = "graficos_exportados"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def generar_grafico_fiel(filepath, filename):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data_json = json.load(f)
        
        skills = data_json['data']['skills']
        labels = [s['label'] for s in skills]
        values = [s['score'] for s in skills]
        num_vars = len(labels)

        # Ángulos empezando desde arriba (90 grados)
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        
        # Cerrar el loop
        values_plot = values + [values[0]]
        angles_plot = angles + [angles[0]]

        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
        
        # Ajustar orientación para que coincida con la imagen
        ax.set_theta_offset(np.pi / 2)
        ax.set_theta_direction(-1)

        # --- REPLICAR RED HEXAGONAL ---
        # Definir niveles de la red (20, 40, 60, 80, 100)
        grid_levels = [20, 40, 60, 80, 100]
        for level in grid_levels:
            # Crear polígono para cada nivel de la red
            grid_angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
            grid_angles += grid_angles[:1]
            grid_values = [level] * (num_vars + 1)
            ax.plot(grid_angles, grid_values, color='#e2e8f0', linestyle='--', linewidth=0.8, zorder=0)

        # Ocultar la rejilla circular por defecto
        ax.yaxis.grid(False)
        ax.xaxis.grid(True, color='#e2e8f0', linestyle='--', linewidth=0.8)

        # --- DIBUJAR DATOS ---
        thm_green = '#5eb95e'
        ax.plot(angles_plot, values_plot, color=thm_green, linewidth=2.5, zorder=3)
        ax.fill(angles_plot, values_plot, color=thm_green, alpha=0.25, zorder=2)

        # --- AÑADIR RÓTULOS DE DATOS Y ETIQUETAS ---
        for i, (angle, value) in enumerate(zip(angles, values)):
            # Posicionar el texto del score un poco más afuera del punto
            x_text = angle
            y_text = value + 7 if value < 95 else value - 10 # Evitar que se salga del borde
            
            # Rótulo del dato (el número)
            ax.text(x_text, y_text, f"{value}", color=thm_green, 
                    fontweight='bold', ha='center', va='center', size=10)
            
            # Etiqueta de la habilidad con flecha (ajustada para no solaparse)
            display_label = f"{labels[i]} ➔"
            # Calcular posición de la etiqueta
            label_radius = 125 
            ax.text(angle, label_radius, display_label, color='#64748b', 
                    fontweight='bold', ha='center', va='center', size=10)

        # Limpieza estética final
        ax.set_yticklabels([])
        ax.set_xticklabels([]) # Quitamos las default para usar las personalizadas arriba
        ax.spines['polar'].set_visible(False)
        plt.ylim(0, 110) # Espacio para las etiquetas

        # Título
        clean_name = filename.replace('.json', '').replace('_', ' ').upper()
        plt.title(f"SKILLS MATRIX: {clean_name}", size=14, color='#1e293b', pad=40, fontweight='bold')

        # Guardar
        output_path = os.path.join(output_folder, filename.replace('.json', '.png'))
        plt.savefig(output_path, bbox_inches='tight', dpi=120, facecolor='white')
        plt.close()
        return True
    except Exception as e:
        print(f"Error en {filename}: {e}")
        return False

# Ejecución
archivos = [f for f in os.listdir(input_folder) if f.endswith('.json')]
for archivo in archivos:
    if generar_grafico_fiel(os.path.join(input_folder, archivo), archivo):
        print(f"[+] Renderizado fiel completado: {archivo}")