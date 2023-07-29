def message_creator(text):
   if text == 'computadora':
      return 'Con mi computadora puedo programar usando Python'
   elif text == 'celular':
      return 'En mi celular puedo aprender usando la app de Platzi'
   elif text == 'cable':
      return '¡Hay un cable en mi bota!'
   else:
      return 'Artículo no encontrado'

text = 'computadora'
response = message_creator(text)
print(response)

# ME GUSTO MUCHO ESTA SOLUCION:

def DescripcionProducto(IDProducto):

   DBProductos = {
     '01computadora' : "Computadora Çore i9 con 32GB Ram ",
     '02celular' : "Celular Samsung S22",
     '03cable' : "Cable de red RJ-45 categoria 6"
   }

   if IDProducto in DBProductos.keys(): 
      return DBProductos[IDProducto]
   else: 
      return 'Artículo no encontrado'

IDProducto = '02celular'
respuesta = DescripcionProducto(IDProducto)
print(respuesta)