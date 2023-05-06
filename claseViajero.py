class ViajeroFrecuente(object):
    __numero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millasAc = 0
    def __init__(self, num=0, dni='' ,nom='', ap='', mill=0):
        self.__numero = num
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = ap
        self.__millasAc += mill
    
    
    def getNumeroViajero(self):
        return self.__numero
    def getnombre (self):
        return self.__nombre
    def getdni(self):
        return self.__dni
    def getapellido(self):
        return self.__apellido
    def getacummillas(self):
        return self.__millasAc
    
    def  __gt__ (self, otroViajero):
        return ViajeroFrecuente(self.__millasAc > otroViajero.getacummillas())
    
    def __add__(self, otroViajero):
        if type(self) == type(otroViajero):
            return ViajeroFrecuente(self.__numero,self.__dni,self.__nombre,self.__apellido, self.__millasAc + otroViajero.getacummillas())
    def __sub__(self, otroViajero):
        if type(self) == type(otroViajero):
            return ViajeroFrecuente(self.__numero,self.__dni,self.__nombre,self.__apellido, self.__millasAc - otroViajero.getacummillas())