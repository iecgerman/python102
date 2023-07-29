"""
dict = {}
for i in range(1,5): # i va a ser la clave
  dict[i] = i * 2

print(dict)

# dict comprehentions

dict_v2 = { i: i*2 for i in range(1,5)}
print(dict_v2)
import random

countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
  population[country] = random.randint(1,100)
  # country es la key

print(population)

# dict comprehentions

population_v2 = { country: random.randint(1,100) for country in countries } # la llave es country y el valor es random.ranint(1,100)

print(population_v2)
"""

names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

# la funcion zip sirve para unir listas

print(list(zip(names, ages))) # [('nico', 12), ('zule', 56), ('santi', 98)]

new_dict = { name: age for (name, age) in zip(names, ages) }
print(new_dict)

print('---------------------comentario----------------------')

lista_nombres = ['nico', 'zule', 'santi', 'carlos']
lista_edades = [12, 56, 98, 67]

new_dict = {lista_nombres[i]: lista_edades[i] for i in range(len(lista_edades)) }
print(new_dict)

print('---------------------comentario----------------------')

# El truco es convertir la tupla a diccionario con dict.
dict2=dict(zip(names,ages))
print(dict2)

print('---------------------comentario----------------------')

# Hay otras formas para llegar al mismo resultado, entre ellas esta la siguiente:

# Opcion 1
new_dict = {}
for i in range(len(names)):
    item = names[i]
    new_dict[item] = ages[i]  
print(new_dict)

# Opcion 2
new_dict = {names[i] : ages[i] for i in range(len(names))}
print(new_dict)  