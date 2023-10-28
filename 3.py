lista = [2,4,6,8,10,10]

#com numeros repetidos
def segundoMaiorValor(lista):
    if len(lista) < 2:
        return "Não há segundo maior valor."

    maiorValor = max(lista)
    lista.remove(maiorValor)
    segundoMaior = max(lista)

    return segundoMaior


#sem numeros repetidos
def segundoMaiorValorSemRepetidos(lista):
    if len(lista) < 2:
        return "Não há segundo maior valor."
    
    lista_sem_duplicatas = list(set(lista))

    maiorValor = max(lista_sem_duplicatas)
    lista_sem_duplicatas.remove(maiorValor)
    segundoMaior = max(lista_sem_duplicatas)

    return segundoMaior

print(segundoMaiorValor(lista))
print(segundoMaiorValorSemRepetidos(lista))