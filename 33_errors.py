"""try: 
  print(0 / 0)
except ZeroDivisionError as error:
  print(error)

try:
  assert 1 != 1, 'uno no es igual que uno'
except AssertionError as error: #ojo con los 2 puntos (:)
  print(error)

try:
  age = 10
  if age < 18:
    raise Exception('No se permite menores de edad')
except Exception as error: # de nuevo los :
  print(error)

print('hola')"""

# una buena práctica en la ingeniería es hacer tracking o registrar todo en un sistema de errores, pero luego tener un reporte de fallos

# tambien puedes meter todo en un solo try

try: 
  print(0 / 0)
  assert 1 != 1, 'uno no es igual que uno'
  age = 10
  if age < 18:
    raise Exception('No se permite menores de edad')

except ZeroDivisionError as error:
  print(error)
except Exception as error:
  print(error)
except AssertionError as error:
  print(error)

print('hola')
print('hola 2')

"""A primera vista podemos pensar que lanzar Excepciones no sirve de nada si al final igual ahí mismo las vamos a rodear de un try-except. Pero es más util cuando estamos creando funciones en modulos que van a ser usadas por otros módulos, funciones que dependiendo del uso que se le de en una u otra parte del código del proyecto tienen que hacerse diferentes validaciones para ese “error”.
Generar excepciones OBLIGA al equipo a manejarlos porque sino, el proyecto no va a funcionar."""