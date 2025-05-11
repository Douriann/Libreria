import tkinter as tk
from tkinter import ttk, messagebox
from Estudiante import Estudiante
from Lista import Lista 

class VistaIdentificacion_estudiantes:
    def __init__(self, root, lista):
        self.nodo_seleccionado = None
        
        self.root = root
        self.root.title("Gestión de Estudiantes")
        self.root.minsize(1000, 800)

        self.lista = lista
        
        self.lista_excesivo = Lista()
        self.lista_medio = Lista()
        self.lista_bajo = Lista()
        
        self.titulo = tk.Label(self.root, text="Gestión de Estudiantes", font=("Arial", 20))
        self.titulo.pack(side="top", pady=10)

        # self.frame_busquedas = tk.Frame(root)
        # self.frame_busquedas.pack(padx=10, pady=5)

        # # Busqueda de los ingresados
        # tk.Label(self.frame_busquedas, text="Buscar Ingresados:").grid(row=0, column=0)
        # self.entry_buscar_ingresados = tk.Entry(self.frame_busquedas)
        # self.entry_buscar_ingresados.grid(row=0, column=1, padx=(5,50))
        # self.entry_buscar_ingresados.bind("<KeyRelease>", self.filtrar_ingresados)

        # # Busqueda no ingresados
        # tk.Label(self.frame_busquedas, text="Buscar No Ingresados:").grid(row=0, column=4, padx=(80, 0))
        # self.entry_buscar_no_ingresados = tk.Entry(self.frame_busquedas)
        # self.entry_buscar_no_ingresados.grid(row=0, column=5, padx=(20,5))
        # self.entry_buscar_no_ingresados.bind("<KeyRelease>", self.filtrar_no_ingresados)

        self.frame_tablas = tk.Frame(root)
        self.frame_tablas.pack(fill="x", expand=True, padx=10)
        
        self.frame_tablas.grid_columnconfigure(0, weight=1)
        # self.frame_tablas.grid_columnconfigure(1, weight=1)

        self.tree_excesivos = self.crear_tabla("Estudiantes con cargas academicas excesivas", 0)
        self.tree_medios = self.crear_tabla("Estudiantes con cargas academicas normales", 1)
        self.tree_bajos = self.crear_tabla("Estudiantes con cargas academicas bajas", 2)

        # self.contador_ingresados = tk.Label(self.frame_tablas, text="Total Ingresados: 0")
        # self.contador_ingresados.grid(row=0, column=1, pady=(0,10))

        # self.contador_no_ingresados = tk.Label(self.frame_tablas, text="Total No Ingresados: 0")
        # self.contador_no_ingresados.grid(row=1, column=1, pady=(0,10))

        # self.tree_ingresados.bind("<<TreeviewSelect>>", lambda e: self.autocompletar_desde_tabla(self.tree_ingresados))
        # self.tree_no_ingresados.bind("<<TreeviewSelect>>", lambda e: self.autocompletar_desde_tabla(self.tree_no_ingresados))

        # self.frame_form = tk.Frame(root)
        # self.frame_form.pack(padx=10, pady=5)

        # self.entries = {}
        # for i, campo in enumerate(["Cédula", "Nombre", "Carrera", "Materias", "UC Aprobadas"]):
        #     tk.Label(self.frame_form, text=campo).grid(row=i, column=0, sticky='w')
        #     entry = tk.Entry(self.frame_form)
        #     entry.grid(row=i, column=1, pady=2, sticky='ew')
        #     self.entries[campo.lower()] = entry

        # self.lista_destino = tk.StringVar(value="Ingresados")
        # tk.Radiobutton(self.frame_form, text="Ingresados", variable=self.lista_destino, value="Ingresados").grid(row=0, column=2)
        # tk.Radiobutton(self.frame_form, text="No Ingresados", variable=self.lista_destino, value="No Ingresados").grid(row=1, column=2)

        # self.frame_btns = tk.Frame(root)
        # self.frame_btns.pack(pady=5)

        # tk.Button(self.frame_btns, text="Agregar Estudiante", command=self.agregar_estudiante).grid(row=0, column=0, padx=5)
        # tk.Button(self.frame_btns, text="Eliminar de Ingresados", command=lambda: self.eliminar_estudiante(self.lista_ingresados)).grid(row=0, column=1, padx=5)
        # tk.Button(self.frame_btns, text="Eliminar de No Ingresados", command=lambda: self.eliminar_estudiante(self.lista_no_ingresados)).grid(row=0, column=2, padx=5)
        # tk.Button(self.frame_btns, text="Limpiar Campos", command=self.limpiar_campos).grid(row=0, column=3, padx=5)

        # tk.Button(self.frame_btns, text="Mover Todos a Ingresados", command=self.mover_todos_no_ingresados).grid(row=1, column=1, pady=5)
        # tk.Button(self.frame_btns, text="Mover Todos a No Ingresados", command=self.mover_todos_ingresados).grid(row=1, column=3, pady=5)

        # # self.label_img_grafo = tk.Label(root)
        # # self.label_img_grafo.pack(pady=10)
        # # Canvas para dibujar
        # self.canvas = tk.Canvas(self.root, bg="white")
        # self.canvas.pack(fill=tk.BOTH, padx=20, pady=20, expand=True)

        self.actualizar_tablas()

    def crear_tabla(self, titulo, col):
        frame = tk.Frame(self.frame_tablas)
        frame.grid(row=col, column=0, padx=10, sticky="nsew")
        tk.Label(frame, text=titulo).pack()
        tree = ttk.Treeview(frame, columns=("Cedula", "Nombre", "Carrera", "cantidad de materias", "UC acumuladas", "UC actuales"), show="headings", height=8)
        for col in tree["columns"]:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        tree.pack(fill="x", padx=30, pady=(10,60))
        return tree
    
    
    def filtrar_ingresados(self, event=None):
        # texto = self.entry_buscar_ingresados.get().lower()
        self.filtrar_tabla()

    def filtrar_tabla(self):
        for item in self.tree_excesivos.get_children():
            self.tree_excesivos.delete(item)
        for item in self.tree_medios.get_children():
            self.tree_medios.delete(item)
        for item in self.tree_bajos.get_children():
            self.tree_bajos.delete(item)
            
        p = self.lista.Primero
        
        while p:
            if p.info.creditos_totales > 16 and len(p.info.materias) >= 7:
                self.tree_excesivos.insert("", tk.END, values=p.info.getInfo())
            elif p.info.creditos_totales < 8 and len(p.info.materias) <= 3:
                self.tree_bajos.insert("", tk.END, values=p.info.getInfo())
            else: 
                self.tree_medios.insert("", tk.END, values=p.info.getInfo())
            p = p.prox
            

    def actualizar_tablas(self):
        self.filtrar_ingresados()

