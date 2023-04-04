'''Crea un script que acepte un string de 5 caracteres y devuelva otro string con todos los caracteres
duplicados. Si el input es ‘sbc56’, el output deberá ser ‘ssbbcc5566’'''

repeticion=[5]
repeticion=input()
final= []


for i in range(5):
    final.append(repeticion[i]+repeticion[i])

final2=final.join("")
print(final2)