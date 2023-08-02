with open('./texto.txt', 'w+') as file: # con esta instruccion lo va a cerrar de forma automatica
  for line in file:
    print(line)
    
  file.write('\nescribir nuevas cosas en este archivo \n') # es solo de lectura

  file.write('otra linea \n')
  file.write('otra linea \n')




"""Veamos algunos de los modos más usados con los que un archivo puede ser abierto en Python:

r -> abre un archivo solo para lectura. El puntero al archivo esta localizado al comienzo del archivo. Este es el modo predeterminado de la función.
rb -> abre un archivo solo para lectura en formato binario. El puntero al archivo esta localizado al comienzo del archivo. Este es el modo predeterminado de la función.
r+ -> abre un archivo para escritura y lectura. El puntero del archivo está localizado al comienzo del archivo.
w -> abre un archivo solo para escritura. Sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura.
wb -> abre un archivo solo para escritura en formato binario. Sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura.
w+ -> abre un archivo para escritura y lectura. Sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura.
a -> abre un archivo para anexo. El puntero del archivo esta al final del archivo si este existe. Es decir, el archivo está en modo anexo. Si el archivo no existe, crea un nuevo archivo para escritura."""

"""Usando ‘\n’
Para escribir una nueva línea por primera vez deberíamos de agregar el ‘\n’ en el principio de la cadena, no en el final ya que si no agregaríamos la cadena al final y después crearíamos el salto de línea

Si este es nuestro archivo de texto:

text.txt
linea1
linea2

Usando ‘\n’ al final
with open("text.txt", "r+) as file:
	file.write(''linea3 \n")
El archivo se vería así
text.txt
linea1
linea2linea3

Pero si ponemos ‘\n’ al principio
with open("text.txt", "r+) as file:
	file.write(''\nlinea3")
Se vería así
text.txt
inea1
linea2
linea3"""