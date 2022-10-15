#Programa Maquina de estados finitos JSON
class FMS_C2:

    ##FMS Suma
    Entradas = [0,1,0,1,1]
    Estados = [0,1]
    salidas = []
    estado_siguiente = []

    def Transiciones(entrada, estado_actual):
        for i in entrada:
            if(entrada[i] == 0):
                if(estado_actual == 0):
                    salida[i]=0
                    estado_siguiente[i]=0
                if(estado_actual == 1):
                    salida[i]=0
                

import json

#Programa para probar la FSM diseñada

Codigo1 = []

lec = int(input("""Ingrese que maquina de estados desea comprobar:

1. FSM Complemento a dos
2. FSM Suma binarios
3. FSM Multiplicador por tres

Escriba el numero que desee (1/2/3): """))

if lec == 1:
    
    i = int(input ("Ingrese el numero de bits del codigo: "))
    
    for x in range (i):
        cod1 = int(input("Ingrese el bit numero "))
        Codigo1.append(cod1)
        
print (Codigo1)