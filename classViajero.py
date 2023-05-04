import csv
from classViajeroFrecuente import ViajeroFrecuente
class ManejadorViajero(object):
    __lista_viajeros = []
    def __init__(self):
        self.__lista_viajeros = []       
            
    def agregarlista(self, viajeros):
        self.__lista_viajeros.append(viajeros)
      
    def mostrarLista (self):
        for viajero in (self.__lista_viajeros):
            print("".center(50, '-'),"\n", viajero.mostrarViajero())
            print (hex(id(self.__lista_viajeros)))
        
    def testlista(self):
        file = open('Viajeros.csv')
        reader = csv.reader(file, delimiter=';')
        print ("Archivo leido exitosamente")
        for fila in reader:
            num = int(fila[0])
            dni = int(fila[1])
            nom = fila[2]
            ape = fila[3]
            millas = float(fila[4])
            
            unViajero = ViajeroFrecuente(num,dni, nom, ape, millas)
            self.agregarlista(unViajero)
        
        file.close()
        
    def mostrarViajeros (self):
        for viaj in self.__lista_viajeros:
            print("=".center(30,'='))
            print(viaj.mostrarViajero())
            
    def consultarMillas (self, nroV):
        i = 0
        band = False
        while (i < len(self.__lista_viajeros) and band == False):
            if self.__lista_viajeros[i].getNumeroViajero() == nroV:
                band = True
            else:
                i += 1
        
        print("La cantidad de millas del viajero {}, es", self.__lista_viajeros[i].cantidadTotaldeMillas())
        
        
    def verificarnumero(self, num):
        band = False
        i=0
        while i< len(self.__lista_viajeros): 
            if  self.__lista_viajeros[i].getNumeroViajero() == num:
                band = True
        
            i+=1              
    
        return band
        
    
        
    def acumularM (self, nroV, millas):
        i = 0
        band = False
        while (i < len(self.__lista_viajeros) and band == False):
            if self.__lista_viajeros[i].getNumeroViajero() == nroV:
                band = True
                self.__lista_viajeros[i].acumularMillas (millas)
            else:
                i += 1

        print("La NUEVA cantidad de millas del viajero {}, es ".format(self.__lista_viajeros[i].cantidadTotaldeMillas())) 

    def canjearM (self, nroV, millas):
        i = 0
        band = False
        while (i < len(self.__lista_viajeros) and band == False):
            if self.__lista_viajeros[i].getNumeroViajero() == nroV:
                band = True
                self.__lista_viajeros[i].canjearMillas (millas)
            else:
                i += 1
