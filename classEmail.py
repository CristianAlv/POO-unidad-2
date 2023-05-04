class email:
    __IDcuenta = ''
    __dom = ''
    __tipo_dominio = ''
    __password = ''

    def __init__(self,IDcuenta, dom,tipD,contra):
        self.__IDcuenta = IDcuenta
        self.__dom = dom
        self.__tipo_dominio = tipD
        self.__password = contra
        
    def retornaEmail(self):
        return (self.__IDcuenta + "@" + self.__dom + '.' + self.__tipo_dominio)
    
    
    def getDominio(self):
        return("El dominio del correo es:", self.__dom)
    
    def CrearCuenta(self, Correo):
        trozo = Correo.split('@')
        self.__IDcuenta = trozo[0]
        trozo2 = trozo[1].split('.')
        self.__dom = trozo2[0]
        self.__tipo_dominio =trozo2[1]
    
    def Crear_Cuenta(self, direccion_correonuevo):
        parte = direccion_correonuevo.split('@')
        self.__IDcuenta=parte[0]
        parte2 = parte[1].split('.')
        self.__dom = parte2[0]
        self.__tipo_dominio = parte2[1]
        
    def NuevaContraseña(self, contrasenaActual):
        if contrasenaActual == self.__password:
            nueva_password = str(input("Ingrese la nueva contraseña: "))
            self.__password = nueva_password
        else:
            print ("La contraseña no fue ingresada correctamente")
