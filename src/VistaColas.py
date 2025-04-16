import tkinter as tk
from tkinter import messagebox
from Colas import Cola  # Importa tu clase Cola (ajusta el nombre del archivo)

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Visualización de Cola")
ventana.geometry("800x400")

# Crear una instancia de tu Cola
cola = Cola()

# Canvas para dibujar la cola
canvas = tk.Canvas(ventana, width=750, height=300, bg="white")
canvas.pack(pady=20)

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
        canvas.create_text(x+30, y, text=str(p.info), font=("Arial", 12))
        
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

# Botones para operaciones
frame_botones = tk.Frame(ventana)
frame_botones.pack()

# Insertar elemento
entry_valor = tk.Entry(frame_botones, width=10)
entry_valor.pack(side=tk.LEFT, padx=5)

def insertar():
    valor = entry_valor.get()
    if valor:
        if cola.Insertar(valor):
            dibujar_cola()
        else:
            messagebox.showerror("Error", "¡La cola está llena (memoria)!")
    else:
        messagebox.showwarning("Advertencia", "Ingresa un valor.")
    entry_valor.delete(0, tk.END)

tk.Button(frame_botones, text="Insertar", command=insertar).pack(side=tk.LEFT, padx=5)

# Remover elemento
def remover():
    if cola.Vacia():
        messagebox.showinfo("Info", "La cola está vacía.")
    else:
        cola.Remover()
        dibujar_cola()

tk.Button(frame_botones, text="Remover", command=remover).pack(side=tk.LEFT, padx=5)

# Mostrar cola inicial
dibujar_cola()
ventana.mainloop()