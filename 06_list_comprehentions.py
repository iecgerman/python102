numbers = []
for element in range(1,11):
  numbers.append(element * 2)

print(numbers)

# Asi seria con list comprehentions
numbers_v2 = [element * 2 for element in range(1,11)]
print(numbers_v2)


numbers = []
for i in range(1,11):
  if i % 2 == 0:
    numbers.append(i * 2)

print(numbers)

# de la forma list comprehentions
numbers_v2 = [i * 2 for i in range(1,11) if i % 2 == 0]
print(numbers_v2)

print('------------------------------------------')

days = ['lunes', 'martes', 'miercoles','jueves','viernes','sabado','domingo']
print(days)

# para ordenar una lista de la "a" a la "z" usamos el metodo sort()
days.sort()
print(days)

new_list = []

for i in days:
  if "a" in i:
    new_list.append(i)

print(new_list) # ['martes', 'sabado']

# con list comprehension seria:

new_list = [i for i in days]
print(new_list)

new_list = [i for i in days if 'a' in i]
print(new_list)

print('------------------------------------------')

# https://www.hackerrank.com/challenges/list-comprehensions/problem

# video de permutaciones: https://www.youtube.com/watch?v=3svszuOz368

x = int(input('write a number: ')) + 1
y = int(input('write a number: ')) + 1
z = int(input('write a number: ')) + 1
n = int(input('write a number: ')) + 1

permutations = [[i,j,k ] for i in range(0,x) for j in range(0,y) for k in range(0,z) if i + j + k != n]
print(permutations)
print(len(permutations))
