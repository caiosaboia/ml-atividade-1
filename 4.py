pessoasLista = [("Joao", 30), ("Antonio", 25), ("Pedro", 35), ("Guilherme", 22), ("Abigaiu",20)]

def ordenaPorNome(pessoasLista):
    listaOrdenada = sorted(pessoasLista, key=lambda pessoa: pessoa[0])
    return listaOrdenada


print(ordenaPorNome(pessoasLista))