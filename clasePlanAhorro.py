class PlanAhorro(object):
    __codigo = None 
    __modelo = ''
    __version = '' 
    __valordel_vehiculo= None 
    __cuotasdelplan = 0 
    __cuotaspagas = 0
    def __init__(self, cod, model, vers, valor, cuotas, cuotaspagas):
        self.__codigo = cod
        self.__modelo = model
        self.__version = vers
        self.__valordel_vehiculo = valor
        self.__cuotasdelplan = cuotas
        self.__cuotaspagas = cuotaspagas
        
    def getCodigo(self):
        return self.__codigo
    def getcuotas (self):
        return self.__cuotasdelplan
    def cuotas_pagas(self):
        return self.__cuotaspagas
    def getmodelo (self):
        return self.__modelo
    def getvalor (self):
        return self.__valordel_vehiculo
    def getversion(self):
        return self.__version
    
    def setvalor (self, valor):
        self.__valordel_vehiculo = valor
        print ("El valor del vehiculo fue cambiado con exito")
        
    @classmethod
    def Modificarcuota(cls):
            cuotas = int(input("Ingrese la cantidad de cuotas para modificar: "))
            cls.__cuotaspagas = cuotas
            print ("La modificacion fue exitosa")
            print ("Los planes fueron modificados por la cantidad de: ", cls.__cuotaspagas)        
    