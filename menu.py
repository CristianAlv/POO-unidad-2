from classConjunto import Conjunto

class Menu(object):
    __switcher = None
    __A = []
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '0':self.salir
        }
        self.__A = Conjunto()
    def getSwitcher(self):
        return self.__switcher
    
    def opcion(self, op, conj, otroConj):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(conj, otroConj)
    
    def salir(self):
        print ("Terminando ejecucion del programa....")
    
    def opcion1(self,A, B):
        print ("Ingreso la opcion 1")
        suma = A + B
        print ("El resultado de la suma es: ", format(suma))
        
    def opcion2(self,A,B):
        print ("Ingreso la opcion ")
        resta=A-B
        print ("El resultado de la resta es: ", format(resta))
        
    def opcion3 (self, A, B):
        print ("Ingreso la opcion 3 ")
        comparacion= A == B
        comparacion = A if A == B else False
        if (comparacion == False):
            print ("Los conjuntos no son iguales")
        else:
            print ("Los conjuntos son iguales")
        
    
        