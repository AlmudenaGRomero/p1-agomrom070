class Libro:
    total_libros = 0

    
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True
        Libro.total_libros += 1

    def prestar(self):
        if not self.disponible:
            raise ValueError("El libro ya está prestado")

        self.disponible = False


    def devolver(self):
        if self.disponible:
            raise ValueError("El libro ya está disponible")

        self.disponible = True


    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({self.anio}) [{estado}]"


    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        if not isinstance(nuevo_titulo, str):
            raise TypeError("El título debe ser texto")

        if not nuevo_titulo.strip():
            raise ValueError("El título no puede estar vacío")

        self._titulo = nuevo_titulo.strip()

    @property
    def es_antiguo(self):
        return self.anio < 1950