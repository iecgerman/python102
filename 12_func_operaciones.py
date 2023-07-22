def operaciones(a,b):
  multiplica = (a*b)
  suma = (a+b)
  resta = (a-b)
  divide = (a/b)
  
  print ("multiplicados ", multiplica)
  print ("sumandos ",suma)
  print ("restados ", resta)
  print ("divididos", divide)

if __name__=="__main__":
  
  variable_1 = int(input("ingresa un numeros enteros: "))
  variable_2 = int(input("ingresa otro numero entero: "))
  
  operaciones(variable_1, variable_2)