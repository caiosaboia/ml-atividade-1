lista = [1,2,3,4,5,6,7,8,9]

def retornaPrimo(lista):
  listaSaida = []
  for numeros in lista:
      eh_primo = True
      for divisores in range(2,numeros): 
          if numeros % divisores == 0: 
              eh_primo = False
              break
      
      if eh_primo == True:
          listaSaida.append(numeros)
  return listaSaida
    
print(retornaPrimo(lista))