# Clase Usuario
class Usuario:
    def __init__(self, nombre, id):
        self.nombre = nombre  # Nombre del usuario
        self.id = id  # ID del usuario

    def consultar_multas(self):
        # Método para consultar multas (pendiente de implementación)
        pass

    def realizar_prestamo(self, libro, catalogo):
        # Método para realizar un préstamo a través del catálogo
        return catalogo.prestar_libro(self, libro)

# Clase Catalogo
class Catalogo:
    def __init__(self):
        self.libros = []  # Lista de libros disponibles en el catálogo

    def verificar_disponibilidad(self, titulo):
        # Método para verificar si un libro está disponible
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro.disponibilidad
        return False

    def actualizar_catalogo(self, libro):
        # Método para añadir un libro al catálogo
        self.libros.append(libro)

    def prestar_libro(self, usuario, libro):
        # Método para prestar un libro a un usuario
        if libro.disponibilidad:
            libro.disponibilidad = False  # Marcar el libro como no disponible
            prestamo = Prestamo(usuario, libro)
            return prestamo
        else:
            print("Libro no disponible")

# Clase Libro
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo  # Título del libro
        self.autor = autor  # Autor del libro
        self.disponibilidad = True  # Disponibilidad del libro (por defecto, disponible)

    def actualizar_disponibilidad(self, disponible):
        # Método para actualizar la disponibilidad del libro
        self.disponibilidad = disponible

# Clase Prestamo
class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario  # Usuario que realiza el préstamo
        self.libro = libro  # Libro que se presta
        self.fecha_prestamo = "2024-12-05"  # Fecha del préstamo (ejemplo)
        self.fecha_devolucion = None  # Fecha de devolución (por determinar)

    def realizar_prestamo(self):
        # Método para registrar el préstamo (pendiente de implementación)
        pass

    def devolver_libro(self):
        # Método para devolver el libro prestado
        self.libro.actualizar_disponibilidad(True)
        self.fecha_devolucion = "2024-12-15"  # Fecha de devolución (ejemplo)

# Ejemplo de uso del sistema de biblioteca
catalogo = Catalogo()
libro1 = Libro("PARADIGMAS DE LA PROGRAMACION I", "Autor JULIO DE LA TEJA")
catalogo.actualizar_catalogo(libro1)

usuario1 = Usuario("GENARO", 123)
prestamo = usuario1.realizar_prestamo(libro1, catalogo)

if prestamo:
    print(f"Préstamo realizado por {prestamo.usuario.nombre} del libro '{prestamo.libro.titulo}'")
else:
    print("No se pudo realizar el préstamo")

# Devolver el libro
prestamo.devolver_libro()
print(f"Libro '{prestamo.libro.titulo}' devuelto por {prestamo.usuario.nombre}")
