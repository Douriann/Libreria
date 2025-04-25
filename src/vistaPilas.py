import tkinter as tk
from tkinter import ttk, messagebox
from Pila import Pila

class VersionControlApp:
    def __init__(self, root):
        self.root = root
        self.pila = Pila()
        self.contador_versiones = 0
        
        self.configurar_interfaz()
        self.crear_widgets()

    def configurar_interfaz(self):
        self.root.title("Control de Versiones CUMLAUDE")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#f0f0f0')

    def crear_widgets(self):
        # Frame principal
        self.frame_principal = ttk.Frame(self.root)
        self.frame_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Frame de entrada
        self.frame_entrada = ttk.Frame(self.frame_principal)
        self.frame_entrada.pack(fill=tk.X, pady=(0, 10))

        self.label_txt_titulo = ttk.Label(
            self.frame_entrada, 
            text="Agregar Nueva Versión",
            font=('Arial', 12, 'bold')
        )
        self.label_txt_titulo.grid(row=0, column=0, columnspan=2, pady=5)

        self.label_txt_autor = ttk.Label(self.frame_entrada, text="Autor:")
        self.label_txt_autor.grid(row=1, column=0, sticky=tk.W, padx=5)
        
        self.entry_autor = ttk.Entry(self.frame_entrada, width=40)
        self.entry_autor.grid(row=1, column=1, padx=5, pady=2, sticky=tk.W)
        
        self.label_txt_cambios = ttk.Label(self.frame_entrada, text="Cambios realizados:")
        self.label_txt_cambios.grid(row=2, column=0, sticky=tk.W, padx=5)
        
        self.entry_cambios = ttk.Entry(self.frame_entrada, width=40)
        self.entry_cambios.grid(row=2, column=1, padx=5, pady=2, sticky=tk.W)
        
        self.btn_agregar = ttk.Button(
            self.frame_entrada, 
            text="Agregar Versión", 
            command=self.agregar_version
        )
        self.btn_agregar.grid(row=3, column=0, columnspan=2, pady=5)

        # Frame de acciones
        self.frame_acciones = ttk.Frame(self.frame_principal)
        self.frame_acciones.pack(fill=tk.X, pady=(0, 10))
        
        self.btn_revertir = ttk.Button(
            self.frame_acciones, 
            text="Revertir Versión", 
            command=self.revertir_version
        )
        self.btn_revertir.pack(side=tk.LEFT, padx=5)
        
        self.btn_limpiar = ttk.Button(
            self.frame_acciones, 
            text="Limpiar Todo", 
            command=self.limpiar_todo
        )
        self.btn_limpiar.pack(side=tk.LEFT, padx=5)

        # Frame de visualización
        self.frame_visualizacion = ttk.Frame(self.frame_principal)
        self.frame_visualizacion.pack(fill=tk.BOTH, expand=True)
        
        self.label_txt_historial = ttk.Label(
            self.frame_visualizacion, 
            text="Historial de Versiones",
            font=('Arial', 12, 'bold')
        )
        self.label_txt_historial.pack()
        
        self.text_historial = tk.Text(
            self.frame_visualizacion, 
            width=80, 
            height=15, 
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.text_historial.pack(fill=tk.BOTH, expand=True)

        # Frame de gráfico
        self.frame_grafico = ttk.Frame(self.frame_principal)
        self.frame_grafico.pack(fill=tk.X, pady=(10, 0))
        
        self.canvas_pila = tk.Canvas(
            self.frame_grafico, 
            bg='white', 
            height=180,
            highlightthickness=1,
            highlightbackground="#cccccc"
        )
        self.canvas_pila.pack(fill=tk.X)

    def agregar_version(self):
        autor = self.entry_autor.get()
        cambios = self.entry_cambios.get()
        
        if not autor or not cambios:
            messagebox.showwarning("Error", "Debe completar ambos campos")
            return
        
        # Adaptación para usar tu Pila.py original
        self.contador_versiones += 1
        datos_version = {
            'id': self.contador_versiones,
            'autor': autor,
            'cambios': cambios
        }
        
        if not self.pila.Llena():
            self.pila.Insertar(datos_version)
            messagebox.showinfo("Éxito", f"Versión {self.contador_versiones} agregada")
            self.entry_autor.delete(0, tk.END)
            self.entry_cambios.delete(0, tk.END)
            self.actualizar_interfaz()
        else:
            messagebox.showerror("Error", "No se pudo agregar la versión")

    def revertir_version(self):
        version = self.pila.Remover()
        if version:
            self.contador_versiones -= 1
            messagebox.showinfo("Revertido", 
                f"Versión {version['id']} revertida")  # Cambia aquí
            self.actualizar_interfaz()
        else:
            messagebox.showwarning("Error", "No hay versiones para revertir")

    def limpiar_todo(self):
        if messagebox.askyesno("Confirmar", "¿Desea limpiar todo el historial?"):
            self.pila = Pila()
            self.contador_versiones = 0
            self.actualizar_interfaz()

    def actualizar_interfaz(self):
        self.actualizar_historial()
        self.dibujar_pila()

    def actualizar_historial(self):
        self.text_historial.config(state=tk.NORMAL)
        self.text_historial.delete(1.0, tk.END)
        
        contenido = self.pila.obtener_contenido()
        if not contenido:
            self.text_historial.insert(tk.END, "No hay versiones registradas.")
        else:
            for version in contenido:
                self.text_historial.insert(tk.END, 
                    f"Versión {version['id']}\n"
                    f"Autor: {version['autor']}\n"
                    f"Cambios: {version['cambios']}\n"
                    f"{'-'*50}\n\n")
        
        self.text_historial.config(state=tk.DISABLED)

    def dibujar_pila(self):
        self.canvas_pila.delete("all")
        contenido = self.pila.obtener_contenido()
        if not contenido:
            self.canvas_pila.create_text(150, 90, text="Pila vacía", font=('Arial', 12))
            return

        width = self.canvas_pila.winfo_width()
        x = width // 2
        y = 20
        rect_width = 200
        rect_height = 30

        for i, version in enumerate(contenido):
            color = "#d9e6f2" if i % 2 == 0 else "#c4d9f2"
            self.canvas_pila.create_rectangle(
                x - rect_width//2, y,
                x + rect_width//2, y + rect_height,
                fill=color, outline="#4a90d9"
            )
            self.canvas_pila.create_text(
                x, y + rect_height//2,
                text=f"Versión {version['id']}: {version['autor']}",
                font=('Arial', 8)
            )
            if i == 0:
                self.canvas_pila.create_text(
                    x + rect_width//2 - 10, y + 5,
                    text="TOP", font=('Arial', 7, 'bold'),
                    fill="red"
                )
            y += rect_height + 5