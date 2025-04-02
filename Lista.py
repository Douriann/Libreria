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
    
    def ins_despues(self, indice, valor):
        #Inserta elemento despues del nodo X
        if (indice < 0 or indice > self.contar()):
            raise Exception("Indice inválido") #Si el indice no se encuentra, entrega excepción
        elif (indice == 0):
            self.ins_comienzo(valor) #Si el indice es 0, inserta al comienzo
            return
        else:
            cont = 0    #Contador para recorrer la lista
            ins_der = self.primero #Se llama al primer nodo
            #Recorre la lista hasta el nodo indicado
            while ins_der:
                if (cont == indice - 1):
                    #Si el contador es igual al indice, se inserta el nuevo nodo
                    nuevo = Nodo(valor)
                    # El valor del nuevo nodo apunta al siguiente nodo (tomado del nodo indicado)
                    nuevo.prox = ins_der.prox
                    # El nodo indicado apunta al nuevo nodo que se ha creado
                    ins_der.prox = nuevo
                    # Se sale del bucle
                    break
                # Si no se encuentra el nodo indicado, se avanza al siguiente nodo
                # y se incrementa el contador
                ins_der = ins_der.prox
                cont += 1
    
    def eli_despues(self, indice):
        #Elimina elemento despues del nodo X
        if (indice < 0 or indice >= self.contar()): #Si el indice no se encuentra, entrega excepción
            raise Exception("Indice inválido")
        elif (indice == 0):
            self.eli_comienzo() #Si el indice es 0, elimina el primer nodo
        else:
            cont = 0    #Contador para recorrer la lista
            eli_der = self.primero #Se llama al primer nodo
            #Recorre la lista hasta el nodo indicado
            while eli_der:
                if (cont == indice -1):
                    #Si el contador es igual al indice, se elimina el siguiente nodo
                    eli_der.prox = eli_der.prox.prox
                    break
                # Si no se encuentra el nodo indicado, se avanza al siguiente nodo
                # y se incrementa el contador
                eli_der = eli_der.prox
                cont += 1

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
    def mostrar(self):
        #Muestra por pantalla los elementos de la lista
        print("Lista:")
        actual = self.primero
        while actual:
            print(actual.info, end=" -> ")
            actual = actual.prox
        print("Null")
