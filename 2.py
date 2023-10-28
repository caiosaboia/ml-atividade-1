lista1 = [1,2,3,4,8]
lista2 = [3,4,5,6,7]

def elementosUnicos(lista1, lista2):
    listaUnica = []
    for i in lista1:
        if i not in lista2:
          listaUnica.append(i)
    for t in lista2:
        if t not in lista1:
          listaUnica.append(t)
    
    return listaUnica

print((elementosUnicos(lista1,lista2)))