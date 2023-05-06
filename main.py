from claseViajero import ViajeroFrecuente

if __name__ ==  '__main__':
    unViajero = ViajeroFrecuente(2211, 20302484, 'Oscar','Martin', 79213)
    otroViajero = ViajeroFrecuente(332233, 45634424, 'Cristian', 'Alvarez', 43567)
    mayormillas = unViajero > otroViajero
    mayormillas = unViajero if unViajero > otroViajero else otroViajero
    print('El viajero con mayor cantidad de millas acumuladas es: {} {} (millas:{})'.format(mayormillas.getnombre(),mayormillas.getapellido(),mayormillas.getacummillas()))
    print("\n")
    acumularmillas = unViajero + otroViajero
    
    print('La acumulacion de millas es: {}' .format(acumularmillas.getacummillas()))
    print("\n")
    canjearmillas = unViajero - otroViajero
    print('Las millas canjeadas son: {}' .format(canjearmillas.getacummillas()))
    print("\n")
    
    numero = int(input("Ingrese el numero entero a comparar: "))
    print("\n")
    igual1 = unViajero == numero
    igual2 = numero == unViajero
    if (igual1 == igual2):
        print ("El viajero si coincide con la cantidad de millas acumuladas en ambas comparaciones")
        
        
    else:
        print ("La comparacion no fue exitosa")
        
    sumaR = numero + unViajero
    print("\n")
    print('El resultado de la suma es: {}' .format(sumaR.getacummillas()))
    print("\n")
    
    restaR = numero - unViajero
    print('El resultado de la resta es: {}' .format(restaR.getacummillas()))
    print("\n")