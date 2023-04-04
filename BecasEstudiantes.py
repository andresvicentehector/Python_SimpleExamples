'''
El gobierno quiere otorgar becas de excelencia a los estudiantes con un mínimo de un 8 de media.

Además para acceder a la beca el estudiante debe tener entre 17 y 21 años. 
Crea un script que pida el nombre, la edad y la nota media del estudiante e indique si puede optar a la beca o no.

'''

nombre=input('Escribe tu nombre: ').title()
edad=int(input('Escribe tu edad:'))
nota_media=float(input('Escribe tu nota media:'))


if(17<edad<21 and nota_media>8.0 ):
  print(nombre,'puede aplicar para la beca')

else:
 print(nombre,'no es apto para la beca')