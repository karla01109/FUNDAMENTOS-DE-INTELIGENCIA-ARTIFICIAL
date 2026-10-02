from datetime import datetime
import random
import time


class AgenteClimatizacion:

    def __init__(self, archivo_log="registro_agente.txt"):
        self.temperatura = 0.0
        self.humedad = 0.0
        self.accion = ""
        self.archivo_log = archivo_log

    def percibir_simulado(self):
        self.temperatura = round(random.uniform(15.0, 35.0), 1)
        self.humedad = round(random.uniform(40.0, 90.0), 1)

    def tomar_decision(self):
        if self.temperatura > 30 and self.humedad > 70:
            self.accion = "Encender aire acondicionado (Modo Deshumidificador)"
        elif self.temperatura > 30:
            self.accion = "Encender ventilador"
        elif self.temperatura < 18:
            self.accion = "Encender calefacción"
        else:
            self.accion = "Mantener sistema apagado"

    def guardar_registro(self):
        """Escribe la lectura directamente en el archivo .txt"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linea_log = (
            f"[{timestamp}] Temp: {self.temperatura}°C | "
            f"Humedad: {self.humedad}% | Acción: {self.accion}\n"
        )
     
        with open(self.archivo_log, "a", encoding="utf-8") as f:
            f.write(linea_log)

    def ejecutar_bucle(self, intervalo_segundos=3):
        print(f"--- Guardando registros en '{self.archivo_log}' ---")
        print("Presiona Ctrl + C para finalizar.\n")
        try:
            while True:
                self.percibir_simulado()
                self.tomar_decision()
                self.guardar_registro()  
                print(
                    f"Percepción -> {self.temperatura}°C, {self.humedad}% |"
                    f" Acción: {self.accion}"
                )
                time.sleep(intervalo_segundos)
        except KeyboardInterrupt:
            print(
                f"\nSimulación finalizada. Revisa el archivo '{self.archivo_log}'."
            )


if __name__ == "__main__":
    agente = AgenteClimatizacion()
    agente.ejecutar_bucle(intervalo_segundos=2)