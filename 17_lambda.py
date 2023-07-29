# Funciones anonimas (Lambdas)

def incrementar(x):
  return x + 1

incrementar_v2 = lambda x : x + 1
#argumentos : expresion

multiplicar = lambda x, y : x * y

resultado = incrementar(10)
print(resultado)

resultado = incrementar_v2(20)
print(resultado)

resultado = multiplicar(2,2) #4
print(resultado)

print("------------------------------")

nombre_completo = lambda nombre, apellido : f"Mi nombre completo es {nombre.title()} {apellido.title()}"

texto = nombre_completo('German','Garcia')
print(texto)

