from libro import Libro


def main():
    libros = [
        Libro("La colmena", "Camilo José Cela", 1951),
        Libro("Cien años de soledad", "Gabriel García Márquez", 1967),
        Libro("La casa de Bernarda Alba", "Federico García Lorca", 1936),
        Libro("Nada", "Carmen Laforet", 1945),
        Libro("La familia de Pascual Duarte", "Camilo José Cela", 1942)
    ]

    libro = libros[1]

    try:
        print(libro)
        libro.prestar()
        libro.prestar()
    except ValueError as error:
        print(error)

    try:
        print(libro)
        libro.devolver()
        libro.devolver()
    except ValueError as error:
        print(error)

    print("Total de libros creados:", Libro.total_libros)

    for libro in libros:
        print(libro)

    otro_libro = Libro("Nada", "Carmen Laforet", 1945)

    print(libros[3] == otro_libro)  # True
    print(libros[3] is otro_libro)  # False

    try:
        nuevo_libro = Libro("", "Miguel de Unamuno", 1914)
        libros.append(nuevo_libro)
    except ValueError as error:
        print(f"Error al crear el libro: {error}")

    for libro in libros:
        print(libro.titulo, libro.es_antiguo)

    reciente = Libro("Ejemplo reciente", "Autor de ejemplo", 2022)
    print(reciente.titulo, reciente.es_antiguo)

    print("\n--- Libros ordenados (ASC) ---")
    libros_ordenados = sorted(libros, key=lambda libro: libro.anio)
    for libro in libros_ordenados:
        print(libro)

    print("\n--- Libros ordenados (DESC) ---")
    libros_ordenados = sorted(libros, key=lambda libro: libro.anio, reverse=True)
    for libro in libros_ordenados:
        print(libro)

    print("\n--- Libros disponibles ---")
    disponibles = filter(lambda libro: libro.disponible, libros)
    for libro in disponibles:
        print(libro)

    print("\n--- Títulos de los libros disponibles ---")
    libros[1].prestar()

    titulos_disponibles = map(
        lambda libro: libro.titulo,
        filter(lambda libro: libro.disponible, libros)
    )
    for titulo in titulos_disponibles:
        print(titulo)

    # También se pueden obtener los títulos de los libros disponibles:
    titulos_disponibles = [
        libro.titulo for libro in libros if libro.disponible
    ]

    print("\n--- Libros prestados ---")
    prestados = filter(lambda libro: not libro.disponible, libros)
    for libro in prestados:
        print(libro)
    else:
        print("No hay libros prestados")

    print("\n--- Títulos de los libros prestados ---")
    titulos_prestados = map(
        lambda libro: libro.titulo,
        filter(lambda libro: not libro.disponible, libros)
    )
    for titulo in titulos_prestados:
        print(titulo)

    # También se pueden obtener los libros prestados:
    titulos_no_disponibles = [
        libro.titulo for libro in libros if not libro.disponible
    ]


if __name__ == "__main__":
    main()