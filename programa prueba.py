import json

with open('Datos.json', 'r') as archivo:
    datosLeidos=json.load(archivo)
    #print (datosLeidos)

Estado_actualNorm = list(datosLeidos ["Estado_actual"])
EntradaNorm = list(datosLeidos ["Entrada"])
Estado_siguienteNorm = list(datosLeidos ["Estado_siguiente"])
SalidaNorm = list(datosLeidos ["Salida"])

Estado_actual = Estado_actualNorm [::-1]
Entrada = EntradaNorm [::-1]
Estado_siguiente = Estado_siguienteNorm [::-1]
Salida = SalidaNorm [::-1]

#Logica

def recorrer(Estado_actual,Entrada):
        for i in range (4): 
            if Estado_actual[i] == 0:
                if Entrada[i] == 0:                   
                    Estado_siguienteComp = 0
                    SalidaComp = 0 
                    print ("El bit ", i, " de entrada es: ", Entrada [i], " entonces su estado siguiente debe ser: ", Estado_siguienteComp, " y su salida debe ser: ", SalidaComp)
                    if Estado_siguienteComp == Estado_siguiente[i]:
                        if SalidaComp == Salida[i]:
                            print ("---> El bit ",i," es correcto ya que la salida del bit ", i, " es igual a ", SalidaComp ,"\n")
                        if SalidaComp != Salida[i]:
                            print (" ---> El bit ",i," no es correcto ya que la salida del bit ", i, " es diferente a ", SalidaComp,"\n" )                           
                    if Estado_siguienteComp != Estado_siguiente[i]: 
                        print (" ---> El bit ",i," no es correcto ya que el estado siguiente del bit ", i, " es diferente a ", Estado_siguienteComp ,"\n")   
                        
                if Entrada[i] == 1:
                    Estado_siguienteComp = 1
                    SalidaComp = 1
                    print ("El bit ", i, " de entrada es: ", Entrada [i], " entonces su estado siguiente debe ser: ", Estado_siguienteComp, " y su salida debe ser: ", SalidaComp)
                    if Estado_siguienteComp == Estado_siguiente[i]:
                        if SalidaComp == Salida[i]:
                            print (" ---> El bit ",i," es correcto ya que la salida del bit ", i, " es igual a ", SalidaComp,"\n" )
                        if SalidaComp != Salida[i]:
                            print (" ---> El bit ",i," no es correcto ya que la salida del bit ", i, " es diferente a ", SalidaComp,"\n" ) 

                    if Estado_siguienteComp != Estado_siguiente[i]:
                        print (" ---> El bit ",i," no es correcto ya que el estado siguiente del bit ", i, " es diferente a ", Estado_siguienteComp,"\n" )

            if Estado_actual[i] == 1:
                if Entrada[i] == 0:
                    Estado_siguienteComp = 1
                    SalidaComp = 1
                    print ("El bit ", i, " de entrada es: ", Entrada [i], " entonces su estado siguiente debe ser: ", Estado_siguienteComp, " y su salida debe ser: ", SalidaComp)
                    if Estado_siguienteComp == Estado_siguiente[i]:
                        if SalidaComp == Salida[i]:
                            print (" ---> El bit ",i," es correcto ya que la salida del bit ", i, " es igual a ", SalidaComp,"\n" )
                        if SalidaComp != Salida[i]:
                            print (" ---> El bit ",i," no es correcto ya que la salida del bit ", i, " es diferente a ", SalidaComp ,"\n")

                    if Estado_siguienteComp != Estado_siguiente[i]:
                       print (" ---> El bit ",i," no es correcto ya que el estado siguiente del bit ", i, " es diferente a ", Estado_siguienteComp ,"\n")

                if Entrada[i] == 1:
                    Estado_siguienteComp = 1
                    SalidaComp = 0 
                    print ("El bit ", i, " de entrada es: ", Entrada [i], " entonces su estado siguiente debe ser: ", Estado_siguienteComp, " y su salida debe ser: ", SalidaComp)
                    if Estado_siguienteComp == Estado_siguiente[i]:
                        if SalidaComp == Salida[i]:
                            print (" ---> El bit ",i," es correcto ya que la salida del bit ", i, " es igual a ", SalidaComp,"\n" )
                        if SalidaComp != Salida[i]:
                            print (" ---> El bit ",i," no es correcto ya que la salida del bit ", i, " es diferente a ", SalidaComp,"\n" )
                        
                    if Estado_siguienteComp != Estado_siguiente[i]:
                        print (" ---> El bit ",i," no es correcto ya que el estado siguiente del bit ", i, " es diferente a ", Estado_siguienteComp,"\n" )

#Programa para probar la FSM diseñada

Codigo1 = []


lec = int(input("""Ingrese que maquina de estados desea comprobar:

1. FSM Complemento a dos
2. FSM Suma binarios
3. FSM Multiplicador por tres

Escriba el numero que deses (1/2/3): """))

if lec == 1:
    print("\n")
    print ("Su codigo de entrada ingresado es: --->", EntradaNorm )
    print ("Su codigo de salida ingresado es: --->", SalidaNorm ,"\n")
    recorrer(Estado_actual,Entrada)
    print ("\n")

if lec == 2:
   pass

if lec == 3:
    pass