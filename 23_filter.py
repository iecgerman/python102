"""🤿 Filter (Clase#23)"""

numeros = [1,2,3,4,5]
numeros_pares = filter(lambda x: x % 2 == 0, numeros) # tambien puede ir list()antes de filter para no obtener solo la referencia

print(list(numeros_pares))

