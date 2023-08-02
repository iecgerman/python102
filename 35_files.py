file = open('./texto.txt') # es parecido a cuando en visual studio code buscas una imagen un una carpeta en html

# print(file.read())

"""print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())"""

for line in file: # usando un for no estamos usando mucha memoria porque lo lee linea a linea
  print(line)

file.close() #libera espacio en memoria


with open('./texto.txt') as file: # con esta instruccion lo va a cerrar de forma automatica
  for line in file:
    print(line)
