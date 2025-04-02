


from Pila import Pila, NodoPila
from Colas import Cola, Nodo
from Lista import Lista, Nodo

def menu():
    #este es el menu para seleccionar con que  trabajar
    print("\nSeleccione la estructura de datos con la que desea trabajar:")
    print("1. Pila")
    print("2. Cola")
    print("3. Lista")
    print("4. Salir")

def menu_pila():
   
    print("\nOpciones para la Pila:")
    print("1. Insertar en la Pila")
    print("2. Remover de la Pila")
    print("3. Ver Tope de la Pila")
    print("4. Mostrar valores de la Pila")
    
    print("5. Volver al menú principal")

def menu_cola():
    
    print("\nOpciones para la Cola:")
    print("1. Insertar en la Cola")
    print("2. Remover de la Cola")
    print("3. Ver Frente de la Cola")
    print("4. Mostrar valores de la Cola")
    
    print("5. Volver al menú principal")

def menu_lista():
    
    print("\nOpciones para la Lista:")
    print("1. Insertar al comienzo de la lista")
    print("2. Eliminar del comienzo de la lista")
    print("3. Contar elementos en la lista")
    print("4. Buscar un valor en la lista")
    print("5. Mostrar valores de la lista")
    
    print("6. Volver al menú principal")

def main():
    pila = Pila()
    cola = Cola()
    lista = Lista()
#segun la opcion que seleccionen apareceran las opciones que pueden elegir:
    while True:
        menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
          
            while True:
                menu_pila()
                opcion_pila = input("Ingrese una opción para Pila: ")

                if opcion_pila == "1":
                    valor = input("Ingrese el valor a insertar en la Pila: ")
                    pila.Insertar(valor)
                elif opcion_pila == "2":
                    valor = pila.Remover()
                    if valor is not None:
                        print(f"Se removió: {valor}")
                    else:
                        print("La Pila está vacía.")
                elif opcion_pila == "3":
                    tope = pila.ObtTope()
                    if tope is not None:
                        print(f"El Tope de la Pila es: {tope.info}")
                    else:
                        print("La Pila está vacía.")
                elif opcion_pila== "4":
                    pila.MostrarContenido()
                elif opcion_pila == "5":
                    break
                else:
                    print("Opción inválida.")

        elif opcion == "2":
           
            while True:
                menu_cola()
                opcion_cola = input("Ingrese una opción para Cola: ")

                if opcion_cola == "1":
                    valor = input("Ingrese el valor a insertar en la Cola: ")
                    cola.Insertar(valor)
                elif opcion_cola == "2":
                    valor = cola.Remover()
                    if valor is not None:
                        print(f"Se removió: {valor}")
                    else:
                        print("La Cola está vacía.")
                elif opcion_cola == "3":
                    frente = cola.Frente
                    if frente is not None:
                        print(f"El Frente de la Cola es: {frente.info}")
                    else:
                        print("La Cola está vacía.")
                elif opcion_cola== "4":
                    cola.MostrarContenido()
                elif opcion_cola == "5":
                    break
                else:
                    print("Opción inválida.")

        elif opcion == "3":
          
            while True:
                menu_lista()
                opcion_lista = input("Ingrese una opción para Lista: ")

                if opcion_lista == "1":
                    valor = input("Ingrese el valor a insertar al comienzo de la Lista: ")
                    lista.InsComienzo(valor)
                elif opcion_lista == "2":
                    valor = lista.EliComienzo()
                    if valor is not None:
                        print(f"Se eliminó: {valor}")
                    else:
                        print("La Lista está vacía.")
                elif opcion_lista == "3":
                    print(f"Elementos en la lista: {lista.Contar()}")
                elif opcion_lista == "4":
                    valor = input("Ingrese el valor a buscar en la Lista: ")
                    nodo = lista.Buscar(valor)
                    if nodo is not None:
                        print(f"Valor {valor} encontrado en la lista.")
                    else:
                        print(f"Valor {valor} no encontrado en la lista.")
                elif opcion_lista== "5":
                    lista.MostrarContenido()
                elif opcion_lista == "6":
                    break
                else:
                    print("Opción inválida.")

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
