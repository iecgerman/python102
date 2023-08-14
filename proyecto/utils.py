def obtener_productos(producto_dict):
  precios_dict = {
    'ProductoID': producto_dict['ProductoPrecio']
  }

  labels = precios_dict.keys()
  values = precios_dict.values()
  return labels, values

def precio_por_producto(dataPcymac, precio):
  result = list(filter(lambda item: item['ProductoPrecio'] == precio, dataPcymac))
  print(result)