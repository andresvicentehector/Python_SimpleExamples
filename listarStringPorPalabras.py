'''Crea un script que pida al usuario una palabra y luego muestre por pantalla una a una las letras
de la palabra introducida empezando por la última. 
'''

palabra=input('introduce una palabra: ')
lista=[]
for letra in palabra:
    lista.append(letra)
   
print(lista)

