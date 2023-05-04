

class Registro(object):
    __temperatura = None
    __hum = None
    __PresionAt = None
    
    def __init__(self, temp, humedad, presion):
        self.__temperatura = temp
        self.__hum = humedad
        self.__PresionAt = presion
        
    def getTemp(self):
        return self.__temperatura
    def gethumedad(self):
        return self.__hum
    def getpresion(self):
        return self.__PresionAt
    def getdatos (self):
        return self.__temperatura, self.__hum, self.__PresionAt        