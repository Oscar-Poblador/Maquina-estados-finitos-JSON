#  Grupo de Trabajo:
#  Programación aplicada
#  Manuel Alejandro Guio Cardona - 20211005061
#  Oscar David Poblador Parra    - 20211005116
#  Juan David Bello Rodriguez    - 20211005028

#Estados [V1, V2, V3, Calentar, Start]
Estadosini = [0,0,0,0,0] #Estatico
Estados1 = [1,0,0,0,0] # T1 Llena
Estados2 = [0,0,0,1,1] # Calienta y tiempo 
Estados4_calenNO = [0,1,0,0,0] # T2 llena 
Estados4_calenSI = [0,0,1,0,0] # T3 desocupa

#Transiciones [Vacio,nivel1,nivel2,Temp,tiempo]

Transini=[1,0,0,0,0] # Vacio 
Trans1 = [0,1,0,0,0] # Nivel 1
Trans1_NO = [0,1,0,0,1] # Nivel 1 no caliente
Trans2 = [0,1,1,0,1] # Llena hasta nivel 2 
Trans1_Si = [0,1,0,1,1] # Nivel 1 caliente 

#Función de estado siguiente
def sistema_Trans (estado,transicion): 
  if estado == Estadosini:  #[0,0,0,0,0] Full vacio
    transicion = Transini #[1,0,0,0,0] ,Tanq vacio
    print("El tanque esta vacio")
    print("El siguiente paso es abrir la valvula 1\n")
  elif estado == Estados1: # [1,0,0,0,0] Abre val1 
    print("Abriendo V1")
    transicion = Trans1 # [0,1,0,0,0] Llega a nivel1
    print ("El tanque llega a nivel 1")
    print("El siguiente paso es calentar y contabilizar\n")
  elif estado == Estados2: # [0,0,0,1,1] Calienta y cuenta
    print ("\nComienza a calentar y el tiempo comienza a contar\n")
    
    aux = input("¿El tanque calentó? si/no: ")

    if aux == "si":
      transicion = [0,1,0,1,1]
    elif aux == "no": 
      transicion =  [0,1,0,0,1]
    
    if transicion == Trans1_Si: # [0,1,0,1,1] calento y en 20 min llega a 80°
      print("\nEl tanque llegó a los 80°, procede a desocupar abriendo V3")
      estado = Estados4_calenSI # [0,0,1,0,0] Desocupa 
      print ("El tanque se desocupó ya que superó los 80°")
    elif transicion == Trans1_NO: # [0,1,0,0,1] En 20 min no llega a 80°
      print("El tanque no llegó a los 80°, procede a llenar abriendo V2")
      estado ==Estados4_calenNO # [0,1,0,0,0] Llena con T2 abriendo V2
      print ("Estado intermedio, se llena el tanque hasta nivel 2")
      transicion = Trans2 # Cumplio con tiempo y llena a nivel 2
      print ("El tanque lleno hasta nivel 2")
      estado = Estados4_calenSI # [0,0,1,0,0] Desocupa 
      print ("El tanque se desocupó")

  return transicion, estado

transicion=[0,0,0,0,0]
#Prcesos de lectura de entrada
entradas_Estado=[[0,0,0,0,0],[1,0,0,0,0],[0,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[0,0,0,1,1],[0,0,0,0,0]]

#Lectura y comparación de cada entrada
for estado in entradas_Estado:
  if estado==[0,0,0,0,0]:
    print("\n//////////////////////////////////\n")
  transicion,estado = sistema_Trans(estado,transicion)
  print('\nEl estado actual es:',estado, " y empieza a realizarse (transicion): ",transicion,"\n")
  