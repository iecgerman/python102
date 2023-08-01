import utilidades

data = [
  {
    'Country': 'Colombia',
    'Population': 500
  },
  {
    'Country': 'Bolivia',
    'Population': 300
  }  
]

def run():
  keys, values = utilidades.get_population()
  print(keys, values)
  
  #print(utilidades.saludo)
  

  
  country = input('🏴‍☠️  Escribe el pais del cual quieres su poblacion: ')
  
  resultado = utilidades.population_by_country(data, country)
  
  
  print(resultado)

if __name__ == '__main__': # con esto ya podemos tener dualidad para poder ejecutar run desde app/mainpy como un script
  run()
  
  
  
  # cualquier archivo en python se considera un modulo


