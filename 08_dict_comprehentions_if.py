import random

countries = ['col', 'mex', 'bol', 'pe']

population_v2 = { country: random.randint(1,100) for country in countries } # la llave es country y el valor es random.ranint(1,100)

print(population_v2)

# hacer un nuevo dict que la poblacion sea mayor a 20 usando dict comprehention

result = { country: population for (country, population) in population_v2.items() if population > 20 }
print(result)

text = 'Hola, soy Nicolas'
unique = {c: c.upper() for c in text if c in "aeiou" }
print(unique)

print('-----------reto--------------')

text = "Hola a todos, esta es una cadena de texto de prueba."

unique = { c: text.count(c) for c in text if c in 'aeiou' }
print(unique)

print('-----------reto--------------')

frase = 'agua pasa por mi casa cate de mi corazon'
txt = 'Compa ¿Qué le parece esa morra? La que anda bailando sola me gusta pa mí Bella, ella sabe que está buena'

unico = { caracter: caracter.upper() for caracter in frase if caracter in 'aeiou'}
print(unico)

vocales = ['a', 'e', 'i', 'o', 'u']

vowel = {letra : frase.count(letra) for letra in frase if letra in 'aeiou'} 
print(vowel)

contador_vocales = {char : txt.count(char) for char in txt if char in 'aeiou'}
print(contador_vocales)

print('-----------reto--------------')

text =  'Hola, soy programador'
unique = {c: c.upper() for c in text if c in 'aeiou'}
print(unique)

letter_counts = {}
for letter in unique:
    count = text.count(letter)
    letter_counts[letter] = count

for letter, count in letter_counts.items():
    print(f"{letter}: {count}")