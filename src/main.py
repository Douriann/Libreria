
from Pila import Pila, NodoPila
from Colas import Cola, Nodo
from Lista import Lista, Nodo
import tkinter as tk
from vista_pilas import VersionControlApp

def main():
    root = tk.Tk()
    app = VersionControlApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
def menu():
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
    print("6. Insertar después de un nodo específico")
    print("7. Eliminar un nodo según su valor")
    print("8. Eliminar después de la posición de un nodo específico")
    print("9. Modificar el valor de un nodo según su posición")
    print("10. Pasar elementos a una lista auxiliar")
    print("11. Pasar elementos de la lista auxiliar a la lista original")
    print("12. Volver al menú principal")

def main():
    pila = Pila()
    cola = Cola()
    lista = Lista()
    lista_aux = Lista()  # Lista auxiliar
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
                elif opcion_pila == "4":
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
                elif opcion_cola == "4":
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
                elif opcion_lista == "5":
                    lista.MostrarContenido()
                elif opcion_lista == "6":
                    valor = input("Ingrese el valor después del cual insertar el nuevo valor: ")
                    nodo = lista.Buscar(valor)
                    if nodo is not None:
                        nuevo_valor = input(f"Ingrese el valor a insertar después de {valor}: ")
                        lista.InsDespues(nodo, nuevo_valor)
                        print(f"Se insertó {nuevo_valor} después de {valor}.")
                    else:
                        print(f"Valor {valor} no encontrado en la lista.")
                elif opcion_lista == "7":
                   
                    valor = input("Ingrese el valor del nodo a eliminar: ")
                    nodo = lista.Buscar(valor)
                    if nodo is not None:
                        if nodo == lista.Primero:
                            
                            lista.EliComienzo()
                        else:
                        
                            previo = lista.Primero
                            while previo is not None and previo.prox != nodo:
                                previo = previo.prox
                            if previo is not None:
                                lista.AsigProx(previo, nodo.prox)  
                                print(f"Se eliminó el nodo con el valor {valor}.")
                            else:
                                print(f"No se encontró el nodo con el valor {valor}.")
                    else:
                        print(f"Valor {valor} no encontrado en la lista.")
                elif opcion_lista == "8":
                    
                    valor = input("Ingrese el valor del nodo después del cual eliminar: ")
                    nodo = lista.Buscar(valor)
                    if nodo is not None:
                        eliminado = lista.EliDespues(nodo)
                        if eliminado is not None:
                            print(f"Se eliminó el nodo después de {valor}. El valor eliminado fue {eliminado}.")
                        else:
                            print(f"No hay un nodo después de {valor}.")
                    else:
                        print(f"Valor {valor} no encontrado en la lista.")
                elif opcion_lista == "9":
                   
                    posicion = int(input("Ingrese la posición del nodo a modificar (comienza desde 0): "))
                    nuevo_valor = input("Ingrese el nuevo valor: ")
                    nodo = lista.Primero
                    for _ in range(posicion):
                        if nodo is not None:
                            nodo = nodo.prox
                        else:
                            print("Posición fuera de rango.")
                            break
                    if nodo is not None:
                        lista.AsigInfo(nodo, nuevo_valor)
                        print(f"Se modificó el valor del nodo en la posición {posicion} a {nuevo_valor}.")
                elif opcion_lista == "10":
                    lista.pasarListaAux(lista, lista_aux)
                    print("Los elementos se han movido a la lista auxiliar.")
                elif opcion_lista == "11":
                    lista_aux.pasarListaAux(lista_aux, lista)
                    print("Los elementos de la lista auxiliar se han movido a la lista original.")
                elif opcion_lista == "12":
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