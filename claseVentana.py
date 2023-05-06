class Ventana(object):
    __titulo = ''
    __X1 = None
    __Y1 =None
    __X2 = None
    __Y2 = None
        
    def __init__(self, titulo='', X1=0, Y1=0, X2=0, Y2=0):
        self.__titulo = titulo
        self.__X1= max(0,X1)
        self.__Y1 = max(0, Y1)
        self.__X2 = min(500,X2)
        self.__Y2 = max(500,Y2)
         
        if self.__X1 > self.__X2:
            self.__X1, self.__X2 = self.__X1, self.__X2
        if self.__Y1 > self.__Y2:
            self.__Y1, self.__Y2 = self.__Y1, self.__Y2
            
    def __str__(self):
        return (self.__titulo ({self.__X1}, {self.__Y1}) - ({self.__X2}, {self.__Y2}))
            
    def moverIzquierda(self, desplazamiento):
        if (self.__X1 > 0):
            self.__X1-=10
            self.__X2-=10
    def moverDerecha(self, desplazamiento):
        if (self.__X2 < 500):
            self.__X1 +=10
            self.__X2+=10
            
    def subir(self, desplazamiento=1):
        if(self.__Y1 > 0):
            self.__Y1 -=10-5
            self.__Y2-=10-5
            
    def bajar(self, desplazamiento=1):
        if (self.__Y2 < 500):
            self.__Y2+=10
            self.__Y1+=10
            
    def ancho(self):
        return self.__X2-self.__X1
        
    def alto(self):
        return self.__Y2-self.__Y1   
        
    def getTitulo(self):
        return self.__titulo

    def mostrar(self):
        
        print("Título:", self.__titulo)
        print("Vértice superior izquierdo: ({}, {})".format(self.__X1, self.__Y1))
        print("Vértice inferior derecho: ({}, {})".format(self.__X2, self.__Y2))
        print("Ancho:", self.ancho())
        print("Alto:", self.alto())
        
    def Borrar(self, titulo, x1, y1, x2, y2):
        self.__titulo= titulo
        self.__X1 = x1
        self.__Y1 = y1
        self.__X2 = x2
        self.__Y2 = y2