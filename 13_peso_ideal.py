def peso_ideal(peso=0, estatura=0, sexo=0):
  peso = int(input('Ingresa tu peso che marro => '))
  estatura = int(input('Ingresa tu estatura en cms che enano => '))
  sexo = str(input('Cual es tu sexo M/F => '))
  sexo = sexo.upper()

  if (sexo == 'M'):
    resultado = estatura**2*23 / 10000
  
    print(resultado, 'Kilos es tu peso ideal')
    print('La diferencia con tu peso actual es ', round(peso-resultado, 2), 'kilos')
  if (sexo == 'F'):
    resultado = estatura**2 * 21.5 / 10000
  
    print(resultado, 'Kilos es tu peso ideal')
    print('La diferencia con tu peso actual es ', round(peso-resultado, 2), 'kilos')
  
  return resultado
  
  print(peso_ideal)
  
peso_alcanzar = peso_ideal()
print(peso_alcanzar, 'hola')