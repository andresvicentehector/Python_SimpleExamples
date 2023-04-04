'''
CALCULADORA DE AHORROS:

 El objetivo es crear un programa con el que puedas calcular
tus ahorros anuales. El programa deberá calcular cuánto puede ahorrar una persona dado sus
ingresos por hora, sus horas trabajadas y su gasto de vida semanal.

'''


nombre=(input('me permitirías saber tu nombre: ')).title()
semanas_trabajo_anual=float(input('cuantas semanas trabajas al año (todas son 52): '))

print('Hola '+nombre)

dinero_hora=float(input('cuánto dinero ganas por hora '))

horas_semana=float(input('cuántas horas trabajas a la semana '))

#calculo el dinero que gana semanal
salario_semanal=dinero_hora*horas_semana
#calculo el dinero que gana al año multiplicando por el num de semanas
salario_anual=salario_semanal*semanas_trabajo_anual


print(nombre,',tienes unas ganancias anuales de: ', salario_anual,'euros')

gastos_semanales=float(input('cuánto dinero gastas a la semana: '))

#calculo el gasto anual
gasto_anual=gastos_semanales*semanas_trabajo_anual


ahorro_anual=salario_anual-gasto_anual

print('tu balance de ahorros anual es de: ', ahorro_anual, 'euros brutos')