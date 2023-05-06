class Materia(object):
    __dni = 0
    __nombre_materia = None
    __fecha = None
    __nota = 0
    __aprobacion = None
    
    def __init__(self, dni, nombre, fecha, nota, aprobacion):
        self.__dni = dni
        self.__nombre_materia = nombre
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion = aprobacion
        
    def getDni(self):
        return self.__dni
    def getnombremateria(self):
        return self.__nombre_materia
    def getfecha (self):
        return self.__fecha
    def getnota(self):
        return self.__nota
    def getaprobacion(self):
        return self.__aprobacion