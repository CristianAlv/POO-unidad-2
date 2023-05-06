from classConjunto import Conjunto
from menu import Menu
if __name__ ==  '__main__':
    unConj = Conjunto()
    unConj.cargarConjunto()
    unConj.mostrarConjunto()
    otroConj = Conjunto()
    otroConj.cargarConjunto()
    otroConj.mostrarConjunto()
    
    
    
    Mod_Menu = Menu()
    Salir = True
    while Salir:
        print("Bienvenido al Menú")
        print("1. Opción 1: Adicion entre dos conjuntos")
        print("2. Opción 2: Diferencia: ")
        print("3. Opción 3: Verificar si dos conjuntos son iguales")
        print("0. Salir")
        opcion = input("Ingrese la opcion: ")
        if opcion =='1':
            Mod_Menu.opcion1(unConj,otroConj)
        elif opcion =='2':
            Mod_Menu.opcion2(unConj,otroConj)
        elif opcion == '3':
            Mod_Menu.opcion3(unConj,otroConj)
        else:
            if (opcion == '0'):
                    Salir = False
                    Mod_Menu.salir()
            else:
                print ("Opcion invalida")
                Salir=False
    
    
    
    