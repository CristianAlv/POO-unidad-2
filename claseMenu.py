

from classViajero import ManejadorViajero
from classViajeroFrecuente import ViajeroFrecuente
class Menu(object):
    __switcher = None
    __lista_datos = []
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '0':self.salir
        }
        self.__lista_datos = ManejadorViajero()
        self.__lista_datos.testlista()
    def getSwitcher(self):
        return self.__switcher
    
    def opcion(self, op,numero):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(numero)
    
    def salir(self):
        print ("Terminando ejecucion del programa....")
    
    def opcion1(self, numero):
        print("ingresó opcion 1")
        self.__lista_datos.consultarMillas(numero)
        
    def opcion2(self, numero):
        m= int(input("Ingrese la cantidad de millas a acumular: "))
        self.__lista_datos.acumularM(numero, m)
            
    def opcion3 (self, numero):
        c= int(input("Ingrese la cantidad de millas a canjear: "))
        self.__lista_datos.canjearM(numero, c)
