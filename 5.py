numeros = [10,5,27,8,42,14]

def encontraMaxMin(lista):
    if len(lista) == 0:
        return None, None
    max = lista[0]
    min = lista[0]
    for numero in lista:
        if numero > max:
            max = numero
        if numero < min:
            min = numero

    return max, min

maximo, minimo = encontraMaxMin(numeros)
print(maximo)
print(minimo)
