"""Podemos importar todo un módulo de un paquete y nombrándolo con la palabara clave as

# mod_2.py
import package.mod_2 as mod_2

print(mod_2.func_3())
print(mod_2.func_4())"""

# TODO ESTO LO PUSO EN main.py


"""from pkg.mod_1 import func_1, func_2
from pkg.mod_2 import func_3, func_4

print(func_1())
print(func_2())
print(func_3())
print(func_4())"""

import pkg
print(pkg.URL)
print(pkg.mod_1.func_1()) # esto es debil y puede causar error y funcina porque ya hicimos la importacion de esos modulos en las lineas 1 y 2

# para que no genere error hay que ir al __init__.py e importar los modulos

# esto es la mejor practica o la mejor forma de llamar al paquete y es lo que se le conoce como namespace, o nombre reservado, es decir voy al paquete, llamo al modulo y llamo a la funcion print(pkg.mod_1.func_1())


"""PAQUETES
Los paquetes son las carpetas que contienen varios módulos y cada uno con una función distinta.

Para ello debe tener siempre un archivo de nombre __init__.py (por lo general esta vacio, ya que así es compatible con programas python versiones anteriores a la 3), con esto le estamos indicado a python que esto se trata de un paquete y no de una carpeta.

Para acceder a los módulos de los paquetes podemos utilizar estas opciones:
import nombrecarpeta.nombremodulo
from nombrecarpeta import nombremodulo
from nombrecarpeta.nombremodulo import def"""