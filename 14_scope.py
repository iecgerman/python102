"""Creo que esto te puede ayudar a entender mejor: Dentro de una función puede haber variables, las cuales se llaman variables locales. Estas variables locales, se identifican porque están escritas dentro de la definición de la función; y únicamente funcionan mientras que la función sea llamada o utilizada. Si vas a llamar a una variable local por fuera de la función, no servirá.
Y existen variables globales, que son las que están escritas fuera de una función. Estas variables si funcionan al ser llamadas sin la función, porque no están determinadas dentro de la función."""

precio = 100 # variable global

def incrementar():
  precio = 200
  resultado = precio + 10
  print(resultado) # variable local (local scope)
  return resultado # la variable resultado solo tiene un contexto dentro de nuestra funcion
  
print(precio) # imprime la variable global

precio_2 = incrementar()
print(precio_2)

#print(resultado) # aqui marcaria un error porque resultado es una variable que se encuentra dentra de la funcion incrementar()

"""Exactamente. Creo que las palabras usadas no son las adecuadas y se presta para confusiones. De manera simple se entiende que las variables se pueden definir como globales, es decir, fuera de las funciones y locales, es decir, que solo son creadas dentro de esa función especifica y si es llamada fuera de ese bloque de codigo (me refiero a la variable local), pues no dara resultado porque simplemente no existe."""

