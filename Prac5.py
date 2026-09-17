from datetime import datetime, timedelta
import random
import tkinter as tk
from tkinter import messagebox

# Diccionario global para el historial por Nombre + Dirección
conteo_reportes = {}


def procesar_diagnostico():
    nombre = entry_nombre.get().strip()
    direccion = entry_direccion.get().strip()
    presion = entry_presion.get().strip()
    fc = entry_fc.get().strip()
    oxigeno = entry_oxigeno.get().strip()
    peso = entry_peso.get().strip()
    talla = entry_talla.get().strip()
    especialidad = entry_especialidad.get().strip()

    if not nombre or not direccion:
        messagebox.showwarning(
            "Campos Incompletos",
            "Por favor, ingresa al menos el Nombre y la Dirección.",
        )
        return

    f = var_fiebre.get()
    t = var_tos.get()
    d = var_dolor.get()

    if f and t:
        diagnostico = "Posible infección respiratoria"
        urgencia = "ALTA"
        atencion = "URGENCIAS (Atención inmediata)"
    elif t and d:
        diagnostico = "Posible irritación respiratoria"
        urgencia = "MEDIA"
        atencion = "CITA MISMO DÍA"
    elif f:
        diagnostico = "Se recomienda valoración profesional"
        urgencia = "MEDIA"
        atencion = "CITA MISMO DÍA"
    else:
        diagnostico = "No se identificó un patrón grave"
        urgencia = "NORMAL"
        atencion = "CITA OTRO DÍA"

    dias_aleatorios = random.randint(1, 7)
    fecha_cita = (datetime.now() + timedelta(days=dias_aleatorios)).strftime(
        "%d/%m/%Y"
    )

    clave_usuario = (nombre.lower(), direccion.lower())
    conteo_reportes[clave_usuario] = conteo_reportes.get(clave_usuario, 0) + 1
    total_reportes = conteo_reportes[clave_usuario]

    if total_reportes == 1:
        historial = "1er Reporte (Primer ingreso del paciente)"
    else:
        historial = f"Reporte N° {total_reportes} (Paciente reincidente)"

    texto_reporte = (
        f"==========================================\n"
        f"          REPORTE DE DIAGNÓSTICO          \n"
        f"==========================================\n"
        f"Historial Paciente : {historial}\n"
        f"Nombre             : {nombre}\n"
        f"Dirección          : {direccion}\n"
        f"Especialidad       : {especialidad}\n"
        f"------------------------------------------\n"
        f"SIGNOS VITALES:\n"
        f"  - Presión Arterial : {presion}\n"
        f"  - Frec. Cardíaca   : {fc} bpm\n"
        f"  - Oxigenación      : {oxigeno} %\n"
        f"  - Peso / Talla     : {peso} kg / {talla}\n"
        f"------------------------------------------\n"
        f"DIAGNÓSTICO Y CITA:\n"
        f"  - Resultado        : {diagnostico}\n"
        f"  - Nivel Urgencia   : {urgencia}\n"
        f"  - Indicación       : {atencion}\n"
        f"  - Fecha Programada : {fecha_cita}\n"
        f"=========================================="
    )

    text_reporte.config(state="normal")
    text_reporte.delete("1.0", tk.END)
    text_reporte.insert(tk.END, texto_reporte)
    text_reporte.config(state="disabled")


# --- CONFIGURACIÓN DE PALETA DE COLORES ---
COLOR_FONDO = "#1e1e2e"  # Oscuro principal
COLOR_SECCION = "#2b2b3d"  # Oscuro para marcos
COLOR_TEXTO = "#ffffff"  # Texto blanco
COLOR_ENTRADAS = "#3b3b4f"  # Fondo cuadros de texto
COLOR_BOTON = "#007acc"  # Azul para botón
COLOR_REPORTE = "#000000"  # Fondo área de reporte

# --- VENTANA PRINCIPAL ---
ventana = tk.Tk()
ventana.title("Sistema de Diagnóstico Médico")
ventana.geometry("620x720")
ventana.config(bg=COLOR_FONDO)

# Frame Datos Personales
frame_datos = tk.LabelFrame(
    ventana,
    text=" Datos del Paciente ",
    bg=COLOR_SECCION,
    fg=COLOR_TEXTO,
    font=("Arial", 10, "bold"),
)
frame_datos.pack(fill="x", padx=10, pady=5)

tk.Label(
    frame_datos, text="Nombre:", bg=COLOR_SECCION, fg=COLOR_TEXTO
).grid(row=0, column=0, sticky="w", padx=5, pady=3)
entry_nombre = tk.Entry(
    frame_datos,
    width=30,
    bg=COLOR_ENTRADAS,
    fg=COLOR_TEXTO,
    insertbackground="white",
)
entry_nombre.grid(row=0, column=1, padx=5, pady=3)

tk.Label(
    frame_datos, text="Dirección:", bg=COLOR_SECCION, fg=COLOR_TEXTO
).grid(row=1, column=0, sticky="w", padx=5, pady=3)
entry_direccion = tk.Entry(
    frame_datos,
    width=30,
    bg=COLOR_ENTRADAS,
    fg=COLOR_TEXTO,
    insertbackground="white",
)
entry_direccion.grid(row=1, column=1, padx=5, pady=3)

