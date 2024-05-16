from proceso import Proceso
from scheduling import Scheduling
from memoria import Memoria
from interfaz import Interfaz

# Crear procesos
proceso1 = Proceso(1, 0, 10)
proceso2 = Proceso(2, 2, 5)
proceso3 = Proceso(3, 4, 7)

procesos = [proceso1, proceso2, proceso3]
quantum = 3

# Iniciar la interfaz gráfica
if __name__ == "__main__":
    interfaz = Interfaz(procesos, quantum)
    interfaz.root.mainloop()
