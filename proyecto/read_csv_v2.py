import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    print(header) # con esto sacamos el header que son las columbnas y seran nuestras keys
    # ['ProductoID', 'ProductoNombre', 'ProductoPrecio', 'ProductoStock', 'UnidaMedidaID', 'ProductoStatus']
     
if __name__ == '__main__':
  read_csv('./proyecto/dataPcymac.csv')