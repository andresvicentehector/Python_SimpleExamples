'''
El objetivo de este ejercicio es que crees un script que dado un nombre de usuario"
le de la bienvenida con su nombre en el formato correcto
'''

msg_wllcome='estas usando '+'python'
print(msg_wllcome)

nombre= input('Cuál es tu nombre: ').title().replace('.','')

msg_total='¡Hola '+ nombre+' '+msg_wllcome+'!'

print('¡Hola ',nombre,msg_wllcome,'!' )


print('string sin más')
print(msg_total )
print('string capitalizado')
print(msg_total.upper() )
print('string en minúsculas')
print(msg_total.lower() )
print('Todo el mensaje como toca')
chars=msg_total.split()


chars[len(chars)-1]=chars[len(chars)-1].capitalize()

new_msg=' '.join(chars)
print(new_msg)

