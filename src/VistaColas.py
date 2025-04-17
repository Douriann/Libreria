import tkinter as tk
from tkinter import messagebox
from Colas import Cola 
from EstudianteC import Estudiante

# Configuración de la ventanaa
ventana = tk.Tk()
ventana.title("Visualización de Cola")
ventana.geometry("800x400")

# Crear una instancia de Cola
cola = Cola()

# Función para dibujar la cola
def dibujar_cola():
    canvas.delete("all")  # Limpiar el canvas antes de redibujar
    
    if cola.Vacia():
        canvas.create_text(375, 150, text="[La cola está vacía]", font=("Arial", 14))
        return
    
    x = 100  # Posición inicial en X
    y = 150  # Posición fija en Y
    separacion = 100  # Espacio entre nodos
    
    p = cola.Frente
    while p is not None:
        # Dibujar nodo (círculo + texto)
        canvas.create_oval(x, y-30, x+60, y+30, fill="lightblue")
        canvas.create_text(x+30, y, text=str(p.info.cedula), font=("Arial", 12))
        
        # Dibujar flecha si hay un nodo siguiente
        if p.prox is not None:
            canvas.create_line(x+60, y, x+separacion, y, arrow=tk.LAST)
        
        # Resaltar Frente (rojo) y Final (verde)
        if p == cola.Frente:
            canvas.create_text(x+30, y-50, text="Frente", fill="red", font=("Arial", 10, "bold"))
        if p == cola.Final:
            canvas.create_text(x+30, y+50, text="Final", fill="green", font=("Arial", 10, "bold"))
        
        x += separacion
        p = p.prox

# Función para insertar un elemento en la cola
def insertar():
    cedula = entry_cedula.get()
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    carrera = entry_carrera.get()
    razon = entry_razon.get()
    estudiante = Estudiante(cedula, nombre, edad, carrera, razon)
    if (cedula and nombre and edad and carrera and razon):
        if cola.Insertar(estudiante):
            dibujar_cola()
            estudiante.mostrar_informacion()
            estudiante.describir_razon()
            messagebox.showinfo("Info", "Estudiante agregado a la cola.")
            cola.MostrarContenido()
        else:
            messagebox.showerror("Error", "¡La cola está llena (memoria)!")
    else:
        messagebox.showwarning("Advertencia", "Ingresa un valor.")
    limpiar_entradas()
    # Limpiar entradas de texto después de insertar

# Limpiar entradas de texto después de insertar
def limpiar_entradas():
    entry_cedula.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_carrera.delete(0, tk.END)
    entry_razon.delete(0, tk.END)

# Remover elemento de la cola
def remover():
    if cola.Vacia():
        messagebox.showinfo("Info", "La cola está vacía.")
    else:
        cola.Remover()
        dibujar_cola()

# Canvas para dibujar la cola
canvas = tk.Canvas(ventana, width=750, height=300, bg="white")
canvas.pack(pady=20)

# Creando un frame (contenedor) para los botones y entradas
# y organizando su disposición
frame_botones = tk.Frame(ventana)
frame_botones.pack()

# Creando los botones y entradas de texto

label_txt_cedula = tk.Label(frame_botones, text="Cédula:")
label_txt_cedula.pack(side=tk.LEFT, padx=5)
entry_cedula = tk.Entry(frame_botones, width=10)
entry_cedula.pack(side=tk.LEFT, padx=5)

label_txt_nombre = tk.Label(frame_botones, text="Nombre:")
label_txt_nombre.pack(side=tk.LEFT, padx=5)
entry_nombre = tk.Entry(frame_botones, width=10)
entry_nombre.pack(side=tk.LEFT, padx=5)

label_txt_edad = tk.Label(frame_botones, text="Edad:")
label_txt_edad.pack(side=tk.LEFT, padx=5)
entry_edad = tk.Entry(frame_botones, width=10)
entry_edad.pack(side=tk.LEFT, padx=5)

label_txt_carrera = tk.Label(frame_botones, text="Carrera:")
label_txt_carrera.pack(side=tk.LEFT, padx=5)
entry_carrera = tk.Entry(frame_botones, width=10)
entry_carrera.pack(side=tk.LEFT, padx=5)

label_txt_razon = tk.Label(frame_botones, text="Razón:")
label_txt_razon.pack(side=tk.LEFT, padx=5)
entry_razon = tk.Entry(frame_botones, width=10)
entry_razon.pack(side=tk.LEFT, padx=5)

btn_insertar = tk.Button(frame_botones, text="Insertar", command=insertar)
btn_insertar.pack(side=tk.LEFT, padx=5)

btn_remover = tk.Button(frame_botones, text="Remover", command=remover)
btn_remover.pack(side=tk.LEFT, padx=5)

# Mostrar cola inicial
dibujar_cola()
ventana.mainloop()