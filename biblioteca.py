# Vamos a crear una biblioteca simple. Tendremos libros con título, autor y si están disponibles o prestados. 
# Los usuarios podrán buscar libros, prestarlos y devolverlos.

class Autor:
    def __init__(self, nombre):
        self.nombre = nombre

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def buscar(self, titulo):
        if self.titulo == titulo:
            print(f"El libro {self.titulo} esta disponible")
            return True
        
    # def buscar(self, titulo):
    # if self.titulo == titulo:
    #     print(f"El libro '{self.titulo}' está disponible")
    # else:
    #     print("Libro no encontrado")

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro {self.titulo} ha sido prestado.")
            return True
        else:
            print(f"El libro {self.titulo} no esta disponible")
            return False
    
    def devolver(self):
        self.disponible = True
        print(f"El libro {self.titulo} ha sido devuelto.")
    
def buscarLibro(libros, titulo):
    for libro in libros:
        if libro.buscar(titulo):
            return
    print(f"El libro {titulo} no fue encontrado")



# libro1.buscar("Cien años de soledad")
# libro2.buscar("perro")
# libro1.prestar()
# libro1.devolver()

# autor3 = Autor("Gabriel Garcia Marquez")
# libro3 = Libro("Cualquier libro", autor3)

autor1 = Autor("Gabriel Garcia Marquez")
autor2 = Autor("Jorge Luis Borges")
libro1 = Libro("Cien años de soledad", autor1)
libro2 = Libro("Un dia de estos", autor1)
libro3 = Libro("Cien años", autor2)

libros = [libro1, libro2]

buscarLibro(libros, "Cien años de soledad")
buscarLibro(libros, "perro")
