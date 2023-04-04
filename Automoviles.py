''' Una compañía de automóviles vende tres tipos de coche: RBM Serie 1, RMB Serie plus, RBM
todoterreno. Cada uno de estos coches tiene un precio de venta y el vendedor recibe una
comisión diferente por cada tipo de coche que ha vendido.
Suponga que los precios y las comisiones son:
RBM Serie 1:
precio: 20.000 EU, comisión: 3%
RMB Serie plus:
precio: 35.000 EU, comisión: 5%
RBM todoterreno:
precio: 60.000 EU, comisión: 7%
Crea un programa donde el usuario introduzca el numero de coches vendidos de cada tipo ese
mes y que le devuelva la cantidad en euros a comisionar ese mes.'''

msg_bienvenida="¿Bienvenido, Cuántos coches has vendido este mes?"
print(msg_bienvenida)

serie1=float(input('De la gama RBM Serie 1: '))
seriePlus=float(input('De la gama RBM Serie plus: '))
todoTerreno=float(input('De la gama RBM todoterreno: '))

comision= serie1*20000*0.03+seriePlus*35000*0.05+todoTerreno*0.07*60000

print(' la cantidad que te corresponde es de: ',"{:.2f}".format(comision),'Euros')