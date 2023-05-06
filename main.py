import csv
from clasePlanAhorro import PlanAhorro
from manejadorPA import manejadorPA
from menu import Menu
def test ():
    mv = manejadorPA()
    mv.testlista()
    
if __name__ == '__main__':
    #test()
    print("\n---Ha finalizado el testeo de datos----")
    input("Presione una tecla para continuar: ")
    mv = manejadorPA()
    mv.testlista()
    mv.mostrarLista()
    print("Mostramos la Lista generada".center(40, "="))
    
    ModMenu = Menu()
    Salir = True
    while Salir:
        print("Bienvenido al Menú")
        print("1. Opción 1: Actualizar el valor del vehiculo")
        print("2. Opción 2: Encontrar valor inferior: ")
        print("3. Opción 3: Modificar la cantidad de cuotas licitas")
        print("4. Opción 4: Modificar la cantidad de cuotas pagas: ")
        print("0. Salir")
        opcion = input("Ingrese la opcion: ")
        if opcion =='1':
            ModMenu.opcion1()
        elif opcion =='2':
            ModMenu.opcion2()
        elif opcion == '3':
            ModMenu.opcion3()
        elif opcion == '4':
            ModMenu.opcion4()
        else:
            if (opcion == '0'):
                    Salir = False
                    ModMenu.salir()
            else:
                print ("Opcion invalida")
                Salir=False