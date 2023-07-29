
def suma_de_rangos(menor, mayor):
  print('suma todos los numeros del ', menor, mayor)
  suma = 0
  for i in range(menor, mayor):
    suma += i
  return suma

resultado = suma_de_rangos(1, 3) # suma del 0 a la posicion 2 [0,1,2]= 0,1,2
print(resultado)
resultado_2 = suma_de_rangos(resultado, resultado + 3)
print(resultado_2)