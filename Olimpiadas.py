'''  En la competición de skeleton de las olimpiadas de invierno hay tres finalistas. El cronómetro mide
los siguientes tiempos:

Hannah Neise: 8 minutos 3 segundos y 10 centésimas
Jackie Narracott: 12 minutos 7 segundos y 8 centésimas
Kimberley Bos: 9 minutos 14 segundos y 3 centésimas

1. Crea un script que pida los tiempos por pantalla para cada uno de los finalistas
2. Convierte los tiempos de minutos-segundos-centésimas a segundos
3. Sabiendo que la pista es de 100 metros calcula la velocidad media de cada uno de ellos en
metros por segundo.
4. Imprime los resultados por pantalla

'''

nombre=[]
tiempoMin=[]
tiempoSec=[]
tiempoMili=[]
tiempoSecsTotal=[]
VelocidadMedia=[]

print('Olimpiadas de invierno de Skeleton')

for i in range(3):
 nombre.append(input('Introduce el nombre de la finalista: '))
 print('Introduce el tiempo:')
 tiempoMin.append(float(input('Minutos: ')))
 tiempoSec.append(float(input('Segundos: ')))
 tiempoMili.append(float(input('Milisegundos: ')))
 tiempoSecsTotal.append(tiempoMin[i]*60+tiempoSec[i]+tiempoMili[i]/60)
 VelocidadMedia.append(100/tiempoSecsTotal[i])


 

for i in range(0,3):
    print('El tiempo de', nombre[i], 'ha sido: ',"{:.2f}".format(tiempoSecsTotal[i]),'segundos.','Con una velocidad media de: ','{:.2f}'.format(VelocidadMedia[i]),' Metros por segundo')