from calendar import prmonth
from glob import escape
import json

with open('Tabla.json', 'r') as archivo:
    datosLeidos=json.load(archivo)
    #print (datosLeidos)

#Datos tabla FSM

EstAct_Tabla = list(datosLeidos ["Estado_actual"])
Entrada_Tabla = list(datosLeidos ["Entrada"])
EstSig_Tabla = list(datosLeidos ["Estado_siguiente"])
Salida_Tabla = list(datosLeidos ["Salida"])


#Ejemplos de prueba

def ejemplos_prueba(a):
    ejemplos_entrada=        ["0001","0010","0011","0100","0101","0110"]
    ejemplo_estado_actual=   ["1110","1100","1110","1000","1110","1100"]
    ejemplo_estado_siguiente=["1111","1110","1111","1100","1111","1110"]
    ejemplos_salida=         ["1111","1110","1101","1100","1011","1010"]
    salida=[ejemplos_entrada[a],ejemplo_estado_actual[a],ejemplo_estado_siguiente[a],ejemplos_salida[a]]
    return salida

Ej0=ejemplos_prueba(0)
Ej1=ejemplos_prueba(1)
Ej2=ejemplos_prueba(2)
Ej3=ejemplos_prueba(3)
Ej4=ejemplos_prueba(4)

Entrada0=Ej0[0]
Estado_actual0 = Ej0[1]
Estado_siguiente0 = Ej0[2]
Salida0 = Ej0[3]

Entrada1=list(Ej1[0])
Estado_actual1 = list(Ej1[1])
Estado_siguiente1 = list(Ej1[2])
Salida1 = list(Ej1[3])

Entrada2=list(Ej2[0])
Estado_actual2 = list(Ej2[1])
Estado_siguiente2 = list(Ej2[2])
Salida2 = list(Ej2[3])

Entrada3=list(Ej3[0])
Estado_actual3 = list(Ej3[1])
Estado_siguiente3 = list(Ej3[2])
Salida3 = list(Ej3[3])

Entrada4=list(Ej4[0])
Estado_actual4 = list(Ej4[1])
Estado_siguiente4 = list(Ej4[2])
Salida4 = list(Ej4[3])

#'Estado_actual' : [0,0,1,1] , 'Entrada' : [0,1,0,1], 'Salida' : [0,1,1,0] , 'Estado_siguiente' : [0,1,1,1]

#Logica

def recorrer(Estado_actual,Entrada):
        for i in range (4): 
            if Estado_actual[i] == EstAct_Tabla[0]:
                if Entrada[i] == Entrada_Tabla[0]:                   
                    Estado_siguienteComp = EstSig_Tabla[0]
                    SalidaComp = Salida_Tabla [0] 
                    print ("El bit ", i, " de entrada es: ", Entrada [i], " entonces su estado siguiente debe ser: ", Estado_siguienteComp, " y su salida debe ser: ", SalidaComp)
                    if Estado_siguienteComp == Estado_siguiente[i]:
                        if SalidaComp == Salida[i]:
                            print ("---> El bit ",i," es correcto ya que la salida del bit ", i, " es igual a ", SalidaComp ,"\n")
                        if SalidaComp != Salida[i]:
                            print (" ---> El bit ",i," no es correcto ya que la salida del bit ", i, " es diferente a ", SalidaComp,"\n" )                           
                    if Estado_siguienteComp != Estado_siguiente[i]: 
                        print (" ---> El bit ",i," no es correcto ya que el estado siguiente del bit ", i, " es diferente a ", Estado_siguienteComp ,"\n")   
                        
                if Entrada[i] == Entrada_Tabla[1]:
                    Estado_siguienteComp = EstSig_Tabla[1]
                    SalidaComp = Salida_Tabla [1]
                    print ("El bit ", i, " de entrada es: ", Entrada [i], " entonces su estado siguiente debe ser: ", Estado_siguienteComp, " y su salida debe ser: ", SalidaComp)
                    if Estado_siguienteComp == Estado_siguiente[i]:
                        if SalidaComp == Salida[i]:
                            print (" ---> El bit ",i," es correcto ya que la salida del bit ", i, " es igual a ", SalidaComp,"\n" )
                        if SalidaComp != Salida[i]:
                            print (" ---> El bit ",i," no es correcto ya que la salida del bit ", i, " es diferente a ", SalidaComp,"\n" ) 

                    if Estado_siguienteComp != Estado_siguiente[i]:
                        print (" ---> El bit ",i," no es correcto ya que el estado siguiente del bit ", i, " es diferente a ", Estado_siguienteComp,"\n" )

            if Estado_actual[i] == EstAct_Tabla[2]:
                if Entrada[i] == Entrada_Tabla[2]:
                    Estado_siguienteComp = EstSig_Tabla[2]
                    SalidaComp = Salida_Tabla [2]
                    print ("El bit ", i, " de entrada es: ", Entrada [i], " entonces su estado siguiente debe ser: ", Estado_siguienteComp, " y su salida debe ser: ", SalidaComp)
                    if Estado_siguienteComp == Estado_siguiente[i]:
                        if SalidaComp == Salida[i]:
                            print (" ---> El bit ",i," es correcto ya que la salida del bit ", i, " es igual a ", SalidaComp,"\n" )
                        if SalidaComp != Salida[i]:
                            print (" ---> El bit ",i," no es correcto ya que la salida del bit ", i, " es diferente a ", SalidaComp ,"\n")

                    if Estado_siguienteComp != Estado_siguiente[i]:
                       print (" ---> El bit ",i," no es correcto ya que el estado siguiente del bit ", i, " es diferente a ", Estado_siguienteComp ,"\n")

                if Entrada[i] == Entrada_Tabla[3]:
                    Estado_siguienteComp = EstSig_Tabla[3]
                    SalidaComp = Salida_Tabla [3] 
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


