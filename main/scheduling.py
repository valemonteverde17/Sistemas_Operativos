from proceso import Proceso

class Scheduling:
    def __init__(self, procesos, quantum):
        self.procesos = procesos  # Lista de procesos
        self.quantum = quantum  # Valor del quantum

    def round_robin(self):
        tiempo_actual = 0  # Tiempo actual de la simulación
        cola_listos = self.procesos[:]  # Cola de procesos listos (copia de la lista de procesos)
        eventos = []  # Para almacenar los eventos de ejecución

        while cola_listos:
            proceso_actual = cola_listos.pop(0)  # Obtener el primer proceso en la cola
            t_inicio = tiempo_actual  # Tiempo de inicio de la ejecución

            if proceso_actual.tiempo_ejecucion > self.quantum:
                tiempo_actual += self.quantum  # Incrementar el tiempo actual por el quantum
                proceso_actual.tiempo_ejecucion -= self.quantum  # Decrementar el tiempo de ejecución del proceso
                cola_listos.append(proceso_actual)  # Reinsertar el proceso en la cola
            else:
                tiempo_actual += proceso_actual.tiempo_ejecucion  # Incrementar el tiempo actual por el tiempo de ejecución restante
                proceso_actual.tiempo_ejecucion = 0  # Establecer el tiempo de ejecución a 0

            t_fin = tiempo_actual  # Tiempo de finalización de la ejecución
            eventos.append((proceso_actual, t_inicio, t_fin))  # Añadir evento a la lista
            print(f"Proceso {proceso_actual.id_proceso} ejecutado de {t_inicio} a {t_fin}")

        return eventos  # Devolver la lista de eventos
