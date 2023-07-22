# Elimina elementos duplicados usando conjuntos

"""
Para resolver este desafío, debes escribir un algoritmo que elimine los elementos repetidos para obtener un conjunto único llamado new_set.

Este algoritmo recibirá como entrada cuatro conjuntos de países, estos países serán de todo el continente americano divididos de la siguiente manera:

countries - Países del continente en general.
northAmerica - Países del norte de América.
centralAmerica - Países del centro de América.
southAmerica - Países del sur de América.
En resumen, el algoritmo deberá eliminar los elementos repetidos de los cuatro conjuntos de países y obtener un conjunto único llamado new_set.

Ejemplo 1:

Input: 
{"MX", "COL", "ARG", "USA"},
{"USA", "CA"},
{"MX", "GT", "BZ"},
{"COL", "BZ", "ARG"}

Output:
{'ARG', 'USA', 'CANADA', 'GT', 'COL', 'MX', 'BZ'}

Ejemplo 2:

Input:
{"BOL"},
{"CA"},
{"MX"},
{"COL"}

Output:

{'COL', 'CA', 'BOL', 'MX'}
"""

countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

# union "|"
new_set = countries | northAm | centralAm | southAm
print(countries | northAm | centralAm | southAm)

new_set = set()
new_set = countries.union(northAm, centralAm, southAm)
print(new_set)

# intersection "|"
new_set = centralAm.intersection(southAm)
print(new_set)

print(centralAm & southAm)

# difference "-"
new_set = countries.difference(centralAm)
print(new_set)

print(countries - centralAm)

# symmetric_difference "^"
new_set = centralAm.symmetric_difference(southAm)
print(new_set)

print(centralAm ^ southAm)