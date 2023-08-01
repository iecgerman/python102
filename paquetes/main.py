# aqui para que corriera desde main.py dentro de paquetes, elimine paquetes.modulo_1...

from modulo_1 import obtener_totales
from modulo_2 import calcular_total

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
print(total)




"""if __name__ == '__main__':
  obtener_total(ordenes_de_compra)"""