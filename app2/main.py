import csv

def read_csv(path):
   total = 0
   with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')      
      
      for row in reader:
         total += int(row[2]) #le puse otra columna de numeros
   return total

# si no pongo el if no lo puedo ejecutar desde la terminal
if __name__ == '__main__':
  response = read_csv('./app2/data.csv')
  
  print(response)