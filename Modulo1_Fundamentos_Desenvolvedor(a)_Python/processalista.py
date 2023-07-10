def maior_impar(lista):
    impares = [num for num in lista if num % 2 != 0]
    if impares:
        return max(impares)
    else:
        return None

def menor_impar(lista):
    impares = [num for num in lista if num % 2 != 0]
    if impares:
        return min(impares)
    else:
        return None

def maior_e_menor_impar(lista):
    impares = [num for num in lista if num % 2 != 0]
    if impares:
        return max(impares), min(impares)
    else:
        return None, None

