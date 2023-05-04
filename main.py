import csv
from Manejador import Manejador
from claseRegistro import Registro
from menu import Menu
def test():
    mv = Manejador()
    mv.test_lista()

if __name__ == '__main__':
    test()
    print("\n---Ha finalizado el testeo de datos----")
    input("Presione una tecla para continuar: ")
    mv = Manejador()
    mv.test_lista()
    mv.mostrarLista()
    
    Mod_Menu = Menu()
    Salir = True
    dia = (int(input("Ingrese el dia: ")))
    while Salir:
        print("Bienvenido al Menú")
        print("1. Opción 1: Mostrar para cada variable el día y hora de menor y mayor valor")
        print("2. Opción 2: Promedio: ")
        print("3. Opción 3: Listar los valores de las tres variables para cada hora del día dado")
        print("0. Salir")
        opcion = input("Ingrese la opcion: ")
        if opcion =='1':
            Mod_Menu.opcion1()
        elif opcion =='2':
            Mod_Menu.opcion2()
        elif opcion == '3':
            Mod_Menu.opcion3(dia)
        else:
            if (opcion == '0'):
                    Salir = False
                    Mod_Menu.salir()
            else:
                print ("Opcion invalida")
                Salir=False