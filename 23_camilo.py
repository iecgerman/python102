"""
FILTER
La función filter(), devuelve un valor que esta siendo iterado de la cual su resultado será el valor que se esta buscando en el filter

SINTAXIS
_filter (function, iterable_

Valores.
filter: Una función que se ejecutara para cada elemento iterable
iterable: Lo que se va a filtrar.

Ejercicio:

Tenemos una lista de estudiantes de la cual debemos saber quienes son de Colombia y quienes son considerados mayores de edad al tener igual o mas de 18 años y cuantos son.
"""

people = [
  {
    'name' : 'Pedro',
    'country': 'Colombia',
    'age' : 18,
    'course' : 'developer'
  },
  {
    'name' : 'Juan',
    'country': 'Perú',
    'age' : 17,
    'course' : 'UX'
  },
  {
    'name' : 'Carlos',
    'country': 'Chile',
    'age' : 31,
    'course' : 'Diseño'
  },
  {
    'name' : 'Ana Maria',
    'country': 'Colombia',
    'age' : 25,
    'course' : 'Tester'
  }
]

"""Ahora planteamos el primer problema a resolver, cuales son los estudiantes de Colombia y cuantos son:"""

countrie = list(filter(lambda country: country['country'] == 'Colombia', people))
print(countrie)
print(len(countrie))

# [{'name': 'Pedro', 'country': 'Colombia', 'age': 18, 'course': 'developer'}, {'name': 'Ana Maria', 'country': 'Colombia', 'age': 25, 'course': 'Tester'}]
# 2

"""
Ya sabemos que hay 2 personas en nuestros cursos que son de Colombia quienes son: Pedro y Ana Maria.

Ahora necesitamos saber quienes son considerados mayores de edad al tener 18 años o más.
"""

adult = list(filter(lambda age: age['age'] >= 18, people))
print(adult)
print(len(adult))

# [{'name': 'Pedro', 'country': 'Colombia', 'age': 18, 'course': 'developer'}, {'name': 'Carlos', 'country': 'Chile', 'age': 31, 'course': 'Diseño'}, {'name': 'Ana Maria', 'country': 'Colombia', 'age': 25, 'course': 'Tester'}]
# 3

"""
Con esto podemos saber que hay 3 estudiantes que son considerados mayores de edad al tener 18 años o más quienes serían: Pedro con 18 años, carlos, con 31 años y Ana Maria con 25 años.
"""

