import tkinter as tk

class TextRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget  # Widget de texto al que se redirigirá la salida

    def write(self, string):
        self.text_widget.insert(tk.END, string)  # Insertar cadena en el widget de texto
        self.text_widget.see(tk.END)  # Desplazar automáticamente al final

    def flush(self):
        pass  # Método flush, no se requiere implementación
