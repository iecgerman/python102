"""💩 Reduce (Clase#25)"""

import functools

numeros = [1,2,3,4]

def accum(counter, item):
  print('counter => ', counter)
  print('   item => ', item)
  return counter + item

#result = functools.reduce(lambda counter, item: counter + item, numeros)
result = functools.reduce(accum, numeros)

print(result)

"""
La función reduce()

reduce() es una función incorporada de Python 2, que toma como argumento un conjunto de valores (una lista, una tupla, o cualquier objeto iterable) y lo “reduce” a un único valor. Cómo se obtiene ese único valor a partir de la colección pasada como argumento dependerá de la función aplicada.

Por ejemplo, el siguiente código reduce la lista [1, 2, 3, 4] al número 10 aplicando la función accum(counter, item), que retorna la suma de sus argumentos.

<
def accum(counter, item):
	return counter + item

print(reduce(accum, [1, 2, 3, 4]))
> 
La función pasada como primer argumento debe tener dos parámetros. reduce() se encargará de llamarla de forma acumulativa (es decir, preservando el resultado de llamadas anteriores) de izquierda a derecha. De modo que el código anterior es similar a:

<
print(accum(accum(accum(1, 2), 3), 4))
> 
Es decir, la operación realizada es ((1 + 2) + 3) + 4, de la que resulta 10.

A partir de Python 3 la función fue movida al módulo estándar functools.
"""