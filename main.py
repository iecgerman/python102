# otra forma que solo me sale ejecutandolo en el main.py
from functools import reduce

numbers = (3012,63,1,121,23,5334)
print(f'Lista original: \n{numbers}')

def mayor(numbers):
  result = reduce(max, numbers)
  return result

max_num = mayor(numbers)
print(f'Numero Máximo 👇 \n{max_num}')