items = [
  {
    'product': 'camisa', #loque se encuentra entre los {} es el item
    'price': 100
  },# <= OJO CON LAS COMAS
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'tenis',# ojo con las comas
    'price': 200
  }
]

prices = list(map(lambda item: item['price'], items))
print(prices) # [100, 300, 200]

# Ahora vamos a agregarle un atributo nuevo al dic items

# no nos va funcionar tener una lambda func por que implica un poco mas de complejidad
def add_taxes(item): # recibimos uno de los diccionarios de items
  item['taxes'] = item['price'] * .19
  return item
  

new_items = list(map(add_taxes, items)) # ejecutamos la funcion add_taxes "sin el ()" y usamos items que es la lista que se esta iterando.
print(new_items)
# OJO, si queremos imprimir la lista de items original nosotros podriamos pensar que nos la dara sin las taxes, 
print(items) # [{'product': 'camisa', 'price': 100, 'taxes': 19.0}, {'product': 'pantalones', 'price': 300, 'taxes': 57.0}, {'product': 'tenis', 'price': 200, 'taxes': 38.0}]
# esto tiene que ver con una referencia en memoria

# sollucion de comentarios:

items =[
    {'product': 'shirt',
    'price':120},
    {'product': 'pants',
    'price':160},
    {'product': 'jacket',
    'price':205}
]

new_items = list(map( lambda x: x|{'tax': x['price']*0.19} ,items)) 

print(new_items)   
print(items)