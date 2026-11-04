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
            return listaNums

    if not listaNums:
        listaNums.append(0)

    return listaNums


def resultadoOperacion(num, lista):
    if len(lista) == 1:
        return lista[0]

    listaNums = lista
    total = listaNums[0]
    listaNums.pop(0)
    for x in listaNums:
        match num:
            case 1:  # Suma
                total = total + x
            case 2:  # Resta
                total = total - x
            case 3:  # Multiplicación
                total = total * x
            case 4:  # División
                if x == 0:
                    print("No se puede dividir entre 0")
                    break
                else:
                    total = total / x
            case _:
                print("No se reconoce número introducido")

    return total


def sumar():
    print("Ingrese los números que quiere sumar: ")
    listaNums = bucleLista()

    total = resultadoOperacion(1, listaNums)

    print("Total de la suma de números: ", total)


def restar():
    print("Ingrese los números que quiere restar: ")
    listaNums = bucleLista()

    total = resultadoOperacion(2, listaNums)

    print("Total de la resta de números: ", total)


def multipicar():
    print("Ingrese los números que quiere multiplicar: ")
    listaNums = bucleLista()

    total = resultadoOperacion(3, listaNums)

    print("Total de la multiplicación de números: ", total)


def dividir():
    print("Ingrese los números que quiere dividir: ")
    listaNums = bucleLista()

    total = resultadoOperacion(4, listaNums)

    print("Total de la división de números: ", total)
