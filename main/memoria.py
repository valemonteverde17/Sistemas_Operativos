class BloqueMemoria:
    def __init__(self, id_bloque, tamaño):
        self.id_bloque = id_bloque
        self.tamaño = tamaño
        self.proceso_asignado = None

class Memoria:
    def __init__(self, tamaño_total):
        self.tamaño_total = tamaño_total
        self.bloques = [BloqueMemoria(1, tamaño_total)]
        self.procesos_asignados = []

    def agregar_proceso(self, proceso):
        if self.asignar_memoria(proceso):
            print(f'Proceso {proceso.id_proceso} agregado y asignado a la memoria.')
        else:
            print(f'Proceso {proceso.id_proceso} no se pudo agregar por falta de memoria.')

    def asignar_memoria(self, proceso):
        for bloque in self.bloques:
            if not bloque.proceso_asignado and bloque.tamaño >= proceso.tiempo_ejecucion:
                bloque.proceso_asignado = proceso
                self.procesos_asignados.append(proceso)
                print(f'Proceso {proceso.id_proceso} asignado al bloque {bloque.id_bloque}.')
                return True
        print(f'No se pudo asignar memoria al proceso {proceso.id_proceso}.')
        return False

    def liberar_memoria(self, proceso):
        for bloque in self.bloques:
            if bloque.proceso_asignado == proceso:
                bloque.proceso_asignado = None
                print(f'Memoria liberada para el proceso {proceso.id_proceso}.')
                return True
        print(f'No se encontró el proceso {proceso.id_proceso} en memoria.')
        return False

    def obtener_procesos(self):
        return self.procesos_asignados

    def obtener_memoria_libre(self):
        memoria_libre = sum(bloque.tamaño for bloque in self.bloques if bloque.proceso_asignado is None)
        return memoria_libre

    def obtener_memoria_ocupada(self):
        memoria_ocupada = self.tamaño_total - self.obtener_memoria_libre()
        return memoria_ocupada

