def volumen(longitud=1, ancho=1, profundidad=1): # estos serian los parametros por defecto
  
  return 'volumen=', longitud * ancho * profundidad, ancho, '<=ancho' # aqui podemos retornar multiples valores

resultado, volumen, ancho, hola = volumen(ancho=10)

print(resultado)
#print(resultado[0]) # volumen=
print(volumen)
print(ancho)
print(hola)
