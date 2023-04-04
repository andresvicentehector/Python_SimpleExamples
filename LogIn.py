'''Crea un script que pida una contraseña al usuario (el script sabe cual es la contraseña correcta).

Si la contraseña es correcta el script debe darle la bienvenida al usuario. De lo contrario debe
indicarle que la contraseña es incorrecta y darle una segunda oportunidad de introducir la
contraseña. Al segundo fallo debe mostrar un mensaje de error y terminar de ejecutarse.

Cambia el script para que no distinga entre mayúsculas y minúsculas.'''

contraseña=input('Teclea la contrañeña:')
contador=0

if(contraseña!='pajarito'):
  print('contraseña incorrecta')  
  contador=1
  contraseña=input('Teclea la contrañeña:')

  if(contraseña=='pajarito'):
        print('bienvenido')
        contador=0
  else:
      contador=2
      print('usuario bloqueado, contacte con administración')
    
elif(contraseña=='pajarito'):
    print('bienvenido')
    contador=0