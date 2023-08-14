import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
      print('***' * 5)
      print(row)
   
if __name__ == '__main__':
  read_csv('./proyecto/dataPcymac.csv') # aqui la dataPcymac tenía un caracter raro en lugar de la ñ y lo reemplacé por la n y ya no me marco error y me imprimio todo en formato de lista pero lo ocupamos en formato diccionario.