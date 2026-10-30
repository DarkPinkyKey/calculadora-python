def sumar():
    valor1 = input("Introduce el primer valor: ")
    valor2 = input("Introduce el segundo valor: ")
    try:
        valor1 = float(valor1)
        valor2 = float(valor2)
        resultado = valor1 + valor2
        print("Resultado de la suma: ", resultado)
    except ValueError:
        print("No es un número.")


def restar():
    valor1 = input("Introduce el primer valor: ")
    valor2 = input("Introduce el segundo valor: ")
    try:
        valor1 = float(valor1)
        valor2 = float(valor2)
        resultado = valor1 - valor2
        print("Resultado de la resta: ", resultado)
    except ValueError:
        print("No es un número.")


def multipicar():
    valor1 = input("Introduce el primer valor: ")
    valor2 = input("Introduce el segundo valor: ")
    try:
        valor1 = float(valor1)
        valor2 = float(valor2)
        resultado = valor1 * valor2
        print("Resultado de la multiplicación: ", resultado)
    except ValueError:
        print("No es un número.")


def dividir():
    valor1 = input("Introduce el primer valor: ")
    valor2 = input("Introduce el segundo valor: ")
    try:
        valor1 = float(valor1)
        valor2 = float(valor2)
        if valor2 > 0:
            resultado = valor1 / valor2
            print("Resultado de la división: ", resultado)
        else:
            print("No se puede dividir entre 0")
    except ValueError:
        print("No es un número.")
