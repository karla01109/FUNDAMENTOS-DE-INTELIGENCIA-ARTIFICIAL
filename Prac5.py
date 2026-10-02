# ============================================================
# SISTEMA BÁSICO DE DIAGNÓSTICO DE EQUIPOS DE CÓMPUTO
# ============================================================
# Objetivo:
# Recibir información del usuario y del equipo,
# analizar diferentes condiciones y generar
# automáticamente un diagnóstico.
# ============================================================


# ------------------------------------------------------------
# 1. IMPORTAR LIBRERÍAS
# ------------------------------------------------------------

# datetime permite obtener la fecha y hora actuales.
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# random permite generar un número aleatorio.
import random


# ------------------------------------------------------------
# 2. GENERAR NÚMERO DE REPORTE
# ------------------------------------------------------------

# Generamos un número aleatorio entre 10000 y 99999.
numero = random.randint(10000, 99999)

# Creamos el identificador del reporte.
numero_reporte = "REP-" + str(numero)


# ------------------------------------------------------------
# 3. OBTENER FECHA Y HORA
# ------------------------------------------------------------

# datetime.now() obtiene la fecha y hora actuales.
fecha_hora = datetime.now()

# Convertimos la fecha a un formato fácil de leer.
fecha = fecha_hora.strftime("%d/%m/%Y")

# Convertimos la hora a formato HH:MM.
hora = fecha_hora.strftime("%H:%M")


# ------------------------------------------------------------
# 4. DATOS DEL USUARIO
# ------------------------------------------------------------

print("\n==========================================")
print(" SISTEMA DE DIAGNÓSTICO DE EQUIPOS")
print("==========================================")

print("\nDATOS DEL USUARIO")

nombre = input("Nombre del usuario: ")

direccion = input("Dirección: ")


# ------------------------------------------------------------
# 5. DATOS DEL EQUIPO
# ------------------------------------------------------------

print("\nDATOS DEL EQUIPO")

print("\nSeleccione el tipo de equipo:")

print("1. Computadora de escritorio")
print("2. Laptop")
print("3. All in One")
print("4. Servidor")
print("5. Otro")

tipo_opcion = input("Seleccione una opción: ")


# ------------------------------------------------------------
# 6. CONVERTIR LA OPCIÓN EN UN TIPO DE EQUIPO
# ------------------------------------------------------------

if tipo_opcion == "1":
    tipo_equipo = "Computadora de escritorio"

elif tipo_opcion == "2":
    tipo_equipo = "Laptop"

elif tipo_opcion == "3":
    tipo_equipo = "All in One"

elif tipo_opcion == "4":
    tipo_equipo = "Servidor"

elif tipo_opcion == "5":
    tipo_equipo = input("Especifique el tipo de equipo: ")

else:
    tipo_equipo = "Tipo de equipo no especificado"


# ------------------------------------------------------------
# 7. RECIBIR INFORMACIÓN DEL EQUIPO
# ------------------------------------------------------------

print("\n==========================================")
print(" DIAGNÓSTICO")
print("==========================================")

print("\nResponda utilizando S para Sí o N para No.")

# Preguntamos si existe alimentación eléctrica.
electricidad = input("¿Tiene electricidad? (s/n): ").lower()


# ------------------------------------------------------------
# 8. VALIDAR LA RESPUESTA
# ------------------------------------------------------------

# Mientras la respuesta no sea s o n,
# volvemos a solicitarla.

while electricidad not in ["s", "n"]:

    print("Respuesta no válida.")

    electricidad = input("Ingrese solamente s o n: ").lower()


# ------------------------------------------------------------
# 9. PRIMERA DECISIÓN
# ------------------------------------------------------------

# Si NO existe electricidad,
# no tiene sentido preguntar si enciende.

if electricidad == "n":

    diagnostico = "Revisar alimentación eléctrica."

    recomendacion = "Verificar cable, contacto eléctrico, regulador o fuente de alimentación."

    nivel = "ALTA"


# ------------------------------------------------------------
# 10. CONTINUAR EL DIAGNÓSTICO
# ------------------------------------------------------------

else:

    # Ahora sí tiene sentido preguntar si enciende.

    enciende = input("¿El equipo enciende? (s/n): ").lower()

    while enciende not in ["s", "n"]:

        print("Respuesta no válida.")

        enciende = input("Ingrese solamente s o n: ").lower()


    # --------------------------------------------------------
    # SI NO ENCIENDE
    # --------------------------------------------------------

    if enciende == "n":

        diagnostico = "El equipo recibe electricidad pero no enciende."

        recomendacion = "Revisar fuente de poder, batería, botón de encendido o tarjeta madre."

        nivel = "ALTA"


    # --------------------------------------------------------
    # SI ENCIENDE
    # --------------------------------------------------------

    else:

        # Ahora tiene sentido preguntar si aparece imagen.

        imagen = input("¿Muestra imagen? (s/n): ").lower()

        while imagen not in ["s", "n"]:

            print("Respuesta no válida.")

            imagen = input("Ingrese solamente s o n: ").lower()


        # ----------------------------------------------------
        # SI NO MUESTRA IMAGEN
        # ----------------------------------------------------

        if imagen == "n":

            diagnostico = "El equipo enciende pero no muestra imagen."

            recomendacion = "Revisar monitor, cable de video, memoria RAM o tarjeta gráfica."

            nivel = "MEDIA"


        # ----------------------------------------------------
        # SI MUESTRA IMAGEN
        # ----------------------------------------------------

        else:

            # Preguntamos si el sistema operativo inicia.

            sistema = input("¿Inicia el sistema operativo? (s/n): ").lower()

            while sistema not in ["s", "n"]:

                print("Respuesta no válida.")

                sistema = input("Ingrese solamente s o n: ").lower()


            if sistema == "n":

                diagnostico = "El equipo muestra imagen pero no inicia el sistema operativo."

                recomendacion = "Revisar disco, sistema operativo, memoria RAM o configuración de arranque."

                nivel = "MEDIA"


            else:

                # ------------------------------------------------
                # PREGUNTA ADICIONAL
                # ------------------------------------------------

                rendimiento = input(
                    "¿El equipo funciona con lentitud? (s/n): "
                ).lower()

                while rendimiento not in ["s", "n"]:

                    print("Respuesta no válida.")

                    rendimiento = input(
                        "Ingrese solamente s o n: "
                    ).lower()


                if rendimiento == "s":

                    diagnostico = "El equipo funciona pero presenta bajo rendimiento."

                    recomendacion = "Revisar memoria RAM, almacenamiento, programas en ejecución y malware."

                    nivel = "BAJA"

                else:

                    diagnostico = "Funcionamiento básico correcto."

                    recomendacion = "No se detectaron problemas básicos."

                    nivel = "NORMAL"


