#Programa Maquina de estados finitos JSON
#Contiene la tabla de funcionamiento en JSON 
import json

TabComp2 = {'Estado_actual' : ['0','0','1','1'] , 'Entrada' : ['0','1','0','1'], 'Salida' : ['0','1','1','0'] , 'Estado_siguiente' : ['0','1','1','1']} 

with open('Tabla.json', 'w') as f:  # W es para escritura y f es la variable de manejo
    json.dump(TabComp2, f)

