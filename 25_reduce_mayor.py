"""por si alguna persona quería saber como se sacaba el mayor valor de una lista (es que me quede pensativo cuando lo menciono)"""

import functools 
num = [8, 1, 2, 3, 4]
def mayor(counter, item):
  if counter <= item:
    return item
  else:
    return counter
result = functools.reduce(mayor, num) 
print (result)


# HALLARELMAXIMO
import functools
lista = [2,4,5,9,8,2,1]
max = functools.reduce(lambda a,b: a if a>b else b, lista )
print("Maximo : ")
print(max)

#solo me sale ejecutandolo en el main.py
"""import functools
numbers2 = [1,2,3,4]
result2 = functools.reduce(max, numbers2)
print(result2)"""


# otra forma que solo me sale ejecutandolo en el main.py
from functools import reduce

numbers = (3012,63,1,121,23,5334)
print(f'Lista original: \n{numbers}')

def mayor(numbers):
  result = reduce(max, numbers)
  return result

max_num = mayor(numbers)
print(f'Numero Máximo 👇 \n{max_num}')