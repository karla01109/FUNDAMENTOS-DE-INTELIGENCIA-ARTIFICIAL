from datetime import datetime, timedelta
import random
import tkinter as tk
from tkinter import messagebox

conteo_reportes = {}


def procesar_diagnostico():
    nombre = entry_nombre.get().strip()
    direccion = entry_direccion.get().strip()
    tipo_equipo = combo_tipo.get().strip()

    
    if not nombre or not direccion or not tipo_equipo:
        messagebox.showwarning(
            "Campos Incompletos",
            "Por favor, ingresa el Nombre, Dirección y Tipo de Equipo.",
        )
        return

  
    electricidad = var_electricidad.get()
    enciende = var_enciende.get()
    imagen = var_imagen.get()
    sistema = var_sistema.get()
    lento = var_lento.get()

    
    if not electricidad:
        diagnostico = "Sin alimentación eléctrica o falla en la red/cableado."
        recomendacion = "Verificar cable de poder, regulador, contacto o fuente de alimentación."
        nivel = "ALTA"
        atencion = "REVISIÓN INMEDIATA EN TALLER"
    elif not enciende:
        diagnostico = "El equipo recibe electricidad pero no enciende."
        recomendacion = "Revisar fuente de poder, botón de encendido, batería o tarjeta madre."
        nivel = "ALTA"
        atencion = "REVISIÓN INMEDIATA EN TALLER"
    elif not imagen:
        diagnostico = "El equipo enciende pero no muestra imagen."
        recomendacion = "Revisar cable de video, monitor, memoria RAM o tarjeta gráfica."
        nivel = "MEDIA"
        atencion = "ATENCIÓN EN EL DÍA"
    elif not sistema:
        diagnostico = "El equipo muestra imagen pero no inicia el sistema operativo."
        recomendacion = "Revisar disco duro/SSD, archivos de arranque, memoria RAM o BIOS."
        nivel = "MEDIA"
        atencion = "ATENCIÓN EN EL DÍA"
    elif lento:
        diagnostico = "El equipo funciona pero presenta bajo rendimiento o lentitud."
        recomendacion = "Revisar uso de memoria RAM, programas de inicio, almacenamiento o malware."
        nivel = "BAJA"
        atencion = "MANTENIMIENTO PROGRAMADO"
    else:
        diagnostico = "Funcionamiento básico correcto sin fallas detectadas."
        recomendacion = "Se sugiere mantenimiento preventivo de rutina."
        nivel = "NORMAL"
        atencion = "SEGUIMIENTO RUTINARIO"

   
    hoy = datetime.now()
    if nivel == "ALTA":
        fecha_cita = hoy.strftime("%d/%m/%Y (HOY - URGENTE)")
    elif nivel == "MEDIA":
        fecha_cita = hoy.strftime("%d/%m/%Y (MISMO DÍA)")
    elif nivel == "BAJA":
        fecha_cita = (hoy + timedelta(days=2)).strftime("%d/%m/%Y")
    else:
        fecha_cita = (hoy + timedelta(days=5)).strftime("%d/%m/%Y")

    
    clave_usuario = (nombre.lower(), direccion.lower())
    conteo_reportes[clave_usuario] = conteo_reportes.get(clave_usuario, 0) + 1
    total_reportes = conteo_reportes[clave_usuario]

    folio = f"REP-{random.randint(10000, 99999)}"
    historial = (
        "1er Ingreso (Equipo Nuevo en Taller)"
        if total_reportes == 1
        else f"Ingreso N° {total_reportes} (Cliente Reincidente)"
    )

    texto_reporte = (
        f"==========================================\n"
        f"       REPORTE DE DIAGNÓSTICO TÉCNICO      \n"
        f"==========================================\n"
        f"Folio de Reporte   : {folio}\n"
        f"Historial Cliente  : {historial}\n"
        f"Fecha y Hora       : {hoy.strftime('%d/%m/%Y %H:%M')}\n"
        f"------------------------------------------\n"
        f"DATOS DEL CLIENTE Y EQUIPO:\n"
        f"  - Nombre Cliente : {nombre}\n"
        f"  - Dirección      : {direccion}\n"
        f"  - Tipo de Equipo : {tipo_equipo}\n"
        f"------------------------------------------\n"
        f"DIAGNÓSTICO Y TRIAJE TÉCNICO:\n"
        f"  - Resultado      : {diagnostico}\n"
        f"  - Prioridad      : {nivel}\n"
        f"  - Recomendación  : {recomendacion}\n"
        f"  - Indicación     : {atencion}\n"
        f"  - Fecha Cita     : {fecha_cita}\n"
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
ventana.title("Sistema de Diagnóstico Técnico de Cómputo")
ventana.geometry("640x800")
ventana.config(bg=COLOR_FONDO)


frame_etico = tk.Frame(ventana, bg=COLOR_ALERTA, padx=5, pady=5)
frame_etico.pack(fill="x", padx=10, pady=5)

lbl_disclaimer = tk.Label(
    frame_etico,
    text="⚠️ AVISO: Sistema educativo. No reemplaza la inspección física de un especialista.",
    bg=COLOR_ALERTA,
    fg="black",
    font=("Arial", 8, "bold"),
    wraplength=600,
)
lbl_disclaimer.pack()

# Frame Datos del Cliente y Equipo
frame_datos = tk.LabelFrame(
    ventana,
    text=" Datos del Cliente y Equipo ",
    bg=COLOR_SECCION,
    fg=COLOR_TEXTO,
    font=("Arial", 10, "bold"),
)
frame_datos.pack(fill="x", padx=10, pady=5)

tk.Label(frame_datos, text="Nombre Cliente *:", bg=COLOR_SECCION, fg=COLOR_TEXTO).grid(
    row=0, column=0, sticky="w", padx=5, pady=3
)
entry_nombre = tk.Entry(
    frame_datos, width=32, bg=COLOR_ENTRADAS, fg=COLOR_TEXTO, insertbackground="white"
)
entry_nombre.grid(row=0, column=1, padx=5, pady=3)

tk.Label(frame_datos, text="Dirección *:", bg=COLOR_SECCION, fg=COLOR_TEXTO).grid(
    row=1, column=0, sticky="w", padx=5, pady=3
)
entry_direccion = tk.Entry(
    frame_datos, width=32, bg=COLOR_ENTRADAS, fg=COLOR_TEXTO, insertbackground="white"
)
entry_direccion.grid(row=1, column=1, padx=5, pady=3)

tk.Label(frame_datos, text="Tipo de Equipo *:", bg=COLOR_SECCION, fg=COLOR_TEXTO).grid(
    row=2, column=0, sticky="w", padx=5, pady=3
)
combo_tipo = tk.Entry(
    frame_datos, width=32, bg=COLOR_ENTRADAS, fg=COLOR_TEXTO, insertbackground="white"
)
combo_tipo.insert(0, "Laptop")
combo_tipo.grid(row=2, column=1, padx=5, pady=3)


frame_sintomas = tk.LabelFrame(
    ventana,
    text=" Estado y Síntomas del Equipo ",
    bg=COLOR_SECCION,
    fg=COLOR_TEXTO,
    font=("Arial", 10, "bold"),
)
frame_sintomas.pack(fill="x", padx=10, pady=5)

var_electricidad = tk.BooleanVar(value=True)
var_enciende = tk.BooleanVar(value=True)
var_imagen = tk.BooleanVar(value=True)
var_sistema = tk.BooleanVar(value=True)
var_lento = tk.BooleanVar(value=False)

tk.Checkbutton(
    frame_sintomas,
    text="¿Tiene corriente / alimentación eléctrica?",
    variable=var_electricidad,
    bg=COLOR_SECCION,
    fg=COLOR_TEXTO,
    selectcolor=COLOR_ENTRADAS,
    activebackground=COLOR_SECCION,
).pack(anchor="w", padx=10)

tk.Checkbutton(
    frame_sintomas,
    text="¿El equipo enciende (luces/ventiladores)?",
    variable=var_enciende,
    bg=COLOR_SECCION,
    fg=COLOR_TEXTO,
    selectcolor=COLOR_ENTRADAS,
    activebackground=COLOR_SECCION,
).pack(anchor="w", padx=10)

tk.Checkbutton(
    frame_sintomas,
    text="¿Muestra imagen en la pantalla?",
    variable=var_imagen,
    bg=COLOR_SECCION,
    fg=COLOR_TEXTO,
    selectcolor=COLOR_ENTRADAS,
    activebackground=COLOR_SECCION,
).pack(anchor="w", padx=10)

tk.Checkbutton(
    frame_sintomas,
    text="¿Inicia el Sistema Operativo completamente?",
    variable=var_sistema,
    bg=COLOR_SECCION,
    fg=COLOR_TEXTO,
    selectcolor=COLOR_ENTRADAS,
    activebackground=COLOR_SECCION,
).pack(anchor="w", padx=10)

tk.Checkbutton(
    frame_sintomas,
    text="¿Presenta lentitud o bajo rendimiento?",
    variable=var_lento,
    bg=COLOR_SECCION,
    fg=COLOR_TEXTO,
    selectcolor=COLOR_ENTRADAS,
    activebackground=COLOR_SECCION,
).pack(anchor="w", padx=10)

# Botón Generar
btn_generar = tk.Button(
    ventana,
    text="Generar Diagnóstico Técnico",
    command=procesar_diagnostico,
    bg=COLOR_BOTON,
    fg="white",
    font=("Arial", 10, "bold"),
    activebackground="#005999",
    activeforeground="white",
)
btn_generar.pack(pady=10)


text_reporte = tk.Text(
    ventana,
    height=15,
    width=65,
    font=("Consolas", 9),
    bg=COLOR_REPORTE,
    fg="#00ff66",
    insertbackground="white",
)
text_reporte.pack(padx=10, pady=5)
text_reporte.config(state="disabled")

ventana.mainloop()