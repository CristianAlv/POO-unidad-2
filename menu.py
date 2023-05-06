
from clasePlanAhorro import PlanAhorro
from manejadorPA import manejadorPA
class Menu(object):
    __switcher = None
    __lista_datos = []
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '0':self.salir
        }
        self.__lista_datos = manejadorPA()
        self.__lista_datos.testlista()
    def getSwitcher(self):
        return self.__switcher
    
    def opcion(self, op,numero):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(numero)
    
    def salir(self):
        print ("Terminando ejecucion del programa....")
    
    def opcion1(self):
        print("ingresó opcion 1")
        self.__lista_datos.Actualizar_Valor()
        
    def opcion2(self):
        self.__lista_datos.BuscarInferior()
            
    def opcion3 (self):
        self.__lista_datos.Monto_Licitar()
    
    def opcion4 (cls):
        PlanAhorro.Modificarcuota()