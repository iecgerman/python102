def Celsius():
  fahrenheit = float(input('what is the Fahrenheit temp? '))
  celcius = (fahrenheit - 32) * 5/9
  rounded_celcius = (round(celcius, 1))
  print(rounded_celcius)

Celsius()