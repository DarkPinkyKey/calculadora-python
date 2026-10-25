import operaciones


# Menu
def mostrarMenu():
    print("\n CALCULADORA ")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def iniciarPrograma():
    while True:
        mostrarMenu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            operaciones.sumar()
        elif opcion == "2":
            operaciones.restar()
        elif opcion == "3":
            operaciones.multipicar()
        elif opcion == "4":
            operaciones.dividir()
        elif opcion == "5":
            print("Fin del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige entre 1 y 5.")


if __name__ == "__main__":
    iniciarPrograma()
