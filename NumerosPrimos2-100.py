'''NUMEROS PRIMOS 1:
Crea un programa que imprima todos los números primos entre el 2 y el 100. Un numero primo es
un numero positivo y entero mayor que uno que no tiene un divisor positivo y entero que no sea 1
o sí mismo.'''
contador=2
lista=[]

while (contador <100):
        es_primo=True
        for i in range(2,contador):
            if contador % i ==0:
                 es_primo=False
                 break
        if es_primo:
                lista.append(contador)  

        contador+=1

print(lista)