tk.Label(
    frame_datos, text="Especialidad:", bg=COLOR_SECCION, fg=COLOR_TEXTO
).grid(row=2, column=0, sticky="w", padx=5, pady=3)
entry_especialidad = tk.Entry(
    frame_datos,
    width=30,
    bg=COLOR_ENTRADAS,
    fg=COLOR_TEXTO,
    insertbackground="white",
)
entry_especialidad.grid(row=2, column=1, padx=5, pady=3)

# Frame Signos Vitales
frame_vitales = tk.LabelFrame(
    ventana,
    text=" Signos Vitales ",
    bg=COLOR_SECCION,
    fg=COLOR_TEXTO,
    font=("Arial", 10, "bold"),
)
frame_vitales.pack(fill="x", padx=10, pady=5)

tk.Label(
    frame_vitales, text="Presión Arterial:", bg=COLOR_SECCION, fg=COLOR_TEXTO
).grid(row=0, column=0, padx=5, pady=3)
entry_presion = tk.Entry(
    frame_vitales,
    width=10,
    bg=COLOR_ENTRADAS,
    fg=COLOR_TEXTO,
    insertbackground="white",
)
entry_presion.grid(row=0, column=1, padx=5)

tk.Label(
    frame_vitales,
    text="Frec. Cardíaca (bpm):",
    bg=COLOR_SECCION,
    fg=COLOR_TEXTO,
).grid(row=0, column=2, padx=5, pady=3)
entry_fc = tk.Entry(
    frame_vitales,
    width=10,
    bg=COLOR_ENTRADAS,
    fg=COLOR_TEXTO,
    insertbackground="white",
)
entry_fc.grid(row=0, column=3, padx=5)

tk.Label(
    frame_vitales, text="Oxigenación (%):", bg=COLOR_SECCION, fg=COLOR_TEXTO
).grid(row=1, column=0, padx=5, pady=3)
entry_oxigeno = tk.Entry(
    frame_vitales,
    width=10,
    bg=COLOR_ENTRADAS,
    fg=COLOR_TEXTO,
    insertbackground="white",
)
entry_oxigeno.grid(row=1, column=1, padx=5)

tk.Label(
    frame_vitales, text="Peso (kg):", bg=COLOR_SECCION, fg=COLOR_TEXTO
).grid(row=1, column=2, padx=5, pady=3)
entry_peso = tk.Entry(
    frame_vitales,
    width=10,
    bg=COLOR_ENTRADAS,
    fg=COLOR_TEXTO,
    insertbackground="white",
)
entry_peso.grid(row=1, column=3, padx=5)

tk.Label(
    frame_vitales, text="Talla:", bg=COLOR_SECCION, fg=COLOR_TEXTO
).grid(row=2, column=0, padx=5, pady=3)
entry_talla = tk.Entry(
    frame_vitales,
    width=10,
    bg=COLOR_ENTRADAS,
    fg=COLOR_TEXTO,
    insertbackground="white",
)
entry_talla.grid(row=2, column=1, padx=5)

# Frame Síntomas
frame_sintomas = tk.LabelFrame(
    ventana,
    text=" Síntomas ",
    bg=COLOR_SECCION,
    fg=COLOR_TEXTO,
    font=("Arial", 10, "bold"),
)
frame_sintomas.pack(fill="x", padx=10, pady=5)

var_fiebre = tk.BooleanVar()
var_tos = tk.BooleanVar()
var_dolor = tk.BooleanVar()

tk.Checkbutton(
    frame_sintomas,
    text="Fiebre",
    variable=var_fiebre,
    bg=COLOR_SECCION,
    fg=COLOR_TEXTO,
    selectcolor=COLOR_ENTRADAS,
    activebackground=COLOR_SECCION,
).pack(anchor="w", padx=10)
tk.Checkbutton(
    frame_sintomas,
    text="Tos",
    variable=var_tos,
    bg=COLOR_SECCION,
    fg=COLOR_TEXTO,
    selectcolor=COLOR_ENTRADAS,
    activebackground=COLOR_SECCION,
).pack(anchor="w", padx=10)
tk.Checkbutton(
    frame_sintomas,
    text="Dolor de garganta",
    variable=var_dolor,
    bg=COLOR_SECCION,
    fg=COLOR_TEXTO,
    selectcolor=COLOR_ENTRADAS,
    activebackground=COLOR_SECCION,
).pack(anchor="w", padx=10)

# Botón Generar
btn_generar = tk.Button(
    ventana,
    text="Generar Diagnóstico",
    command=procesar_diagnostico,
    bg=COLOR_BOTON,
    fg="white",
    font=("Arial", 10, "bold"),
    activebackground="#bfff00",
    activeforeground="white",
)
btn_generar.pack(pady=10)

# Cuadro de Salida del Reporte
text_reporte = tk.Text(
    ventana,
    height=16,
    width=65,
    font=("Consolas", 9),
    bg=COLOR_REPORTE,
    fg="#e6e6fa",
    insertbackground="white",
)
text_reporte.pack(padx=10, pady=5)
text_reporte.config(state="disabled")

ventana.mainloop()