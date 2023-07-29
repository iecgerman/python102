items = [
  {
    'product': 'camisa', 
    'price': 100
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'tenis',
    'price': 200
  }
]

"""def add_taxes(item): 
  item['taxes'] = item['price'] * .19
  return item  """

# usamos copy(), que es una funcion que copia todos los valores de esa referencia y asi estamos creando otro diccionario con los mismos valores.
def add_taxes(item): 
  new_item = item.copy() # me falto ()
  new_item['taxes'] = new_item['price'] * .19
  return new_item

new_items = list(map(add_taxes, items)) 
print("NEW LIST")
print(new_items)
print("OLD LIST")
print(items)

# ahora si nos respeta la lista original y no hace una referencia en memoria para modificarla, a esto se le llama metodo de inmutabilidad
# [{'product': 'camisa', 'price': 100}, {'product': 'pantalones', 'price': 300}, {'product': 'tenis', 'price': 200}]