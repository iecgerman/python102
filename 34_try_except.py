def dividir(a,b):
  try:
    operacion = a / b
  except ZeroDivisionError:
    operacion = "No se puede dividir entre 0"
  return operacion  

respuesta = dividir(10,2)
print(respuesta) # 5.0

respuesta = dividir(10,0) # No se puede dividir entre 0
print(respuesta)