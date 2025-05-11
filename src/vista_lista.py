import tkinter as tk
from tkinter import ttk, messagebox
from Estudiante import Estudiante
from Lista import Lista 

# Diccionario de materias y sus créditos
MATERIAS_CREDITOS = {
    "Calculo I": 4,
    "Calculo II": 4,
    "Calculo III": 4,
    "Calculo IV": 4,
    "Programacion I": 3,
    "Programacion II": 3,
    "Programacion III": 3,
    "Estadistica I": 4,
    "Estadistica II": 4,
    "Estadistica Matematica": 4,
    "Teoria de la Administracion I": 4,
    "Tecnicas de la Administracion II": 4,
    "Laboratorio I": 2,
    "Laboratorio II": 2,
    "Programacion Numerica": 2,
    "Programacion No Numerica I": 3,
    "Programacion No Numerica II": 4,
}
grupos_excluyentes = [
    ["Calculo I", "Calculo II", "Calculo III", "Calculo IV"],
    ["Programacion I", "Programacion II", "Programacion III"],
    ["Estadistica I", "Estadistica II", "Estadistica Matematica"],
    ["Teoria de la Administracion I", "Tecnicas de la Administracion II"],
    ["Laboratorio I", "Laboratorio II"],
    ["Programacion No Numerica I", "Programacion No Numerica II"]
]
class VistaListaApp:
    def __init__(self, root):
        self.nodo_seleccionado = None
        
        self.root = root
        self.root.title("Gestión de Estudiantes")

        self.lista_ingresados = Lista()
        self.lista_no_ingresados = Lista()
        
        self.titulo = tk.Label(self.root, text="Gestión de Estudiantes", font=("Arial", 20))
        self.titulo.pack(side="top", pady=10)

        self.frame_busquedas = tk.Frame(root)
        self.frame_busquedas.pack(padx=10, pady=5)

        # Busqueda de los ingresados
        tk.Label(self.frame_busquedas, text="Buscar Ingresados:").grid(row=0, column=0)
        self.entry_buscar_ingresados = tk.Entry(self.frame_busquedas)
        self.entry_buscar_ingresados.grid(row=0, column=1, padx=(5,50))
        self.entry_buscar_ingresados.bind("<KeyRelease>", self.filtrar_ingresados)

        # Busqueda no ingresados
        tk.Label(self.frame_busquedas, text="Buscar No Ingresados:").grid(row=0, column=4, padx=(80, 0))
        self.entry_buscar_no_ingresados = tk.Entry(self.frame_busquedas)
        self.entry_buscar_no_ingresados.grid(row=0, column=5, padx=(20,5))
        self.entry_buscar_no_ingresados.bind("<KeyRelease>", self.filtrar_no_ingresados)

        self.frame_tablas = tk.Frame(root)
        self.frame_tablas.pack(fill="x", expand=True, padx=10)
        
        self.frame_tablas.grid_columnconfigure(0, weight=1)
        self.frame_tablas.grid_columnconfigure(1, weight=1)

        self.tree_ingresados = self.crear_tabla("Estudiantes Ingresados", 0)
        self.tree_no_ingresados = self.crear_tabla("Estudiantes No Ingresados", 1)

        self.contador_ingresados = tk.Label(self.frame_tablas, text="Total Ingresados: 0")
        self.contador_ingresados.grid(row=1, column=0, pady=(0,10))

        self.contador_no_ingresados = tk.Label(self.frame_tablas, text="Total No Ingresados: 0")
        self.contador_no_ingresados.grid(row=1, column=1, pady=(0,10))

        self.tree_ingresados.bind("<<TreeviewSelect>>", lambda e: self.autocompletar_desde_tabla(self.tree_ingresados))
        self.tree_no_ingresados.bind("<<TreeviewSelect>>", lambda e: self.autocompletar_desde_tabla(self.tree_no_ingresados))

        self.frame_form = tk.Frame(root)
        self.frame_form.pack(padx=10, pady=5)

        self.entries = {}
        for i, campo in enumerate(["Cédula", "Nombre", "Carrera", "Materias", "UC Aprobadas"]):
            tk.Label(self.frame_form, text=campo).grid(row=i, column=0, sticky='w')
            entry = tk.Entry(self.frame_form)
            entry.grid(row=i, column=1, pady=2, sticky='ew')
            self.entries[campo.lower()] = entry

        self.lista_destino = tk.StringVar(value="Ingresados")
        tk.Radiobutton(self.frame_form, text="Ingresados", variable=self.lista_destino, value="Ingresados").grid(row=0, column=2)
        tk.Radiobutton(self.frame_form, text="No Ingresados", variable=self.lista_destino, value="No Ingresados").grid(row=1, column=2)

        self.frame_btns = tk.Frame(root)
        self.frame_btns.pack(pady=5)

        tk.Button(self.frame_btns, text="Agregar Estudiante", command=self.agregar_estudiante).grid(row=0, column=0, padx=5)
        tk.Button(self.frame_btns, text="Eliminar de Ingresados", command=lambda: self.eliminar_estudiante(self.lista_ingresados)).grid(row=0, column=1, padx=5)
        tk.Button(self.frame_btns, text="Eliminar de No Ingresados", command=lambda: self.eliminar_estudiante(self.lista_no_ingresados)).grid(row=0, column=2, padx=5)
        tk.Button(self.frame_btns, text="Limpiar Campos", command=self.limpiar_campos).grid(row=0, column=3, padx=5)

        tk.Button(self.frame_btns, text="Mover Todos a Ingresados", command=self.mover_todos_no_ingresados).grid(row=1, column=1, pady=5)
        tk.Button(self.frame_btns, text="Mover Todos a No Ingresados", command=self.mover_todos_ingresados).grid(row=1, column=3, pady=5)

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill=tk.BOTH, padx=20, pady=20, expand=True)

        self.actualizar_tablas()

    def crear_tabla(self, titulo, col):
        frame = tk.Frame(self.frame_tablas)
        frame.grid(row=0, column=col, padx=10, sticky="nsew")
        tk.Label(frame, text=titulo).pack()
        tree = ttk.Treeview(frame, columns=("Cedula", "Nombre", "Carrera", "Materias", "UC"), show="headings", height=7)
        for col in tree["columns"]:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        tree.pack(fill="x", padx=30)
        return tree
    def agregar_estudiante(self):
     datos = [entry.get().strip() for entry in self.entries.values()]
     if not all(datos):
        messagebox.showwarning("Campos incompletos", "Todos los campos deben estar llenos.")
        return

     cedula, nombre, carrera, materias, uc_aprobadas = datos

     # Validaciones campos de entrada
     if not cedula.isdigit():
        messagebox.showerror("Error de Validación", "La cédula debe contener solo números.")
        return

     # Validar que la cédula no esté repetida en ninguna lista
     for lista in [self.lista_ingresados, self.lista_no_ingresados]:
        if lista.Buscar(cedula):
            messagebox.showerror("Duplicado", "La cédula ya está registrada.")
            return

     if not uc_aprobadas.isdigit():
        messagebox.showerror("Error de Validación", "Las UC Aprobadas deben ser un número.")
        return
     if not nombre.replace(" ", "").isalpha():
        messagebox.showerror("Error de Validación", "El nombre solo debe contener letras.")
        return

     materias = materias.split(",")
     materias = [materia.strip() for materia in materias]

     # Validación de materias duplicadas
     if len(materias) != len(set(materias)):
        messagebox.showerror("Error de Materia", "No se puede inscribir una misma materia más de una vez.")
        return

     creditos_totales = 0
     materias_validadas = []

     grupos_excluyentes = [
        ["Calculo I", "Calculo II", "Calculo III", "Calculo IV"],
        ["Programacion I", "Programacion II", "Programacion III"],
        ["Estadistica I", "Estadistica II", "Estadistica Matematica"],
        ["Teoria de la Administracion I", "Tecnicas de la Administracion II"],
        ["Laboratorio I", "Laboratorio II"],
        ["Programacion No Numerica I", "Programacion No Numerica II"]
     ]

     for materia in materias:
        if materia not in MATERIAS_CREDITOS:
            messagebox.showerror("Error de Materia", f"La materia {materia} no existe en el sistema.")
            return

        # Validar exclusividad por grupo
        for grupo in grupos_excluyentes:
            if materia in grupo:
                if any(m in grupo for m in materias_validadas):
                    messagebox.showerror(
                        "Error de Materia",
                        f"No se pueden inscribir juntas materias excluyentes del mismo grupo: {grupo}"
                    )
                    return

        # Verificar que los créditos no superen el límite
        creditos_totales += MATERIAS_CREDITOS[materia]
        if creditos_totales > 16:
            messagebox.showerror("Error de Créditos", "El total de créditos no puede superar 16.")
            return

        materias_validadas.append(materia)

     estudiante = Estudiante(cedula, nombre, carrera, materias, uc_aprobadas)
     estudiante.materias = materias_validadas

     destino = self.lista_ingresados if self.lista_destino.get() == "Ingresados" else self.lista_no_ingresados

     # Insertar al final de la lista usando InsDespues
     if destino.Vacia():
        destino.InsComienzo(estudiante)
     else:
        ultimo_nodo = destino.Primero
        while ultimo_nodo.prox is not None:
            ultimo_nodo = ultimo_nodo.prox
        destino.InsDespues(ultimo_nodo, estudiante)

     self.actualizar_tablas()
     self.limpiar_campos()




    
    def eliminar_estudiante(self, lista):
        cedula = self.entries["cédula"].get().strip()
        if not cedula:
            messagebox.showwarning("Cédula Vacía", "Ingrese la cédula a eliminar.")
            return

        p = lista.Primero
        ant = None
        while p:
            if p.info.identificacion == cedula:
                if ant:
                    lista.EliDespues(ant)
                else:
                    lista.EliComienzo()
                self.actualizar_tablas()
                self.limpiar_campos()
                return
            ant = p
            p = p.prox
        messagebox.showinfo("No encontrado", "Cédula no encontrada.")

    def limpiar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.lista_destino.set("Ingresados")

    def actualizar_tablas(self):
        for tree, lista in [(self.tree_ingresados, self.lista_ingresados), (self.tree_no_ingresados, self.lista_no_ingresados)]:
            for item in tree.get_children():
                tree.delete(item)

            for estudiante in lista.obtener_todos():
                tree.insert("", "end", values=(estudiante.cedula, estudiante.nombre, estudiante.carrera, ", ".join(estudiante.materias), estudiante.uc_aprobadas))

        self.contador_ingresados.config(text=f"Total Ingresados: {self.lista_ingresados.obtener_tamano()}")
        self.contador_no_ingresados.config(text=f"Total No Ingresados: {self.lista_no_ingresados.obtener_tamano()}")

    def filtrar_ingresados(self, event):
        self.filtrar(self.entry_buscar_ingresados, self.tree_ingresados)

    def filtrar_no_ingresados(self, event):
        self.filtrar(self.entry_buscar_no_ingresados, self.tree_no_ingresados)

    def filtrar(self, entry, tree):
        filtro = entry.get().lower()
        for item in tree.get_children():
            tree.delete(item)

        for estudiante in self.lista_ingresados.obtener_todos():
            if filtro in estudiante.nombre.lower():
                tree.insert("", "end", values=(estudiante.cedula, estudiante.nombre, estudiante.carrera, ", ".join(estudiante.materias), estudiante.uc_aprobadas))

    def mover_todos_no_ingresados(self):
        self.lista_ingresados.pasarListaAux(self.lista_no_ingresados, self.lista_ingresados)
        self.actualizar_tablas()

    def mover_todos_ingresados(self):
        self.lista_no_ingresados.pasarListaAux(self.lista_ingresados, self.lista_no_ingresados)
        self.actualizar_tablas()

    def autocompletar_desde_tabla(self, tree):
        selected = tree.selection()
        if selected:
            item = tree.item(selected[0])
            for key, value in zip(self.entries.keys(), item["values"]):
                self.entries[key].delete(0, tk.END)
                self.entries[key].insert(0, value)


    def limpiar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def filtrar_ingresados(self, event=None):
        texto = self.entry_buscar_ingresados.get().lower()
        self.filtrar_tabla(self.tree_ingresados, self.lista_ingresados, texto)

    def filtrar_no_ingresados(self, event=None):
        texto = self.entry_buscar_no_ingresados.get().lower()
        self.filtrar_tabla(self.tree_no_ingresados, self.lista_no_ingresados, texto)

    def filtrar_tabla(self, tree, lista, texto):
        for item in tree.get_children():
            tree.delete(item)
        p = lista.Primero
        while p:
            if texto in p.info.identificacion.lower():
                tree.insert("", tk.END, values=p.info.getInfo())
            p = p.prox

    def actualizar_tablas(self):
        self.filtrar_ingresados()
        self.filtrar_no_ingresados()
        self.actualizar_grafo()
        self.contador_ingresados.config(text=f"Total de Ingresados: {self.lista_ingresados.Contar()}")
        self.contador_no_ingresados.config(text=f"Total de No Ingresados: {self.lista_no_ingresados.Contar()}")
        
    def actualizar_grafo(self):
        self.canvas.delete("all")
        print("dibujar lista estudiante")
        if self.lista_ingresados.Vacia():
            self.canvas.create_text((self.canvas.winfo_reqwidth() / 2), (self.canvas.winfo_reqheight() / 2), text="[Lista vacía]", font=("Arial", 14))
            return

        x = 100  # Posición inicial X
        y = 150  # Posición fija Y
        separacion = 170  # Espacio entre nodos

        p = self.lista_ingresados.Primero
        while p is not None:
            # Dibujar nodo (círculo + texto)
            color = "red" if p == self.lista_ingresados.Primero else ("lightgreen" if p == self.nodo_seleccionado else "lightblue")
            # canvas.create_oval(x-30, y-30, x+30, y+30, fill=color, tags=f"nodo_{p.info.identificacion}")
            self.canvas.create_rectangle(x-50, y-30, x+50, y+30, fill=color, tags=f"nodo_{p.info.identificacion}")
            small_rect_width = 20
            self.canvas.create_rectangle(x+50, y-30, x+50+small_rect_width, y+30, fill=color, tags=f"nodo_{p.info.identificacion}")
            if p.prox is None:
                self.canvas.create_line(x+50, y+30, x+50+small_rect_width, y-30, tags=f"nodo_{p.info.identificacion}")
            self.canvas.create_text(x, y, text=str(p.info.identificacion), font=("Arial", 12))

            # Dibujar flecha si hay próximo nodo
            if p.prox is not None:
                self.canvas.create_line(x+70, y, x+separacion-30, y, arrow=tk.LAST)

            # Etiquetar cabeza
            if p == self.lista_ingresados.Primero:
                self.canvas.create_text(x, y-50, text="Primero", fill="red", font=("Arial", 10, "bold"))

            # Asignar evento de clic para selección
            self.canvas.tag_bind(f"nodo_{p.info}", "<Button-1>", lambda e, nodo=p: self.seleccionar_nodo(nodo))

            x += separacion
            p = p.prox
            
    # Selección de nodo
    def seleccionar_nodo(self,nodo):
        self.nodo_seleccionado = nodo
        self.actualizar_grafo()

if __name__ == "__main__":
    root = tk.Tk()
    app = VistaListaApp(root)
    root.mainloop()