import json


with open('Datos.json') as archivo:
    datosLeidos=json.load(archivo)

print (datosLeidos)

#Programa para probar la FSM diseñada

Codigo1 = []

estado_actuali = 0

entradai = 0

def complemento_a_dos (entrada, estado_actual):
    pass

lec = int(input("""Ingrese que maquina de estados desea comprobar:

1. FSM Complemento a dos
2. FSM Suma binarios
3. FSM Multiplicador por tres

Escriba el numero que desee (1/2/3): """))


if lec == 1:
    if estado_actuali == 0:
        if entradai == 0:
            estado_sigi = 0
            salida = 0 
        if entradai == 1:
            estado_sigi = 1
            salida = 1
    if estado_actuali == 1:
        if entradai == 0:
            estado_sigi = 1
            salida = 1
        if entradai == 1:
            estado_sigi = 1
            salida = 0

            

if lec == 2:
    pass

if lec == 3:
    pass