from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox


conteo_reportes = {}


def validar_signos_vitales():
    """Valida que los campos numéricos tengan valores válidos y dentro de rangos fisiológicos razonables."""
    try:
        presion = entry_presion.get().strip()
        fc_str = entry_fc.get().strip()
        oxigeno_str = entry_oxigeno.get().strip()
        peso_str = entry_peso.get().strip()
        talla_str = entry_talla.get().strip()

        
        if not all([presion, fc_str, oxigeno_str, peso_str, talla_str]):
            messagebox.showwarning(
                "Signos Vitales Incompletos",
                "Por favor, completa todos los campos de signos vitales para una evaluación precisa.",
            )
            return None

       
        fc = int(fc_str)
        oxigeno = float(oxigeno_str)
        peso = float(peso_str)
        talla = float(talla_str)

        if not (30 <= fc <= 220):
            messagebox.showerror("Error en FC", "La Frecuencia Cardíaca debe estar entre 30 y 220 bpm.")
            return None

        if not (50 <= oxigeno <= 100):
            messagebox.showerror("Error en Oxigenación", " La Saturación de Oxígeno debe estar entre 50% y 100%.")
            return None

        if peso <= 0 or talla <= 0:
            messagebox.showerror("Error en Peso/Talla", "El peso y la talla deben ser valores mayores a 0.")
            return None

        return {
            "presion": presion,
            "fc": fc,
            "oxigeno": oxigeno,
            "peso": peso,
            "talla": talla,
        }

    except ValueError:
        messagebox.showerror(
            "Entrada Inválida",
            "Por favor, ingresa números válidos para Frecuencia Cardíaca, Oxigenación, Peso y Talla.",
        )
        return None


def procesar_diagnostico():
    nombre = entry_nombre.get().strip()
    direccion = entry_direccion.get().strip()
    especialidad = entry_especialidad.get().strip()

    
    if not nombre or not direccion:
        messagebox.showwarning(
            "Campos Incompletos",
            "Por favor, ingresa al menos el Nombre y la Dirección del paciente.",
        )
        return

    
    vitales = validar_signos_vitales()
    if vitales is None:
        return  

    f = var_fiebre.get()
    t = var_tos.get()
    d = var_dolor.get()

    
    if vitales["oxigeno"] < 90:
        diagnostico = "Alerta de Hipoxia / Saturación baja de oxígeno"
        urgencia = "ALTA (CRÍTICA)"
        atencion = "URGENCIAS (Atención inmediata)"
    elif f and t:
        diagnostico = "Posible infección respiratoria"
        urgencia = "ALTA"
        atencion = "URGENCIAS (Atención prioritaria)"
    elif t and d:
        diagnostico = "Posible irritación respiratoria"
        urgencia = "MEDIA"
        atencion = "CITA MISMO DÍA"
    elif f:
        diagnostico = "Se recomienda valoración profesional por cuadro febril"
        urgencia = "MEDIA"
        atencion = "CITA MISMO DÍA"
    else:
        diagnostico = "No se identificó un patrón de alarma"
        urgencia = "NORMAL"
        atencion = "CITA PROGRAMADA"

   
    hoy = datetime.now()

    if urgencia.startswith("ALTA"):
        fecha_cita = hoy.strftime("%d/%m/%Y (HOY - INMEDIATO)")
    elif urgencia == "MEDIA":
        fecha_cita = hoy.strftime("%d/%m/%Y (MISMO DÍA)")
    else:
        
        fecha_cita = (hoy + timedelta(days=3)).strftime("%d/%m/%Y")

   
    clave_usuario = (nombre.lower(), direccion.lower())
    conteo_reportes[clave_usuario] = conteo_reportes.get(clave_usuario, 0) + 1
    total_reportes = conteo_reportes[clave_usuario]

    historial = (
        "1er Reporte (Primer ingreso del paciente)"
        if total_reportes == 1
        else f"Reporte N° {total_reportes} (Paciente reincidente)"
    )

    texto_reporte = (
        f"==========================================\n"
        f"          REPORTE DE DIAGNÓSTICO          \n"
        f"==========================================\n"
        f"Historial Paciente : {historial}\n"
        f"Nombre             : {nombre}\n"
        f"Dirección          : {direccion}\n"
        f"Especialidad       : {especialidad if especialidad else 'General'}\n"
        f"------------------------------------------\n"
        f"SIGNOS VITALES VALIDADOS:\n"
        f"  - Presión Arterial : {vitales['presion']}\n"
        f"  - Frec. Cardíaca   : {vitales['fc']} bpm\n"
        f"  - Oxigenación      : {vitales['oxigeno']} %\n"
        f"  - Peso / Talla     : {vitales['peso']} kg / {vitales['talla']} m\n"
        f"------------------------------------------\n"
        f"DIAGNÓSTICO Y TRIANJE:\n"
        f"  - Resultado        : {diagnostico}\n"
        f"  - Nivel Urgencia   : {urgencia}\n"
        f"  - Indicación       : {atencion}\n"
        f"  - Fecha Asignada   : {fecha_cita}\n"
        f"=========================================="
    )

    text_reporte.config(state="normal")
    text_reporte.delete("1.0", tk.END)
    text_reporte.insert(tk.END, texto_reporte)
    text_reporte.config(state="disabled")



