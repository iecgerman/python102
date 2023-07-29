# Multiplica todos los elementos por dos

# Que bonito se siente el haber hecho esto sólo y a la primera en menos de 2 min =D

def duplicados(lista_numeros): # definimos una funcion llamada duplicados con su parametro lista_numeros
  resultado = list(map(lambda num: num*2, lista_numeros)) # creamos la variable resultado la cual contiene la funcion map que esta misma contiene una funncion lambda que multiplicara por 2 casa numero de la lista_numeros y tambien usamos list para poderimprimirlos como lista
  return resultado # recordemos que si no ponemos list en antes de la fuincion map lo podemos poner aqui antes de resultado para que no nos imprima un valor iterable

# en la solucion lo ponen despues del return solo que ahi ya no creas la variable resultado

# return list(map(lambda num: num*2, lista_numeros))

lista_numeros = [1,2,3,4,5,62,234,] 

respuesta = duplicados(lista_numeros)
print(respuesta) # [2, 4, 6, 8, 10, 12]