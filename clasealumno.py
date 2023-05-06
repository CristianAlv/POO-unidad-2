class Alumno(object):
    __dni = 0
    __apellido = ''
    __nombre = ''
    __carrera = ''
    __cursa = 0
    
    def __init__(self, dni, apellido, nombre, carrera, cursado):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__cursa = cursado
        
    def getDocumento(self):
        if (self.__dni is not None):
            return self.__dni
    def getapellido(self):
        return self.__apellido
    def getnombre (self):
        return self.__nombre
    def getcarrera(self):
        return self.__carrera
    def getcursado(self):
        return self.__cursa
    
    def getdatos(self):
        return self.__dni,self.__apellido,self.__nombre,self.__carrera,self.__cursa

        
    
    def __lt__(self, other):
        if self.getcursado() == other.getcursado():
            return self.getapellido().lower() < other.getapellido().lower()
        else:
            return self.getcursado() < other.getcursado()
        
    
        
    def __str__(self):
        return f"{self.__apellido}, {self.__nombre} - {self.__cursa}"