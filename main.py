from claseViajero import ViajeroFrecuente

if __name__ ==  '__main__':
    unViajero = ViajeroFrecuente(2211, 20302484, 'Oscar','Martin', 79213)
    
    otroViajero = ViajeroFrecuente(332233, 45634424, 'Cristian', 'Alvarez', 43567)
    mayormillas = unViajero > otroViajero
    mayormillas = unViajero if unViajero > otroViajero else otroViajero
    print('El viajero con mayor cantidad de millas acumuladas es: {} {} (millas:{})'.format(mayormillas.getnombre(),mayormillas.getapellido(),mayormillas.getacummillas()))
    acumularmillas = unViajero + otroViajero
    
    print('La acumulacion de millas es: {}' .format(acumularmillas.getacummillas()))
    canjearmillas = unViajero - otroViajero
    print('Las millas canjeadas son: {}' .format(canjearmillas.getacummillas()))
    