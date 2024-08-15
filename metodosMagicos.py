class Rectangulo:
    def __init__(self, anchura, altura):
        self.anchura = anchura
        self.altura = altura

    def __str__(self):
        return f"El ancho del rectangulo es {self.anchura}, y su altura es {self.altura}"
    

    
rect_uno = Rectangulo(10, 3)
rect_dos = Rectangulo(10, 5)
rect_tres = rect_uno + rect_dos
print(rect_tres)