lec = int(input("""Para la maquina de estados de complemento a dos, que ejmplo desea comprobar:

1. Ejemplo1
2. Ejemplo2
3. Ejemplo3
4. Ejemplo4
5. Ejemplo5 


Escriba el numero que desee (1/2/3/4/5): """))

if lec == 1:

    Estado_actualNorm0 = list(Estado_actual0)
    EntradaNorm0 = list(Entrada0)
    Estado_siguienteNorm0 = list(Estado_siguiente0)
    SalidaNorm0 = list(Salida0)

    Estado_actual = Estado_actualNorm0 [::-1]
    Entrada = EntradaNorm0 [::-1]
    Estado_siguiente = Estado_siguienteNorm0 [::-1]
    Salida = SalidaNorm0 [::-1]


    print("\n")
    print ("Su codigo de entrada ingresado es: --->", EntradaNorm0 )
    print ("Su codigo de salida ingresado es: --->", SalidaNorm0 ,"\n")
    
    recorrer(Estado_actual,Entrada)

    print ("\n")
    

if lec == 2:
    Estado_actualNorm1 = Estado_actual1
    EntradaNorm1 = Entrada1
    Estado_siguienteNorm1 = Estado_siguiente1
    SalidaNorm1 = Salida1

    Estado_actual = Estado_actualNorm1 [::-1]
    Entrada = EntradaNorm1 [::-1]
    Estado_siguiente = Estado_siguienteNorm1 [::-1]
    Salida = SalidaNorm1 [::-1]

    print("\n")
    print ("Su codigo de entrada ingresado es: --->", EntradaNorm1 )
    print ("Su codigo de salida ingresado es: --->", SalidaNorm1 ,"\n")
    recorrer(Estado_actual,Entrada)
    print ("\n")   

if lec == 3:
    Estado_actualNorm2 = Estado_actual2
    EntradaNorm2 = Entrada2
    Estado_siguienteNorm2 = Estado_siguiente2
    SalidaNorm2 = Salida2

    Estado_actual = Estado_actualNorm2 [::-1]
    Entrada = EntradaNorm2 [::-1]
    Estado_siguiente = Estado_siguienteNorm2 [::-1]
    Salida = SalidaNorm2 [::-1]

    print("\n")
    print ("Su codigo de entrada ingresado es: --->", EntradaNorm2 )
    print ("Su codigo de salida ingresado es: --->", SalidaNorm2 ,"\n")
    recorrer(Estado_actual,Entrada)
    print ("\n")

if lec == 4:
    Estado_actualNorm3 = Estado_actual3
    EntradaNorm3 = Entrada3
    Estado_siguienteNorm3 = Estado_siguiente3
    SalidaNorm3 = Salida3

    Estado_actual = Estado_actualNorm3 [::-1]
    Entrada = EntradaNorm3 [::-1]
    Estado_siguiente = Estado_siguienteNorm3 [::-1]
    Salida = SalidaNorm3 [::-1]

    print("\n")
    print ("Su codigo de entrada ingresado es: --->", EntradaNorm3 )
    print ("Su codigo de salida ingresado es: --->", SalidaNorm3 ,"\n")
    recorrer(Estado_actual,Entrada)
    print ("\n")

if lec == 5:
    Estado_actualNorm4 = Estado_actual4
    EntradaNorm4 = Entrada4
    Estado_siguienteNorm4 = Estado_siguiente4
    SalidaNorm4 = Salida4

    Estado_actual = Estado_actualNorm4 [::-1]
    Entrada = EntradaNorm4 [::-1]
    Estado_siguiente = Estado_siguienteNorm4 [::-1]
    Salida = SalidaNorm4 [::-1]

    print("\n")
    print ("Su codigo de entrada ingresado es: --->", EntradaNorm4 )
    print ("Su codigo de salida ingresado es: --->", SalidaNorm4 ,"\n")
    recorrer(Estado_actual,Entrada)
    print ("\n")