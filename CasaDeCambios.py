'''Una casa de cambios necesita construir un programa que dada una cantidad de euros introducida
por el usuario de el resultante en dólares.
1. Crea un script que reciba una cantidad de euros del usuario e imprima por pantalla el
correspondiente en dólares (considera una tasa de cambio donde 1 EU = 1.2 $)

2. La casa de cambios se queda un 10% en concepto de tasas de gestión. Calcula el monto
recibido, el cambio en dólares, la cantidad que se queda la casa de cambios y la cantidad de
dólares restante que recibirá el usuario. Imprime el desglose por pantalla formateado de tal
forma que quede claro para el usuario.
 '''




print('Bienvenide a la casa de cambios de Python:')

amount=float(input('Introduce la cantidad en Euros que quieres cambiar:'))


fee=amount*0.1

conversion=(amount-fee)*1.2

print('Su cambio asciende a un total de:', '{:.2f}'.format(conversion),' despues de aplicar nuestra comisión del ',fee,'Euros')