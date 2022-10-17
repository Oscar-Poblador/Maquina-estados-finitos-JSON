import json

with open('libreria.json', 'r') as archivo:
    libreria_leida=json.load(archivo)
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