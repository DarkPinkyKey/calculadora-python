import auxiliar


def bucleLista():
    listaNums = []
    while True:
        numIntroducido = input()
        if numIntroducido == "=":
            break
        elif auxiliar.esNumero(numIntroducido):
            listaNums.append(float(numIntroducido))
        else:
            print("Operación cancelada: El número introducido no es válido.")
            break

        return listaNums


def sumar():
    print("Ingrese los números que quiere sumar: ")
    listaNums = bucleLista()

    total = listaNums[0]
    for x in listaNums:
        total = total + x

        print("Total de la suma de números: ", total)


def restar():
    print("Ingrese los números que quiere restar: ")
    listaNums = bucleLista()

    total = 0
    for x in listaNums:
        total - x

        print("Total de la suma de números: ", total)


def multipicar():
    print("Ingrese los números que quiere sumar: ")
    listaNums = bucleLista()

    total = listaNums[0]
    for x in listaNums:
        total = total * x

        print("Total de la suma de números: ", total)


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
