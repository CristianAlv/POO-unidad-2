from Manejador import Manejador
from claseRegistro import Registro
class Menu(object):
    __switcher = None
    __lista_datos = []
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '0':self.salir
        }
        self.__lista_datos = Manejador()
        self.__lista_datos.test_lista()
    def getSwitcher(self):
        return self.__switcher
    
    def opcion(self, op,numero):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(numero)
    
    def salir(self):
        print ("Terminando ejecucion del programa....")
    
    def opcion1(self):
        self.__lista_datos.maximo()
        self.__lista_datos.minimo()
        
    def opcion2(self):
        print ("El promedio es: ", self.__lista_datos.Promedio())
        
    def opcion3 (self, dia):
        self.__lista_datos.mostrarTabla(dia)
        