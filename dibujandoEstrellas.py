'''. Escribe un programa que pida al usuario un número entero y muestre por pantalla una
estructura como la de más abajo, donde el valor de entrada es el número de estrellas en el
centro de la estructura.
*
**
***
****
*****
****
***
**
*'''

n=int(input('Dame un número:'))

for i in range(1, 2*n):
        if(i<=(2*n)/2):
            print('*'*i)
for i in range(2*n+1, 0,-1):
        if(i<(2*n)/2):
            print('*'*i)
