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

        return listaNums


def resultadoOperacion(num):
    listaNums = bucleLista()
    total = listaNums[0]
    listaNums.pop(0)
    for x in listaNums:
        match num:
            # Suma
            case "1":
                total = total + x
            case "2":
                total = total - x
            case "3":
                total = total * x
            case "3":
                total = total / x
            case _:
                print("No se reconoce número introducido")


def sumar():
    print("Ingrese los números que quiere sumar: ")
    listaNums = bucleLista()

    total = listaNums[0]
    listaNums.pop(0)
    for x in listaNums:
        total = total + x

        print("Total de la suma de números: ", total)


def restar():
    print("Ingrese los números que quiere restar: ")
    listaNums = bucleLista()

    total = listaNums[0]
    listaNums.pop(0)
    for x in listaNums:
        total = total - x

        print("Total de la resta de números: ", total)


def multipicar():
    print("Ingrese los números que quiere multiplicar: ")
    listaNums = bucleLista()

    total = listaNums[0]
    listaNums.pop(0)
    for x in listaNums:
        total = total * x

        print("Total de la multiplicación de números: ", total)


def dividir():
    print("Ingrese los números que quiere dividir: ")
    listaNums = bucleLista()

    total = listaNums[0]
    listaNums.pop(0)
    indexBucle = 0
    for x in listaNums:
        indexBucle += 1
        if listaNums[indexBucle] == 0:
            print("No se puede dividir entre 0")
        else:
            total = total / x

            print("Total de la división de números: ", total)
