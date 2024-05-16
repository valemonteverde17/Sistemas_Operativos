import tkinter as tk
from proceso import Proceso

class Interfaz:
    def __init__(self, procesos):
        self.root = tk.Tk()
        self.root.title('Simulador de Sistema Operativo')

        self.canvas = tk.Canvas(self.root, width=800, height=400, bg='white')
        self.canvas.pack()

        self.procesos = procesos

        self.dibujar_linea_tiempo()
        self.visualizar_ejecucion()

    def dibujar_linea_tiempo(self):
        # Dibujar línea de tiempo
        self.canvas.create_line(50, 50, 750, 50, width=2)
        for i in range(51, 751, 50):
            self.canvas.create_line(i, 50, i, 55, width=2)

    def dibujar_proceso(self, proceso, x_inicio, y_inicio):
        # Dibujar proceso en la línea de tiempo
        x_fin = x_inicio + proceso.tiempo_ejecucion * 10
        y_fin = y_inicio + 30
        self.canvas.create_rectangle(x_inicio, y_inicio, x_fin, y_fin, fill='skyblue')
        self.canvas.create_text((x_inicio + x_fin) / 2, (y_inicio + y_fin) / 2, text=f'P{proceso.id_proceso}')

    def visualizar_ejecucion(self):
        x_inicio = 50
        y_inicio = 100
        for proceso in self.procesos:
            self.dibujar_proceso(proceso, x_inicio, y_inicio)
            x_inicio += proceso.tiempo_ejecucion * 10 + 20

if __name__ == "__main__":
    proceso1 = Proceso(1, 0, 10)
    proceso2 = Proceso(2, 2, 5)
    proceso3 = Proceso(3, 4, 7)
    procesos = [proceso1, proceso2, proceso3]

    interfaz = Interfaz(procesos)
    interfaz.root.mainloop()

