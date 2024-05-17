class Proceso:
    def __init__(self, id_proceso, tiempo_llegada, tiempo_ejecucion):
        self.id_proceso = id_proceso  # Identificador del proceso
        self.tiempo_llegada = tiempo_llegada  # Tiempo de llegada del proceso
        self.tiempo_ejecucion = tiempo_ejecucion  # Tiempo de ejecución del proceso
        self.tiempo_espera = 0  # Tiempo de espera del proceso (inicialmente 0)
        self.tiempo_respuesta = -1  # Tiempo de respuesta del proceso (inicialmente -1)

    def __str__(self):
        return f"Proceso {self.id_proceso}: Llegada = {self.tiempo_llegada}, Ejecución = {self.tiempo_ejecucion}"
        # Método para convertir el objeto a cadena de texto
