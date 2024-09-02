class Libro:
    def __init__(self, titulo, autor, isbn, paginas, genero):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.genero = genero
    
    def prestar(self):
        print("Prestado")
    
    def devolver(self):
        print("Devuelto")
    
    def buscarPorTitulo(self, titulo):
        return self.titulo == titulo

class Autor:
    def __init__(self, nombre, nacionalidad, fechaNacimiento):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fechaNacimiento = fechaNacimiento
    
    def publicarLibro(self, titulo):
        print("Publicado")

class Lector:
    def __init__(self, nombre, edad, direccion, numeroSocio):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.numeroSocio = numeroSocio
    
    def solicitarPrestamo(self, libro):
        print("Prestado")
    
    def devolverLibro(self, libro):
        print("Devuelto")

class Libreria:
    def __init__(self, autores, lectores):
        self.autores = autores
        self.lectores = lectores
    
    def agregarLibro(self, Libro):
        pass

    def buscarLibro(self, Libro)
        
class Libreta:
    def __init__(self) -> None:
        pass