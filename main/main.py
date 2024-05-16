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

# Simular ejecución de procesos
print("Ejecución de procesos:")
scheduler = Scheduling(procesos, quantum)
scheduler.round_robin()


# Simular gestión de memoria
print("\nGestión de memoria:")
memoria = Memoria(20)
for proceso in procesos:
    memoria.asignar_memoria(proceso)

# Liberar memoria de un proceso
memoria.liberar_memoria(proceso2)

# Visualizar procesos
print("\nProcesos:")
for proceso in procesos:
    print(proceso)

if __name__ == "__main__":
    proceso1 = Proceso(1, 0, 10)
    proceso2 = Proceso(2, 2, 5)
    proceso3 = Proceso(3, 4, 7)
    procesos = [proceso1, proceso2, proceso3]

    interfaz = Interfaz(procesos)
    interfaz.root.mainloop()
