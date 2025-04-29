import tkinter as tk
import subprocess
from vista_pilas import VersionControlApp

# Funciones para los botones
def abrir_listas():
    subprocess.run(["python", "src/vista_lista.py"])

def abrir_pilas():
    ventana_pilas = tk.Tk()
    app = VersionControlApp(ventana_pilas)
    ventana_pilas.mainloop()

def abrir_colas():
    subprocess.run(["python", "src/vista_colas.py"])

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ventana con Botones")
ventana.geometry("300x200")

# Crear botones
btn_listas = tk.Button(ventana, text="Listas", command=abrir_listas)
btn_pilas = tk.Button(ventana, text="Pilas", command=abrir_pilas)
btn_colas = tk.Button(ventana, text="Colas", command=abrir_colas)

# Ubicar botones en la ventana
btn_listas.pack(pady=10)  # Espacio entre botones
btn_pilas.pack(pady=10)
btn_colas.pack(pady=10)

# Ejecutar ventana principal
ventana.mainloop()