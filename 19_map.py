lista_numeros = [1,2,3,4]
numeros_v2 = []
for numero in lista_numeros:
  numeros_v2.append(numero*2)

numeros_con_map = map(lambda numero: numero*2, lista_numeros)

print(lista_numeros)
print(numeros_v2) # [2, 4, 6, 8]
print(numeros_con_map) # nos envia un iterable <map object at 0x7f4aa630f1c0>
print(list(numeros_con_map)) # [2, 4, 6, 8]


lista_1 = [1,2,3,4]
lista_2 = [5,6,7]

print(lista_1)
print(lista_2)
result = list(map(lambda x,y: x + y, lista_1, lista_2))
print(result)

print("------------------------")

"""MAP( )
La función map () ejecuta una función especifica para cada elemento en un iterable y el elemento se envía a la función como un parámetro.

Sintaxis.
map(function, iterables)

Con esto vamos hacer unos deliciosos tacos, para ello utilizáremos maps()"""

ingredientes = ('carne', 'maiz', 'aguacate')
ingredientes_2 = ('molida', 'tacos', 'guacamole')
menu = list(map(lambda a, b: a + ' es a ' + b, ingredientes, ingredientes_2))
print(menu)

# ['carne es a molida', 'maiz es a tacos', 'aguacate es a guacamole']

