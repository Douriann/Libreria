import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from graphviz import Digraph
import os
from Lista import Lista 

class VistaListaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Estudiantes")

        self.lista_ingresados = Lista()
        self.lista_no_ingresados = Lista()

        self.frame_busquedas = tk.Frame(root)
        self.frame_busquedas.pack(padx=10, pady=5)

        # Busqueda de los ingresados
        tk.Label(self.frame_busquedas, text="Buscar Ingresados:").grid(row=0, column=0)
        self.entry_buscar_ingresados = tk.Entry(self.frame_busquedas)
        self.entry_buscar_ingresados.grid(row=0, column=1, padx=5)
        self.entry_buscar_ingresados.bind("<KeyRelease>", self.filtrar_ingresados)

        # Busqueda no ingresados
        tk.Label(self.frame_busquedas, text="Buscar No Ingresados:").grid(row=0, column=2)
        self.entry_buscar_no_ingresados = tk.Entry(self.frame_busquedas)
        self.entry_buscar_no_ingresados.grid(row=0, column=3, padx=5)
        self.entry_buscar_no_ingresados.bind("<KeyRelease>", self.filtrar_no_ingresados)

        self.frame_tablas = tk.Frame(root)
        self.frame_tablas.pack(padx=10)

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

        self.label_img_grafo = tk.Label(root)
        self.label_img_grafo.pack(pady=10)

        self.actualizar_tablas()

    def crear_tabla(self, titulo, col):
        frame = tk.Frame(self.frame_tablas)
        frame.grid(row=0, column=col, padx=10)
        tk.Label(frame, text=titulo).pack()
        tree = ttk.Treeview(frame, columns=("Cedula", "Nombre", "Carrera", "Materias", "UC"), show="headings", height=7)
        for col in tree["columns"]:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        tree.pack()
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
        if not uc_aprobadas.isdigit():
            messagebox.showerror("Error de Validación", "Las UC Aprobadas deben ser un número.")
            return
        if not nombre.replace(" ", "").isalpha():
            messagebox.showerror("Error de Validación", "El nombre solo debe contener letras.")
            return

        destino = self.lista_ingresados if self.lista_destino.get() == "Ingresados" else self.lista_no_ingresados

        for lista in [self.lista_ingresados, self.lista_no_ingresados]:
            if lista.Buscar(cedula):
                messagebox.showerror("Duplicado", "La cédula ya está registrada.")
                return

        destino.InsComienzo("|".join(datos))
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
            if p.info.split("|")[0] == cedula:
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

    def mover_todos_no_ingresados(self):
        self.lista_ingresados.pasarListaAux(self.lista_no_ingresados, self.lista_ingresados)
        self.actualizar_tablas()

    def mover_todos_ingresados(self):
        self.lista_no_ingresados.pasarListaAux(self.lista_ingresados, self.lista_no_ingresados)
        self.actualizar_tablas()

    def autocompletar_desde_tabla(self, tree):
        item = tree.selection()
        if item:
            datos = tree.item(item[0])["values"]
            claves = list(self.entries.keys())
            for i in range(len(claves)):
                self.entries[claves[i]].delete(0, tk.END)
                self.entries[claves[i]].insert(0, datos[i])

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
            if texto in p.info.lower():
                tree.insert("", tk.END, values=p.info.split("|"))
            p = p.prox

    def actualizar_tablas(self):
        self.filtrar_ingresados()
        self.filtrar_no_ingresados()
        self.actualizar_grafo()
        self.contador_ingresados.config(text=f"Total de Ingresados: {self.lista_ingresados.Contar()}")
        self.contador_no_ingresados.config(text=f"Total de No Ingresados: {self.lista_no_ingresados.Contar()}")

    def actualizar_grafo(self):
        dot = Digraph(format='png')
        dot.attr(rankdir='LR', size='10')
        p = self.lista_ingresados.Primero
        idx = 0
        last = None
        while p:
            datos = p.info.split("|")
            cedula = datos[0]
            nombre = datos[1]
            label = f"{cedula}\\n{nombre}"
            node = f"node{idx}"
            dot.node(node, label)
            if last:
                dot.edge(last, node)
            last = node
            idx += 1
            p = p.prox

        path = os.path.join(os.path.dirname(__file__), "grafo_lista")
        dot.render(path, cleanup=True)
        img = Image.open(path + ".png")
        img = img.resize((800, 300), Image.Resampling.LANCZOS)
        self.img_grafo = ImageTk.PhotoImage(img)
        self.label_img_grafo.config(image=self.img_grafo)

if __name__ == "__main__":
    root = tk.Tk()
    app = VistaListaApp(root)
    root.mainloop()
