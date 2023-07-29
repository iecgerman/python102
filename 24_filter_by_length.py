"""📖 Retorna solo palabras de 4 letras y más (Clase#24)"""

def filter_by_length(words):
  
  nueva_lista = list(filter(lambda word: len(word) >= 4, words))
  return nueva_lista

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)