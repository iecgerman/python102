import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    print(header) 
    
    for row in reader:
      iterable = zip(header, row)
      print(list(iterable))
   
if __name__ == '__main__':
  read_csv('./proyecto/dataPcymac.csv')

# [('ProductoID', 'TEWNACNA-0944'), ('ProductoNombre', 'TECLADO GAMER NACEB ALAMBRICO BLACK COBRA RGB MECANICO BSUN ROJO ANTI-GHOSTING REPOSAMUnECAS DESMONTABLE'), ('ProductoPrecio', '836'), ('ProductoStock', '3'), ('UnidaMedidaID', 'Pza'), ('ProductoStatus', 'VERDADERO')]

# nos lo dio en formato tuplas