# ------------------------------------------------------------
# 11. MOSTRAR REPORTE
# ------------------------------------------------------------

import tkinter as tk

# Diccionario para mantener la cuenta de reportes por usuario (Nombre + Dirección)
conteo_reportes = {}
contador_folio = 1


def mostrar_reporte_gui(texto_reporte, folio):
    # Crear ventana emergente para mostrar el reporte
    ventana = tk.Toplevel()
    ventana.title(f"Reporte de Servicio - {folio}")
    ventana.geometry("540x520")
    ventana.config(bg="#1e1e2e")

    # Asegurar que aparezca al frente en VS Code
    ventana.lift()
    ventana.attributes("-topmost", True)
    ventana.after_idle(ventana.attributes, "-topmost", False)

    lbl_titulo = tk.Label(
        ventana,
        text="REPORTE DE SERVICIO TÉCNICO",
        bg="#1e1e2e",
        fg="#ffffff",
        font=("Arial", 12, "bold"),
    )
    lbl_titulo.pack(pady=10)

    # Área de texto con el formato del reporte
    text_salida = tk.Text(
        ventana,
        height=22,
        width=62,
        font=("Consolas", 9),
        bg="#000000",
        fg="#00ff66",
    )
    text_salida.insert(tk.END, texto_reporte)
    text_salida.config(state="disabled")
    text_salida.pack(padx=10, pady=5)

    btn_cerrar = tk.Button(
        ventana,
        text="Aceptar y Continuar",
        command=ventana.destroy,
        bg="#007acc",
        fg="white",
        font=("Arial", 10, "bold"),
    )
    btn_cerrar.pack(pady=10)

    # Esperar a que se cierre la ventana para continuar en terminal
    ventana.wait_window()



root = tk.Tk()
root.withdraw()

while True:
    print("\n==========================================")
    print("      REGISTRO DE REPORTE DE SERVICIO      ")
    print("==========================================")

    # 1. PREGUNTAS EN LA TERMINAL DE VS CODE
    fecha = input("Fecha (dd/mm/aaaa)      : ").strip()
    hora = input("Hora (hh:mm)            : ").strip()

    print("\n--- DATOS DEL USUARIO ---")
    nombre = input("Nombre del usuario      : ").strip()
    direccion = input("Dirección               : ").strip()

    print("\n--- DATOS DEL EQUIPO ---")
    tipo_equipo = input("Tipo de equipo          : ").strip()

    print("\n--- DIAGNÓSTICO TÉCNICO ---")
    diagnostico = input("Resultado del diagnóstico: ").strip()
    nivel = input("Nivel (Bajo/Medio/Alto) : ").strip()
    recomendacion = input("Recomendación           : ").strip()

   
    clave_usuario = (nombre.lower(), direccion.lower())
    conteo_reportes[clave_usuario] = conteo_reportes.get(clave_usuario, 0) + 1
    total = conteo_reportes[clave_usuario]

    if total == 1:
        historial = "1er Reporte (Primer ingreso)"
    else:
        historial = f"Reporte N° {total} (Reincidente)"

    folio = f"REP-{contador_folio:03d}"
    contador_folio += 1

    
    texto_reporte = (
        f"==========================================\n"
        f"           REPORTE DE SERVICIO            \n"
        f"==========================================\n"
        f"Número de reporte : {folio}\n"
        f"Historial usuario : {historial}\n"
        f"Fecha             : {fecha}\n"
        f"Hora              : {hora}\n"
        f"------------------------------------------\n"
        f"USUARIO\n"
        f"Nombre            : {nombre}\n"
        f"Dirección         : {direccion}\n"
        f"------------------------------------------\n"
        f"EQUIPO\n"
        f"Tipo de equipo    : {tipo_equipo}\n"
        f"------------------------------------------\n"
        f"DIAGNÓSTICO\n"
        f"Resultado         : {diagnostico}\n"
        f"Nivel             : {nivel}\n"
        f"Recomendación     : {recomendacion}\n"
        f"==========================================\n"
        f"Fin del reporte.\n"
    )

    
    print("\nDesplegando reporte en ventana visual...")
    mostrar_reporte_gui(texto_reporte, folio)

    
    respuesta = (
        input("\n¿Deseas registrar otro reporte? (s/n): ").strip().lower()
    )
    if respuesta != "s":
        print("\nSaliendo del sistema de reportes.")
        break

root.destroy()