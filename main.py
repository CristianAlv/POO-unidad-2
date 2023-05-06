from manejadormateria import ManejadorMateria
from clasealumno import Alumno
from clasemateria import Materia
from manejadoralumno import ManejadorAlumno
from menu import Menu
def test1():
    mv = ManejadorMateria()
    mv.test_lista()
    m2 = ManejadorAlumno()
    m2.test_Cargar1()
    m2.MostrarCarga()


if __name__ == '__main__':
    test1()
    print("\n---Ha finalizado el testeo de datos----")
    input("Presione una tecla para continuar: ")
    m2 = ManejadorAlumno()
    mv = ManejadorMateria()
    mv.test_lista()
    mv.mostrarLista()
    m2.test_Cargar1()
    m2.MostrarCarga()
    otro = Alumno(dni=45634424,apellido="Alvarez",nombre="Cristian", carrera="LSI", cursado=2)

Mod_Menu = Menu()
Salir = True
while Salir:
        print("Bienvenido al Menú")
        print("1. Opción 1: Informar atraves del dni del alumno su promedio con o sin aplazos")
        print("2. Opción 2: Informar los estudiantes que aprobaron en forma promocional: ")
        print("3. Opción 3: Obtener un listado de alumnos ordenado: ")
        print("0. Salir")
        opcion = input("Ingrese la opcion: ")
        if opcion =='1':
            dni_alter = (int(input("Ingrese el dni a buscar: ")))
            Mod_Menu.opcion1(dni_alter)
        elif opcion =='2':
            materia = str(input("Ingrese el nombre de la materia: "))
            Mod_Menu.opcion2(materia, mv)
        elif opcion == '3':
            Mod_Menu.opcion3(otro)
        else:
            if (opcion == '0'):
                    Salir = False
                    Mod_Menu.salir()
            else:
                print ("Opcion invalida")
                Salir=False