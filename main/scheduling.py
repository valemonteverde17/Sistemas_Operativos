from proceso import Proceso

class Scheduling:
    def __init__(self, procesos, quantum):
        self.procesos = procesos
        self.quantum = quantum

    def round_robin(self):
        tiempo_actual = 0
        cola_listos = self.procesos[:]
        while cola_listos:
            proceso_actual = cola_listos.pop(0)
            if proceso_actual.tiempo_espera == 0:  # Primer vez en la CPU
                proceso_actual.tiempo_respuesta = tiempo_actual - proceso_actual.tiempo_llegada
            if proceso_actual.tiempo_ejecucion > self.quantum:
                tiempo_actual += self.quantum
                proceso_actual.tiempo_ejecucion -= self.quantum
                proceso_actual.tiempo_espera += tiempo_actual - proceso_actual.tiempo_llegada
                cola_listos.append(proceso_actual)
            else:
                tiempo_actual += proceso_actual.tiempo_ejecucion
                proceso_actual.tiempo_ejecucion = 0
                print(f"Proceso {proceso_actual.id_proceso} terminado en tiempo {tiempo_actual}")
