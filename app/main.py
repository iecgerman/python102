import utilidades

keys, values = utilidades.get_population()
print(keys, values)

print(utilidades.saludo)

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

country = input('🏴‍☠️  Escribe el pais del cual quieres su poblacion: ')

resultado = utilidades.population_by_country(data, country)


print(resultado)



# cualquier archivo en python se considera un modulo


