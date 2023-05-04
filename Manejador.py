import csv
from claseRegistro import Registro
class Manejador(object):
    __lista_variables = []
    def __init__(self):
        self.__lista_variables = [[0 for j in range(24)] for i in range(3)]
        
    def test_lista(self):
        archivo = open ('metereologicas.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for fila in reader:
            dia = int(fila[0])
            hora = int(fila[1])
            temp = float(fila[2])
            humedad = float(fila[3])
            presion = float(fila[4])
            instancia = Registro(temp, humedad, presion)
            self.__lista_variables[dia-1][hora]= instancia
        archivo.close()    
        
    def mostrarLista(self):
       for i in range(3):
        for j in range(24):    
                print ("=============================== Dia:", i+1, "=================================")
                print ("\n")
                print("\t Temp:",self.__lista_variables[i][j].getTemp(), "\t Humedad:",self.__lista_variables[i][j].gethumedad(), "\t Presion:",self.__lista_variables[i][j].getpresion())
                print ("\n")
    
    def maximo (self):
        max1 = -1000000000
        maximo_dia = 0
        maximo_hora = 0
        for i in range (3):
            for j in range(24):
                if (max1 < self.__lista_variables[i][j].getTemp()):
                    max1 = self.__lista_variables[i][j].getTemp()
                    maximo_dia = i+1
                    maximo_hora = j
            print("El maximo es {} en el dia {} a la hora {}".format(max1, maximo_dia, maximo_hora))
    
        
    def minimo (self):
        min1 = 999999999
        minimo_dia = 0
        minimo_hora = 0
        for i in range (3):
            for j in range(24):
                if (min1 > self.__lista_variables[i][j].getTemp()):
                    min1 = self.__lista_variables[i][j].getTemp()
                    minimo_dia = i+1
                    minimo_hora = j
            print("El minimo es {} en el dia {} a la hora {}".format(min1, minimo_dia, minimo_hora))
              
    def Promedio (self):
        i=0
        j=0
        for i in range (3):
            for j in range(24):
                
                promedio = self.__lista_variables[i][j].getTemp()/ 24
        return promedio
        
    def mostrarTabla(self, dia):
        j=1
        for i in range(1):
            print ("Hora:","\tTemp:","\tHumedad:", "Presion:") 
            for j in range(24):
                print(j+1,"\t",self.__lista_variables[dia][j].getTemp(),"\t",self.__lista_variables[dia][j].gethumedad(),"\t",self.__lista_variables[dia][j].getpresion())
                print ("\n")     
    
