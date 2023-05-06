import csv
from clasePlanAhorro import PlanAhorro
class manejadorPA(object):
    ___lista_datos = []
    def __init__(self):
        self.___lista_datos = []
        
            
    def agregarlista(self, Auto):
        self.___lista_datos.append(Auto)
      
    def mostrarLista (self):
            print (hex(id(self.___lista_datos)))
        
    def testlista(self):
        file = open('planes.csv')
        reader = csv.reader(file, delimiter=';')
        print ("Archivo leido exitosamente")
        for fila in reader:                                      #código del plan, modelo y versión del vehículo, valor del vehículo, cantidad de cuotas del plan, cantidad de cuotas que debe tener pagas para licitar el vehículo (los últimos dos atributos son los mismos para todos los planes).
            codigo = int(fila[0])
            modelo = fila[1]
            version = fila[2]
            valordel_vehiculo = int(fila[3])
            cuotasdelplan = int(fila[4])
            cuotaspagas = int(fila[5])
            
            Auto = PlanAhorro(codigo, modelo, version, valordel_vehiculo, cuotasdelplan, cuotaspagas)
            self.agregarlista(Auto)
        
        file.close()
        
        
    def Actualizar_Valor(self):
        for plan in (self.___lista_datos):
            print ("Codigo del vehiculo: ", plan.getCodigo())
            print ("Modelo del vehiculo: ", plan.getmodelo())
            print ("Version del vehiculo: ", plan.getversion()) 
            valor = int(input("Ingrese el valor actual del vehiculo: "))
            if (valor > 0):   
                plan.setvalor(valor)
            else:
                print ("Valor incorrecto revise nuevamente")
                
    def BuscarInferior(self):
        i=0
        band = False
        valor = int(input("Ingrese un valor para comparar: "))
        for vehiculo in self.___lista_datos:
            if (valor > vehiculo.getvalor()):
                band = True
                print ("Codigo del vehiculo: ",vehiculo.getCodigo())
                print ("Modelo del vehiculo: ", vehiculo.getmodelo())
                print ("Version del vehiculo: ", vehiculo.getversion())
                
    def Monto_Licitar(self):
        monto = 0
        for vehiculo in self.___lista_datos:
            monto = vehiculo.cuotas_pagas()*vehiculo.getcuotas()
            print ("El monto que se debe pagar para licitar el vehiculo",vehiculo.getmodelo(), vehiculo.getversion(),"es:", monto)
    

                
         