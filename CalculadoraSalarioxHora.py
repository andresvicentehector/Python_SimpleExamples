'''
CALCULADORA DE AHORROS:

 El objetivo es crear un programa con el que puedas calcular
tus salario por hora. El programa deberá calcular cuánto puede ahorrar una persona dado sus
ingresos por hora, sus horas trabajadas y su gasto de vida semanal.

'''


nombre=input('me permitirías saber tu nombre: ').title()
semanas_trabajo_anual=float(input('cuantas semanas trabajas al año (todas son 52): '))

print('Hola '+nombre)

dinero_año=float(input('cuánto dinero ganas al año '))

horas_semana=float(input('cuántas horas trabajas a la semana '))

salario_hora=(dinero_año/semanas_trabajo_anual)/horas_semana


print(nombre,' ,ganas ', salario_hora,'euros la hora')

gastos_semanales=float(input('cuánto dinero gastas a la semana: '))

#calculo el gasto anual
gasto_anual=gastos_semanales*semanas_trabajo_anual


ahorro_anual=dinero_año-gasto_anual

print('tu balance de ahorros anual es de: ', ahorro_anual)