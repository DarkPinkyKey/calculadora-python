def esNumero(num):
    try:
        num = float(num)
        return True
    except ValueError:
        return False
