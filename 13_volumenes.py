import math
def area_polygon(sides, length):
  alpha = 360 / (2 * sides)
  betha = (alpha* math.pi)/180 #pasar los grados a radianes
  tan_betha = math.tan(betha)
  apotema = length / (2 * tan_betha)
  perimeter = sides * length
  area = perimeter * apotema / 2  
  return area
  
def volume_prism(sides, length, heith):
  area = area_polygon(sides, length)
  my_volume = area * heith
  return round(my_volume, 2)

def volume_sphere(radius):
  return radius ** 3
  
def volume_pyramid(sides, length, heith):
  volume_p = volume_prism(sides, length, heith)
  my_volume = volume_p / 3
  return round(my_volume, 2)
  
def volume_cube(length, depth, heigth):
  my_volume = length * depth * heigth
  return round(my_volume, 2)
  
  
menu_01 = '''
Welcome to the Volume Calculator
Choose an option:
1 - Cube
2 - Sphere
3 - Prism
4 - Pyramid
__'''

option_01 = input(menu_01)

if option_01 == '1': 
  figure = 'Cube'
  side = int(input('Side length: '))
  my_volume = volume_cube(side)

elif option_01 == '2':
  figure = 'Sphere'
  radius = int(input('Radius length: '))
  my_volume = volume_sphere(radius)

elif option_01 == '3':
  figure = 'Prism'
  sides = int(input('Number of sides of your base: '))
  length = float(input("Side's length: "))
  heith = float(input('Heith: '))
  my_volume = volume_prism(sides, length, heith)
elif option_01 == '4':
  figure = 'Pyramid'
  sides = int(input('Number of sides of your base: '))
  length = float(input("Side's length: "))
  heith = float(input('Heith: '))
  my_volume = volume_pyramid(sides, length, heith)
   
    
print(f'The volume of your {figure} is {my_volume}') 