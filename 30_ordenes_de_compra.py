# aqui lo importante es que tenemos una carpeta que serian nuestros paquetes que contiene modulos los cuales contienen las funciones

from paquetes.modulo_1 import obtener_totales
from paquetes.modulo_2 import calcular_total

def obtener_total(ordenes_de_compra):
  totales = obtener_totales(ordenes_de_compra)
  return calcular_total(totales)

ordenes_de_compra = [
  {
    "nombre_de_cliente": "Nicolas",
    "total": 100,
    "entregado": True,
  },
  {
    "nombre_de_cliente": "Zulema",
    "total": 120,
    "entregado": False,
  },
  {
    "nombre_de_cliente": "Santiago",
    "total": 20,
    "entregado": False,
  }
]

total = obtener_total(ordenes_de_compra)
print(total) # 240 y se pudo ejecutar como script desde python 30_ordenes_de_compra.py

# la mejor practica es usando name space (nombres reservados) y creamos __init.py__ por si se ejecuta desde versiones anterioes a la 3.3 y desde ahi importamos