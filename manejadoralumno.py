from clasealumno import Alumno
import csv
import numpy as np

class ManejadorAlumno(object):

	def __init__(self, dimension = 8):
		self.__arreAlumno = np.empty((dimension), dtype=Alumno)
		self.dimension = dimension
				
	def test_Cargar1(self):
				cabecera = True
				indice = 0
				archivo = open("alumnos.csv")
				reader= csv.reader(archivo, delimiter=';')
				for fila in reader:
								if cabecera:
									cabecera= not cabecera
								else:
									alumno2 = Alumno(int(fila[0]), fila[1], fila[2], fila[3], fila[4])
									self.__arreAlumno[indice] = alumno2
			
									indice+=1
				archivo.close()
						
	def MostrarCarga(self):
		alumno=0
		for alumno in range (self.dimension): 
			print("\t Dni:",self.__arreAlumno[alumno].getDocumento(), "\t Apellido:",self.__arreAlumno[alumno].getapellido(), "\t Nombre:",self.__arreAlumno[alumno].getnombre(), "\t Carrera:",self.__arreAlumno[alumno].getcarrera(), "\t Cursado:",self.__arreAlumno[alumno].getcursado())


	def getdimension(self):
		return self.dimension

	def Estudiante(self, materia, lista):
		i=0
		mat=0
		print("Dni: ","\tApellido y Nombre: ","\tFecha: ","\tNota: ","\tAprobacion: ")
		tamaño_lista = lista.getlongitud()
		for i in range (self.dimension):
			for mat in range (tamaño_lista):
					if self.__arreAlumno[i].getDocumento() == lista.Eldni(mat) and lista.Lanota(mat) >= 7 and materia == lista.nombremateria(mat):
							print("{}\t{} {}\t{}\t{}\t{}".format(self.__arreAlumno[i].getDocumento(), self.__arreAlumno[i].getapellido(), self.__arreAlumno[i].getnombre(), lista.fecha(mat), lista.Lanota(mat), self.__arreAlumno[i].getcursado()))

	
	def Listado(self):
		arreglo_ordenado = np.sort(self.__arreAlumno)
		for alumno in arreglo_ordenado:
			print (alumno)