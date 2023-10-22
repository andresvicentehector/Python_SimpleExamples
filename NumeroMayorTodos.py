''' EL MAYOR DE CUATRO:
Crea un script que pida al usuario 4 números diferentes y imprima el mayor de los cuatro por
pantalla. '''

numero=[]
for i in range (1,5) :
    escribe='escribe el numero '+str(i)+':'
    numero.append(float(input(escribe)))
# --- Pedir NUMEROS al usuario



# --- Imprimir el mayor de los cuatro numeros
if (numero[0]>numero[1]):
    #numero[0], numero[1] = numero[1], numero[0]
    numero[1]=numero[0]
if (numero[1]>numero[2]):
 # numero[1], numero[2] = numero[2], numero[1]
  numero[2]=numero[1]
if (numero[2]>numero[3]):
     #numero[2], numero[3] = numero[3], numero[2]
     numero[3]=numero[2]
print(" El mayor de los 4 es ",   numero[3])
