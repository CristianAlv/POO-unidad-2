import csv
import os
from classViajeroFrecuente import ViajeroFrecuente
from classViajero import ManejadorViajero
from claseMenu import Menu
def test ():
    mv = ManejadorViajero()
    mv.testlista()
    mv.mostrarViajeros ()
    
if __name__ == '__main__':
    #test()
    print("\n---Ha finalizado el testeo de datos----")
    input("Presione una tecla para continuar: ")
    mv = ManejadorViajero()
    mv.testlista()
    mv.mostrarLista()
    print("Mostramos la Lista generada".center(40, "="))
    
    numero = int(input("Ingrese un numero de viajero valido: "))
    b = mv.verificarnumero(numero)
    if b == True:
            print ("Numero de viajero valido")
    else:
            print ("Numero de viajero no valido, intente nuevamente")
            numero = int(input("Ingrese un numero de viajero valido: "))
    
    #while (b != true) ingresar y validar numero
    
    ModMenu = Menu()
    Salir= True
    
    while Salir:
        print("Bienvenido al Menú")
        print("1. Opción 1: Consultar Cantidad de Millas")
        print("2. Opción 2: Acumular Millas.")
        print("3. Opción 3: Canjear Millas.")
        print("0. Salir")
        opcion = input("Ingrese la opcion: ")
        if opcion =='1':
            ModMenu.opcion1(numero)
        elif opcion =='2':
            ModMenu.opcion2(numero)
        elif opcion == '3':
            ModMenu.opcion3(numero)
        else:
            if (opcion == '0'):
                    Salir = False
                    ModMenu.salir()
            else:
                print ("Opcion invalida")
                Salir=False
        
    