COLOR_FONDO = "#1e1e2e"
COLOR_SECCION = "#2b2b3d"
COLOR_TEXTO = "#ffffff"
COLOR_ENTRADAS = "#3b3b4f"
COLOR_BOTON = "#007acc"
COLOR_REPORTE = "#000000"
COLOR_ALERTA = "#ffaa00"


ventana = tk.Tk()
ventana.title("Sistema de Diagnóstico Médico")
ventana.geometry("640x790")
ventana.config(bg=COLOR_FONDO)


frame_etico = tk.Frame(ventana, bg=COLOR_ALERTA, padx=5, pady=5)
frame_etico.pack(fill="x", padx=10, pady=5)

lbl_disclaimer = tk.Label(
    frame_etico,
    text="⚠️ AVISO: Sistema educativo. No sustituye la valoración médica profesional.",
    bg=COLOR_ALERTA,
    fg="black",
    font=("Arial", 8, "bold"),
    wraplength=600,
)
lbl_disclaimer.pack()

  
frame_datos = tk.LabelFrame(
    ventana,
    text=" Datos del Paciente ",
    bg=COLOR_SECCION,
    fg=COLOR_TEXTO,
    font=("Arial", 10, "bold"),
)
frame_datos.pack(fill="x", padx=10, pady=5)

tk.Label(frame_datos, text="Nombre *:", bg=COLOR_SECCION, fg=COLOR_TEXTO).grid(
    row=0, column=0, sticky="w", padx=5, pady=3
)
entry_nombre = tk.Entry(
    frame_datos, width=30, bg=COLOR_ENTRADAS, fg=COLOR_TEXTO, insertbackground="white"
)
entry_nombre.grid(row=0, column=1, padx=5, pady=3)

tk.Label(frame_datos, text="Dirección *:", bg=COLOR_SECCION, fg=COLOR_TEXTO).grid(
    row=1, column=0, sticky="w", padx=5, pady=3
)
entry_direccion = tk.Entry(
    frame_datos, width=30, bg=COLOR_ENTRADAS, fg=COLOR_TEXTO, insertbackground="white"
)
entry_direccion.grid(row=1, column=1, padx=5, pady=3)

tk.Label(frame_datos, text="Especialidad:", bg=COLOR_SECCION, fg=COLOR_TEXTO).grid(
    row=2, column=0, sticky="w", padx=5, pady=3
)
entry_especialidad = tk.Entry(
    frame_datos, width=30, bg=COLOR_ENTRADAS, fg=COLOR_TEXTO, insertbackground="white"
)
entry_especialidad.grid(row=2, column=1, padx=5, pady=3)

# Frame Signos Vitales
frame_vitales = tk.LabelFrame(
    ventana,
    text=" Signos Vitales (Obligatorios) ",
    bg=COLOR_SECCION,
    fg=COLOR_TEXTO,
    font=("Arial", 10, "bold"),
)
frame_vitales.pack(fill="x", padx=10, pady=5)

tk.Label(frame_vitales, text="Presión (ej. 120/80):", bg=COLOR_SECCION, fg=COLOR_TEXTO).grid(
    row=0, column=0, padx=5, pady=3
)
entry_presion = tk.Entry(
    frame_vitales, width=10, bg=COLOR_ENTRADAS, fg=COLOR_TEXTO, insertbackground="white"
)
entry_presion.grid(row=0, column=1, padx=5)

tk.Label(frame_vitales, text="Frec. Cardíaca (bpm):", bg=COLOR_SECCION, fg=COLOR_TEXTO).grid(
    row=0, column=2, padx=5, pady=3
)
entry_fc = tk.Entry(
    frame_vitales, width=10, bg=COLOR_ENTRADAS, fg=COLOR_TEXTO, insertbackground="white"
)
entry_fc.grid(row=0, column=3, padx=5)

tk.Label(frame_vitales, text="Oxigenación (%):", bg=COLOR_SECCION, fg=COLOR_TEXTO).grid(
    row=1, column=0, padx=5, pady=3
)
entry_oxigeno = tk.Entry(
    frame_vitales, width=10, bg=COLOR_ENTRADAS, fg=COLOR_TEXTO, insertbackground="white"
)
entry_oxigeno.grid(row=1, column=1, padx=5)

tk.Label(frame_vitales, text="Peso (kg):", bg=COLOR_SECCION, fg=COLOR_TEXTO).grid(
    row=1, column=2, padx=5, pady=3
)
entry_peso = tk.Entry(
    frame_vitales, width=10, bg=COLOR_ENTRADAS, fg=COLOR_TEXTO, insertbackground="white"
)
entry_peso.grid(row=1, column=3, padx=5)

tk.Label(frame_vitales, text="Talla (m, ej. 1.70):", bg=COLOR_SECCION, fg=COLOR_TEXTO).grid(
    row=2, column=0, padx=5, pady=3
)
entry_talla = tk.Entry(
    frame_vitales, width=10, bg=COLOR_ENTRADAS, fg=COLOR_TEXTO, insertbackground="white"
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
    activebackground="#005999",
    activeforeground="white",
)
btn_generar.pack(pady=10)

# Cuadro de Salida del Reporte
text_reporte = tk.Text(
    ventana,
    height=15,
    width=65,
    font=("Consolas", 9),
    bg=COLOR_REPORTE,
    fg="#e6e6fa",
    insertbackground="white",
)
text_reporte.pack(padx=10, pady=5)
text_reporte.config(state="disabled")

ventana.mainloop()