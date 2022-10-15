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
                    salida[i]=
                
