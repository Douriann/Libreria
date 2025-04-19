import tkinter as tk
from tkinter import messagebox
from Colas import Cola
from EstudianteC import Estudiante

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Visualización de Cola")
ventana.geometry("800x500")

# Crear una instancia de Cola
cola = Cola()

# Función para dibujar la cola
def dibujar_cola():
    canvas.delete("all")  # Limpiar el canvas antes de redibujar

    if cola.Vacia():
        canvas.create_text(375, 150, text="[La cola está vacía]", font=("Arial", 14))
        anuncio.config(text="No hay estudiantes en la cola", fg="black")
        canvas.config(scrollregion=canvas.bbox("all")) # Ajustar scrollregion incluso cuando está vacía
        return

    x = 100  # Posición inicial en X
    y = 150  # Posición fija en Y
    separacion = 100  # Espacio entre nodos

    p = cola.Frente
    while p is not None:
        # Dibujar nodo (círculo + texto)
        canvas.create_oval(x, y-30, x+80, y+30, fill="lightblue")
        canvas.create_text(x+40, y, text=str(p.info.cedula), font=("Arial", 12))

        # Dibujar flecha si hay un nodo siguiente
        if p.prox is not None:
            canvas.create_line(x+80, y, x+separacion, y, arrow=tk.LAST)

        # Resaltar Frente (rojo) y Final (verde)
        if p == cola.Frente:
            canvas.create_text(x+40, y-50, text="Frente", fill="red", font=("Arial", 10, "bold"))
            mostrar_estudiante_atendido(p.info)
        if p == cola.Final:
            canvas.create_text(x+40, y+50, text="Final", fill="green", font=("Arial", 10, "bold"))

        x += separacion
        p = p.prox

    # Actualizar la región de desplazamiento del canvas para que abarque todo el contenido
    canvas.config(scrollregion=canvas.bbox("all"))

# Función para mostrar información del estudiante siendo atendido
def mostrar_estudiante_atendido(estudiante):
    razon = estudiante.describir_razon()
    mensaje = f"El estudiante esta siendo atendido:\n" \
                f"Cédula: {estudiante.cedula}\n" \
                f"Nombre: {estudiante.nombre}\n" \
                f"Razón: {razon}"
    anuncio.config(text=mensaje, fg="black")

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
        estudiante_removido = cola.Remover()
        if estudiante_removido:
            messagebox.showinfo("Info", f"Se atendió al estudiante: {estudiante_removido.cedula}")
        dibujar_cola()

# Crear barra de desplazamiento

barra_horizontal = tk.Scrollbar(ventana, orient=tk.HORIZONTAL)
barra_horizontal.pack(side=tk.BOTTOM, fill=tk.X)

# Canvas para dibujar la cola y asociar la barra de desplazamiento
canvas = tk.Canvas(ventana, width=750, height=250, bg="white",
                   xscrollcommand=barra_horizontal.set)
canvas.pack(pady=20)

# Configurar el comportamiento de la barra de desplazamiento
barra_horizontal.config(command=canvas.xview)

# Etiqueta para mostrar el anuncio del estudiante siendo atendido
anuncio = tk.Label(ventana, text="No hay estudiantes en la cola",
font=("Arial", 12), fg="black", justify=tk.LEFT)
anuncio.place(x=500, y=300) #OJO, cambiar la posición de la etiqueta para que no se superponga con el canvas

# Creando un frame (contenedor) para los botones y entradas
# y organizando su disposición
frame_botones = tk.Frame(ventana)
frame_botones.pack(side=tk.BOTTOM, pady=10)
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(anchor="w", padx=10)

# Creando los botones y entradas de texto
label_txt_entrada = tk.Label(frame_entrada, text="Inserte los datos necesarios\npara visualizar:", justify=tk.LEFT)
label_txt_entrada.pack(anchor="w")
frame_cedula = tk.Frame(frame_entrada)
frame_cedula.pack(anchor="w")
label_txt_cedula = tk.Label(frame_cedula, text="Cédula:")
label_txt_cedula.pack(side=tk.LEFT)
entry_cedula = tk.Entry(frame_cedula, width=10)
entry_cedula.pack(side=tk.LEFT, padx=5)

frame_nombre = tk.Frame(frame_entrada)
frame_nombre.pack(anchor="w")
label_txt_nombre = tk.Label(frame_nombre, text="Nombre:")
label_txt_nombre.pack(side=tk.LEFT)
entry_nombre = tk.Entry(frame_nombre, width=10)
entry_nombre.pack(side=tk.LEFT, padx=5)

frame_edad = tk.Frame(frame_entrada)
frame_edad.pack(anchor="w")
label_txt_edad = tk.Label(frame_edad, text="Edad:")
label_txt_edad.pack(side=tk.LEFT)
entry_edad = tk.Entry(frame_edad , width=10)
entry_edad.pack(side=tk.LEFT, padx=5)

frame_carrera = tk.Frame(frame_entrada)
frame_carrera.pack(anchor="w")
label_txt_carrera = tk.Label(frame_carrera, text="Carrera:")
label_txt_carrera.pack(side=tk.LEFT)
entry_carrera = tk.Entry(frame_carrera , width=10)
entry_carrera.pack(side=tk.LEFT , padx=5)

frame_razon = tk.Frame(frame_entrada)
frame_razon.pack(anchor="w")
label_txt_razon = tk.Label(frame_razon, text="Razón:")
label_txt_razon.pack(side=tk.LEFT)
entry_razon = tk.Entry(frame_razon, width=10)
entry_razon.pack(side=tk.LEFT , padx=5)

btn_insertar = tk.Button(frame_botones, text="Insertar", command=insertar)
btn_insertar.pack(side=tk.LEFT, padx=5)

btn_remover = tk.Button(frame_botones, text="Remover", command=remover)
btn_remover.pack(side=tk.LEFT, padx=5)

# Mostrar cola inicial
dibujar_cola()
ventana.mainloop()