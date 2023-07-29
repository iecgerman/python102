# Higher order function: una función dentro de otra función

"""
Normalmente solemos usar parámetros y argumentos como sinónimos, y en la práctica podemos inferir lo que esto significa según el contexto. Pero en un entorno profesional, deberíamos tener muy claro que los parámetro son las reglas o instrucciones que definimos dentro de la función, mientras los argumentos son los datos que le pasamos a la función para que los “reemplace” y ejecute la función.

Algo así como en matemáticas básicas, cuando definimos y = x^2 + x + 3, la derecha de la ecuación serían los parámetros, mientras que los argumentos, serían los valores que le asignamos a la x, bien sea para encontrar las coordenadas de un punto (una iteración), o para trazar la gráfica completa (multiples iteraciones)…

**Parámetros: **Reglas Internas de la Función.

**Argumentos: **Datos Externos que le Pasamos a la Función para que Pueda Hacer sus Cálculos.
"""

def incrementar(x):
  return x + 1

incrementar_v2 = lambda x : x + 1

def hof(x, func): # como parametro de entrada va a tener otra funcion
  return x + func(x)

hof_v2 = lambda x, func : x + func(x)

resultado = hof(2, incrementar) # se pone la funcion sin los parentesis
# 2 + (2 + 1)
print(resultado)

resultado = hof_v2(2, incrementar_v2)
print(resultado)
resultado = hof_v2(2, lambda x : x + 2)
print(resultado)
resultado = hof_v2(2, lambda x : x * 5)
print(resultado)


"""
Higher order function: una función dentro de otra función
Una función de Orden Superior o en sus siglas HOF se le lama así solo cuando contiene otras funciones como parámetro de entrada o devuelve una función como salida, es decir que en este caso las funciones que operan a otras funciones se les denomina Higher order function.

También hay que entender que a estas Funciones de Orden Superior HOF se aplican para funciones y métodos que toman como funciones a los parámetros o devuelven una función como un resultado.

Propiedades de HOF
Una función es una instancia de tipo objeto.
Puede almacenar una función en una variable.
Puede pasar una función como un parámetro a otra función.
Puede devolver la función desde una función.
Se puede almacenar en una estructura de datos como tablas, listas, etc.
"""