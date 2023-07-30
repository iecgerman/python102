import sys # random es un modulo, sys, time, etc.

#print(sys.path) #te da la ruta de donde estas ahorita

import re # expresiones regulares

"""Las Expresiones Regulares son una herramienta muy poderosa, y si estas aprendiendo ciencia de datos las vas a usar cuando apliques web scraping."""

texto = "mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte es 3"

resultado = re.findall("[0-9]+", texto)

print(resultado) # ['311', '123', '121', '57', '3']

import time
timestamp = time.time()
print(timestamp) # 1690679865.2606952

local = time.localtime()
result = time.asctime(local)
print(result) # Sun Jul 30 01:20:23 2023

import collections
numeros = [1,2,2,3,2,67,23,3,3,21,3,45,456,54,6,5,54,768,5,4,4,44,]
contador = collections.Counter(numeros) # Counter debe de ir asi con mayuscula 
print(contador)

"""
Un módulo es un archivo de Python que contiene código que puedes reutilizar en varios programas.

Los módulos te permiten organizar el código de tu programa en unidades más pequeñas y más manejables.

Esto hace que sea más fácil trabajar en grandes proyectos de código y también te permite reutilizar código en varios programas sin tener que copiar y pegar el código en cada programa.

Para usar un módulo en un programa, primero debes importarlo. Puedes hacer esto usando la declaración import.
"""

