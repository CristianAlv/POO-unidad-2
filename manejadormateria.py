from clasemateria import Materia
from manejadoralumno import ManejadorAlumno
from clasealumno import Alumno
import csv
from datetime import datetime
class ManejadorMateria(object):
    __lista_materias = []
    def __init__(self):
        self.__lista_materias = []
        
    def test_lista(self):
        archivo = open ('materiasAprobadas.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for fila in reader:
            dni = int(fila[0])
            materia = str(fila[1])
            fecha = str(fila[2])
            nota = int(fila[3])
            aprobacion = str(fila[4])
            instancia = Materia(dni, materia, fecha, nota, aprobacion)
            self.__lista_materias.append(instancia)
        archivo.close()   

    def Eldni(self, mat):
        return self.__lista_materias[mat].getDni()
    def Lanota(self, mat):
        return self.__lista_materias[mat].getnota()
    def fecha(self, mat):
        return self.__lista_materias[mat].getfecha()
    def nombremateria(self, mat):
        return self.__lista_materias[mat].getnombremateria()
    

    def getlongitud(self):
        return len(self.__lista_materias)

    def mostrarLista(self):
       for materias in self.__lista_materias: 
                print("\tDni: ",materias.getDni(),"\tNombre de Materia: ",materias.getnombremateria(),"\tFecha: ",materias.getfecha(),"\tNota: ",materias.getnota(),"\tAprobacion: ",materias.getaprobacion())
                print ("\n")
    def buscar_DNI (self, alternativo):
        band = False
        i = 0
        acuum=0
        cont=0
        while i < len(self.__lista_materias):
            if (alternativo == self.__lista_materias[i].getDni()):
                acuum += self.__lista_materias[i].getnota()
                cont+=1
          
            i+=1
        return acuum/cont


