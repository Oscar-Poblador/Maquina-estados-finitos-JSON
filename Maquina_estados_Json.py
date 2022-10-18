#Programa Maquina de estados finitos JSON
import json

<<<<<<< HEAD
Datos = [ {'Estado_actual' : ['0','0','1','1'] }, {'Entrada' : ['0','1','0','1']}, {'Salida' : ['0','1','1','0'] }, {'Estado_siguiente' : ['0','1','1','1']} ] 

with open('Datos.json', 'w') as f:  # W es para escritura y f es la variable de manejo
    json.dump(Datos, f)

def ejemplos_prueba(a):
    ejemplos_entrada=        ["0001","0010","0011","0100","0101","0110"]
    ejemplo_estado_actual=   ["1110","1100","1110","1000","1110","1100"]
    ejemplo_estado_siguiente=["1111","1110","1111","1100","1111","1110"]
    ejemplos_salida=         ["1111","1110","1101","1100","1011","1010"]
    salida=[ejemplos_entrada[a],ejemplo_estado_actual[a],ejemplo_estado_siguiente[a],ejemplos_salida[a]]
    return salida
 


Ej=ejemplos_prueba(0)
print(Ej)

Entrada=list(Ej[0])
print(Entrada)

#with open('libreria.json', 'r') as archivo:
    #libreria_leida=json.load(archivo)
#Programa para probar la FSM diseñada

#Codigo1 = []

#lec = int(input("""Ingrese que maquina de estados desea comprobar:
#1. FSM Complemento a dos
#2. FSM Suma binarios
#3. FSM Multiplicador por tres
#Escriba el numero que desee (1/2/3): """))

#if lec == 1:
    
 #   i = int(input ("Ingrese el numero de bits del codigo: "))
    
  #  for x in range (i):
   #     cod1 = int(input("Ingrese el bit numero "))
    #    Codigo1.append(cod1)
        
#print (Codigo1)
#for j in range (5):


b="x"
print(b)


#print(entradas[j])
=======
TabComp2 = {'Estado_actual' : ['0','0','1','1'] , 'Entrada' : ['0','1','0','1'], 'Salida' : ['0','1','1','0'] , 'Estado_siguiente' : ['0','1','1','1']} 

with open('Tabla.json', 'w') as f:  # W es para escritura y f es la variable de manejo
    json.dump(TabComp2, f)

>>>>>>> origin/ManuelGuio09061
