

class NodoPila:
    def __init__(self, valor=None):
        self.info = valor  # Valor del nodo
        self.ap = None     # Referencia al siguiente nodo (para simular el puntero)


class Pila:
    def __init__(self):
        self.Tope = None 

    def Vacia(self):
        #Verifica si la pila esta vacia
        return self.Tope is None

    def Llena(self):
        #Simula la comprobacion de memoria
        try:
           
            nuevo = NodoPila()
            return False  # Si se creo correctamente entonces la pila no esta llena
        except MemoryError:
            return True  # Si ocurre un error de memoria se considera que la pila esta llena

    def Insertar(self, valor):
        #Inserta un valor en la pila
        if not self.Llena():
            nuevo = NodoPila(valor)  # crear un nuevo nodo
            nuevo.ap = self.Tope  # el puntero 'ap' apunta al nodo anterior simulando puntero
            self.Tope = nuevo  # el nuevo nodo pasa a ser el Tope de la pila
            return True
        return False

    def MostrarContenido(self):
        if self.Vacia():
            print("La Pila está vacía.")
        else:
            p = self.Tope
            print("Contenido de la Pila:")
            while p is not None:
                print(p.info)
                p = p.ap
                
    def Remover(self):
        #Remueve el valor del Tope de la pila y lo devuelve
        if not self.Vacia():
            viejo = self.Tope  # el nodo actual del Tope
            valor = viejo.info  # recuperamos el valor del nodo
            self.Tope = viejo.ap  # el Tope pasa al siguiente nodo simulando desapilar
            return valor
        return None 

    def ObtTope(self):
        #Obtiene el nodo en el Tope de la pila
        return self.Tope

    def AsigTope(self, nodo):
        #Asigna un nuevo nodo al Tope de la pila
        self.Tope = nodo

    def ObtInfo(self, nodo):
        #Obtiene la informacion almacenada en el nodo
        return nodo.info

    def AsigInfo(self, nodo, valor):
        #Asigna un nuevo valor al nodo
        nodo.info = valor


# Seccion para verificar el funcionamiento de la pila
if __name__ == "__main__":
   
    mi_pila = Pila()

    # Verificar si la pila esta vacia
    print("¿Está la pila vacía?", mi_pila.Vacia())  # deberia imprimir True

    # Insertar elementos
    print("Insertando 10:", mi_pila.Insertar(10))  # deberia devolver True
    print("Insertando 20:", mi_pila.Insertar(20))  # deberia devolver True
    print("Insertando 30:", mi_pila.Insertar(30))  # deberia devolver True

    # Verificar si la pila esta vacia despues de que se agrego 10,20,30
    print("¿Está la pila vacía?", mi_pila.Vacia())  # Deberia imprimir False

    # Obtener el tope de la pila
    tope = mi_pila.ObtTope()
    print("Tope de la pila:", tope.info)  # deberia imprimir un 30

    # Remover elementos de la pila
    print("Remover valor:", mi_pila.Remover())  # deberia devolver 30
    print("Remover valor:", mi_pila.Remover())  # deberia devolver 20
    print("Remover valor:", mi_pila.Remover())  # deberia devolver 10

    # Verificar si la pila esta vacia despues de las eliminaciones que se hicieron
    print("¿Esta vacia la pila ?", mi_pila.Vacia())  # deberia imprimir True

    # Intentar remover un elemento de una pila vacia
    print("Intentando remover de una pila vacía:", mi_pila.Remover())  # deberia devolver None
