class FechaHora:
    __dia=0
    __mes=0
    __anio=0

    __hora=0
    __minuto=0
    __segundo=0

    def __init__ (self,dia=1,mes=1,anio=2020,hora=0,minuto=0,segundo=0):

        while mes>12 or mes<0:
            mes=int(input("MES incorrecto. Vuelva a ingresarlo: "))

        while dia>31:
            dia=int(input("DIA incorrecto. Vuelva a ingresarlo: "))

        while hora<0 or hora>23:
            hora=int(input("HORA incorrecta. Vuelva a ingresarlo: "))

        while minuto>59 or minuto<0:
            minuto=int(input("MINUTO incorrecto. Vuelva a ingresarlo: "))

        while segundo>59 or segundo<0:
            segundo=int(input("SEGUNDO incorrecto. Vuelva a ingresarlo: "))

        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

    def Mostrar(self):
        print(" ")
        print("Dia: {}  Mes: {}  Año: {}\nHora: {}  Minuto: {}  Segundo:{}".format(self.__dia,self.__mes,self.__anio,self.__hora,self.__minuto,self.__segundo))
        print(" ")

    def PonerEnHora(self,hora=0,minuto=0,segundo=0):
        self.__hora= hora
        self.__minuto = minuto
        self.__segundo =segundo

    def AdelantarHora(self,h=0,m=0):
        self.__hora+=h
        self.__minuto+=m

        #Validaciones de las fechas ingresadas
        if self.__segundo>60:
            self.__segundo=0
            self.__minuto+=1
        if self.__minuto>60:
            self.__minuto=0
            self.__hora+=1

        #Si la hora llega a 24, la hora se pone en 0 y se incrementa el dia
        if self.__hora>=24:
            self.__hora=h-24
            self.__dia+=1

        #si el año es bisiesto
        if self.__anio%4 == 0:
            #si 
            if self.__anio%100==0:
                if self.__anio%400:
                    if self.__mes==2 and self.__dia>29:
                        self.__dia=1
                        self.__mes+=1
                    else:
                         if self.__mes==2 and self.__dia<29:
                            self.__dia+=1
            else:
                if self.__mes==2 and self.__dia>29:
                    self.__dia=1
                    self.__mes+=1
                else:
                    if self.__mes==2 and self.__dia<29:
                        self.__dia+=1
        #Al no ser bisiesto, se valida los días de los meses
        else:
            if self.__mes == 2 and self.__dia>28:
                self.__dia=1
                self.__mes+=1
            else:
                #cambio de mes
                if (self.__mes == 4 or self.__mes==6 or self.__mes==9 or self.__mes==11) and self.__dia>30:
                    self.__dia=1
                    self.__mes+=1
       
                else:
                    #cambio de mes
                    if self.__mes==1 or self.__mes==3 or self.__mes==5 or self.__mes==7 or self.__mes==8 or self.__mes==10 or self.__mes==12 and self.__dia>31:
                        self.__dia=1
                        self.__mes+=1
                        #El mes Disiembre se produce el cambio de año
                        if self.__mes>12:
                            self.__mes=1
                            self.__anio+=1
