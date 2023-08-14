import csv

def read_csv(path):
  with open(path, 'r') as csvfile:    
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    dataPcymac = [] # agregamos dataPcymac en array vacio
    for row in reader:
      iterable = zip(header, row)
      producto_dict = {key: value for key, value in iterable}
      dataPcymac.append(producto_dict)
    return dataPcymac
         
if __name__ == '__main__':
  dataPcymac = read_csv('./proyecto/dataPcymac.csv')
  #print(dataPcymac)

# {'ProductoID': 'TEWNACNA-0938', 'ProductoNombre': 'TECLADO GAMER ONE HAND NACEB ALAMBRICO ATHERIS RETROILUMINADO RGB', 'ProductoPrecio': '445', 'ProductoStock': '1', 'UnidaMedidaID': 'Pza', 'ProductoStatus': 'VERDADERO'}, {'ProductoID': 'TEWNACNA-0944', 'ProductoNombre': 'TECLADO GAMER NACEB ALAMBRICO BLACK COBRA RGB MECANICO BSUN ROJO ANTI-GHOSTING REPOSAMUnECAS DESMONTABLE', 'ProductoPrecio': '836', 'ProductoStock': '3', 'UnidaMedidaID': 'Pza', 'ProductoStatus': 'VERDADERO'}]

# Ahora si tenemos un array que esta formado por diccionarios

#print(dataPcymac[53])

# Por ejemplo este sería el producto numero 54 (recordemos que empezamos en el indice 0)

# {'ProductoID': 'ACDCM074N', 'ProductoNombre': 'MOUSEPAD BROBOTIX TIPO GEL NEGRO', 'ProductoPrecio': '105', 'ProductoStock': '12', 'UnidaMedidaID': 'Pza', 'ProductoStatus': 'VERDADERO'}

