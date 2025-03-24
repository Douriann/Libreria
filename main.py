from Lista import Lista

def mostrar_menu():
    print("\n--- Menú de Prueba ---")
    print("1. Insertar elemento al inicio (Lista 1)")
    print("2. Eliminar elemento al inicio (Lista 1)")
    print("3. Contar elementos (Lista 1)")
    print("4. Buscar elemento (Lista 1)")
    print("5. Transferir todos a Lista 2")
    print("6. Mostrar estado de listas")
    print("7. Salir")

def mostrar_estado(lista1, lista2):
    print("\n=== Estado Actual ===")
    print("Lista 1 - Elementos:", lista1.contar(), "| Vacía:", lista1.vacia())
    print("Lista 2 - Elementos:", lista2.contar(), "| Vacía:", lista2.vacia())

if __name__ == "__main__":
    lista1 = Lista()
    lista2 = Lista()
    
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                valor = int(input("Ingrese el valor a insertar: "))
                if lista1.ins_comienzo(valor):
                    print(f"✅ {valor} insertado correctamente")
                else:
                    print("❌ Error: Lista llena o memoria no disponible")
                    
            elif opcion == 2:
                valor = lista1.eli_comienzo()
                if valor is not None:
                    print(f"🗑️ Elemento eliminado: {valor}")
                else:
                    print("❌ La lista está vacía")
                    
            elif opcion == 3:
                print(f"🔢 Total elementos en Lista 1: {lista1.contar()}")
                
            elif opcion == 4:
                valor = int(input("Ingrese el valor a buscar: "))
                resultado = lista1.buscar(valor)
                print(f"🔍 {'Encontrado' if resultado else 'No encontrado'}")
                
            elif opcion == 5:
                lista1.pasar_lista_aux(lista1, lista2)
                print("🔄 Elementos transferidos a Lista 2")
                
            elif opcion == 6:
                mostrar_estado(lista1, lista2)
                
            elif opcion == 7:
                print("👋 Saliendo del programa...")
                break
                
            else:
                print("❌ Opción no válida")
                
        except ValueError:
            print("❌ Error: Ingrese un número válido")
            
        input("\nPresione Enter para continuar...")