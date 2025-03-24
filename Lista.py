class Nodo:
    def __init__(self, valor):
        # Inicializa un nodo con un valor y un puntero a None
        self.info = valor
        self.prox = None

class Lista:
    def __init__(self):
        # Inicializa la lista con el primer nodo como None
        self.primero = None

    def vacia(self):
        # Verifica si la lista está vacía
        return self.primero is None

    def llena(self):
        # Intenta crear un nuevo nodo para verificar si hay memoria disponible
        try:
            _ = Nodo(None)  # Intentar crear un nodo
            return False
        except MemoryError:
            return True  # Si no se puede crear, la lista está llena

    def ins_comienzo(self, valor):
        # Inserta un nuevo nodo al comienzo de la lista
        if not self.llena():
            nuevo = Nodo(valor)  # Crea un nuevo nodo
            nuevo.prox = self.primero  # El nuevo nodo apunta al antiguo primero
            self.primero = nuevo  # Actualiza el primero a ser el nuevo nodo
            return True
        return False  # No se pudo insertar porque la lista está llena

    def eli_comienzo(self):
        # Elimina el nodo al comienzo de la lista y devuelve su valor
        if not self.vacia():
            viejo = self.primero  # Guarda el nodo a eliminar
            self.primero = self.primero.prox  # Actualiza el primero al siguiente nodo
            return viejo.info  # Devuelve el valor del nodo eliminado
        return None  # No se pudo eliminar porque la lista está vacía

    def contar(self):
        # Cuenta el número de nodos en la lista
        cont = 0
        p = self.primero
        while p is not None:
            cont += 1  # Incrementa el contador por cada nodo
            p = p.prox  # Avanza al siguiente nodo
        return cont  # Devuelve el total de nodos

    def buscar(self, valor):
        # Busca un nodo con un valor específico y lo devuelve
        aux = self.primero
        while aux is not None:
            if aux.info == valor:  # Si se encuentra el valor
                return aux  # Devuelve el nodo encontrado
            aux = aux.prox  # Avanza al siguiente nodo
        return None  # No se encontró el valor

    def pasar_lista_aux(self, lista_fuente, lista_destino):
        # Transfiere todos los nodos de lista_fuente a lista_destino
        while not lista_fuente.vacia():
            valor = lista_fuente.eli_comienzo()  # Elimina el primer nodo de lista_fuente
            lista_destino.ins_comienzo(valor)  # Inserta el valor en lista_destino
