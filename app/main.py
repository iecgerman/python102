import utilidades
import read_csv
import charts

#no ocuparemos esta data para la clase 40
"""data = [
  {
    'Country': 'Colombia',
    'Population': 500
  },
  {
    'Country': 'Bolivia',
    'Population': 300
  }  
]"""

def run():
  data =read_csv.read_csv('./app/data.csv')
  country = input('🏴‍☠️  Escribe el pais del cual quieres su poblacion: ')

  resultado = utilidades.population_by_country(data, country)

  if len(resultado) > 0:
    country = resultado[0]
    labels, values = utilidades.get_population(country)
    charts.generate_bar_chart(labels, values)
  
  #print(utilidades.saludo)
  
  print(resultado)

if __name__ == '__main__': # con esto ya podemos tener dualidad para poder ejecutar run desde app/mainpy como un script
  run()
  
  
  
# cualquier archivo en python se considera un modulo


