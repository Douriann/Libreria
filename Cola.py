from Lista import Nodo

class Cola:
  
  def __init__(self):
    self.frente = None
    self.final = None
  
  def vacia(self):
    return self.frente is None
  
  def llena(self):
    try:
      _ = Nodo() #Crea un nuevo nodo para verificar que haya espacio en memoria
      return False 
    except MemoryError: #Si no hay espacio en memoria retorna True
      return True

  def insertar(self, valor):
    #Verifica que la lista no esta llena
    if not self.llena():
      nuevo = Nodo() #Crea un nuevo nodo
      nuevo.info = valor  #Asigna el valor al nuevo nodo
      nuevo.prox = None #Indica al nuevo nodo que no tiene ningun elemento al frente
      if self.final is None:  #Verifica si no hay elementos en la cola
        self.frente = nuevo #Agrega el primer elemento
      else: #Si ya existen elementos en la cola agrega el nuevo nodo al final
        self.final.prox = nuevo 
      self.final = nuevo #Asigna el nuevo nodo como el ultimo
      return True
    
    return False
  
  def remover(self):
    
    #Verifica que la lista no esta vacia
    if not self.vacia():
      self.frente = self.frente.prox #Eliminamos el primer nodo de la cola
      if self.frente is None: #Si la cola no posee mas nodos se regresa a su valor inicial
        self.final = None
      return True
    
    return False