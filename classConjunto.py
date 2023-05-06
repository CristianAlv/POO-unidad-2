class Conjunto(object):
    __A = []
    
    def __init__(self):
        self.__A = []
        
    def buscarValor (self, unvalor):
        valor = 0
        i = 0
        while i < (len(self.__A)):
            if (unvalor == self.__A[i]):
                valor = -1
            i += 1
        return valor
    
    def cargarConjunto (self):
        valor = int(input("Ingrese un valor entero(Distinto de -1 (finalizar ingreso) y de los ingresados anteoriormente): "))
        while (valor != -1):
            validar = self.buscarValor (valor)
            if (validar != -1):
                self.__A.append(valor)
            else:
                if (validar == -1):
                    print("Elemento del conjunto repetido")

            valor = int(input("Ingrese un valor entero(Distinto de -1 (finalizar ingreso) y de los ingresados anteoriormente): "))
    def getlongitud(self):
        return len(self.__A)
    
    def getvalor(self, indice):
        return self.__A[indice]
        
    def mostrarConjunto (self):
        for i in range (len(self.__A)):
            print("Elemento nº ", i+1, "" .center(50, "="))
            print("Valor del elemento: {}".format(self.__A[i]))
            
    def buscarlemento (self, elemento, otroConj):
        band = False
        i = 0
        while i < (otroConj.getlongitud()) and band == False:
            if (elemento == otroConj.getvalor(i)):
                band = True
            i += 1
        return band
            
    def __add__(self, otroConj):
        if type(self) == type(otroConj):
            suma = Conjunto()
            longitud = otroConj.getlongitud()
            longitudL = self.getlongitud()
            for j in range (longitudL):
                suma.__A.append(self.__A[j])
                
            for i in range (longitud):
                if (self.buscarlemento(otroConj.getvalor(i), suma) == False):
                    suma.__A.append(otroConj.getvalor(i))
                    
        return suma.__A
    
    def __sub__(self, otroConj):
        band = False
        if type(self) == type(otroConj):
            resta = Conjunto()
            longitud = otroConj.getlongitud()
            longitudL = self.getlongitud()
            for i in range (longitudL):
                    for j in range (longitud):
                        band = self.buscarlemento(self.__A[i], otroConj)
                        if (band == False):
                            if (self.buscarlemento(self.__A[i], resta) == False):
                                resta.__A.append(self.__A[i])
                    
        return resta.__A
    

    
    
    def __eq__(self, otroConj):
            band = False
            cont = 0
            if type(self) == type(otroConj):
                Igual = Conjunto()
                longitud = otroConj.getlongitud()
                longitudL = self.getlongitud()
                if (longitud == longitudL):
                    band = True
                    for i in otroConj:
                            if (i is not self.__A):
                                band = False
                else:
                    band = False  
                    
            return band