import csv

def read_csv(path):
  with open(path, 'r') as csvfile:    
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)    
    for row in reader:
      iterable = zip(header, row)
      producto_dict = {key: value for key, value in iterable}
      print(producto_dict)
      # con list comprehention lo convertimos de tuplas a dic comprehention
      # {'ProductoID': 'TEWNACNA-0944', 'ProductoNombre': 'TECLADO GAMER NACEB ALAMBRICO BLACK COBRA RGB MECANICO BSUN ROJO ANTI-GHOSTING REPOSAMUnECAS DESMONTABLE', 'ProductoPrecio': '836', 'ProductoStock': '3', 'UnidaMedidaID': 'Pza', 'ProductoStatus': 'VERDADERO'}
   
if __name__ == '__main__':
  read_csv('./proyecto/dataPcymac.csv')
