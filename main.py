import classEmail
import csv
def test():
        IDcuenta= str(input("Ingrese id de la cuenta: "))
        dom = str(input("Ingrese el dominio: "))
        tipD = str(input("Ingrese el tipo de dominio: "))
        contra = str(input("Ingrese la contraseña: "))
        email1= classEmail.email(IDcuenta,dom,tipD,contra)
        print(email1.retornaEmail())
        print(email1.getDominio())


        nombre = str(input("Ingrese su nombre: "))
        Correo = str(input("Ingrese el correo electronico: "))
        email12 = classEmail.email(IDcuenta,dom,tipD,contra)
        email12.CrearCuenta(Correo)
        print ("Estimado ", nombre, "te enviaremmos mensajes a la direccion de correo ", email12.retornaEmail())
   
        
        ContrasenaActual = input ("Ingrese su clave actual, para cambiarla por una nueva:")
        email113 =classEmail.email(IDcuenta,dom,tipD,contra)
        email113.NuevaContraseña(ContrasenaActual)
        
        
        direccion_correonuevo =  'juanLiendro1957@yahoo.com'
        email4 = classEmail.email(IDcuenta,dom,tipD,contra)
        email4.Crear_Cuenta(direccion_correonuevo)
        print (email4.retornaEmail())
        


def archivocsv():
        archivo = open('CORREOS.csv')
        reader = csv.reader(archivo, delimiter = ';')
        print("Archivo Leido con exito")
        lista_datosvalidos = []
        listar_datosnovalidos = []                
        for fila in reader:
                direccion = fila[:4]
                if fila == direccion:
                        lista_datosvalidos.append(direccion)
                        
                else:    
                        listar_datosnovalidos.append(fila)
                        
        print ("Correos validos: ", lista_datosvalidos)
        print ("Correos no validos: ", listar_datosnovalidos)
                        
        archivo.close()        

        contador = 0  
        donIngresado = str(input("Ingrese el dominio: "))
        for fila in lista_datosvalidos:
                if (donIngresado == fila[1]):
                        contador+=1
        print("La cantidad de correos que coinciden con el dominio ingresado son: ", contador)


if __name__ == '__main__':
        #test()
        archivocsv()

