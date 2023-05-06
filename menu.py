from manejadoralumno import ManejadorAlumno
from manejadormateria import ManejadorMateria
from clasealumno import Alumno
from clasemateria import Materia
class Menu(object):
    __switcher = None
    __lista_datos = []
    __arreAlumno = []
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '0':self.salir
        }
        self.__lista_datos = ManejadorMateria()
        self.__lista_datos.test_lista()
        
        self.__arreAlumno = ManejadorAlumno()
        self.__arreAlumno.test_Cargar1()

    def getSwitcher(self):
        return self.__switcher
    
    def opcion(self, op,numero):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(numero)
    
    def salir(self):
        print ("Terminando ejecucion del programa....")
    
    def opcion1(self, alternativo):
        m= self.__lista_datos.buscar_DNI(alternativo)
        print ("El promedio del alumno es: ", m)   
        
    def opcion2(self, materia, lista):
        self.__arreAlumno.Estudiante(materia,self.__lista_datos)

        
    def opcion3 (self, other):
        self.__arreAlumno.Listado()
        