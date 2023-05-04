
class ViajeroFrecuente(object):
    __numero= None
    __dni = None
    __nombre = None
    __apellido = None
    __millasAc = None
    def __init__(self, num=0, dni=0,nom='',ap='', mill=0):
        self.__numero = num
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = ap
        self.__millasAc = mill
    
    def getNumeroViajero(self):
        return self.__numero

    def cantidadTotaldeMillas (self):
        return self.__millasAc
    
    def acumularMillas (self, millas):
        self.__millasAc += millas

    def canjearMillas (self, cantAcanjear):
        if cantAcanjear <= self.__millasAc:
            print("Las millas han sido canjeadas con exito!\n")
        else:
            print("Error en la operacion: no se puede canjear las millas\n")

    def mostrarViajero (self):
        return("Numero: {}-DNI: {}-Nombre: {}\nApellido: {}-Millas: {}".format(self.__numero, self.__dni, self.__nombre, self.__apellido, self.__millasAc))