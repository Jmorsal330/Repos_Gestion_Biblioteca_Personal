from model.Libro import Libro
class Biblioteca():
    """
    Clase que representa una biblioteca que contiene una lista de libros.

    Métodos:
    - __init__(): Constructor de la clase que inicializa la lista de libros.
    - agregar_libro(titulo, autor, anno_publicacion): Agrega un nuevo libro a la biblioteca.
    - eliminar_libro_id(id): Elimina un libro de la biblioteca según su ID.
    - __str__(): Devuelve una representación en cadena de la biblioteca.

    Atributos:
    - _ListadoLibros: Lista que almacena los libros en la biblioteca.
    """
    def __init__(self):
        """
        Constructor de la clase Biblioteca.

        Inicializa la lista de libros (_ListadoLibros) como una lista vacía.
        """
        self._ListadoLibros = []

    def agregar_libro(self, titulo,autor,anno_publicacion):
        """
        Agrega un nuevo libro a la biblioteca.

        :param titulo: Título del libro
        :param autor: Autor del libro
        :param anno_publicacion: Año de publicación del libro
        :return: Objeto Libro si se agrega con éxito, None si hay un error
        """

        try:
            libro = Libro(titulo=titulo, autor=autor, anno_publicacion=anno_publicacion)
            self._ListadoLibros.append(libro)
            return libro
            print("Libro agregado con éxito.\n")
        except ValueError as e:
            print(f"Error al agregar libro: {e}\n")

    def eliminar_libro(self,id):
        """
        Elimina un libro de la biblioteca según su ID.

        :param id: ID del libro a eliminar
        :return: Lista actualizada de libros en la biblioteca
        """
        try:
            for libro in self._ListadoLibros:
                if(libro._id == id):
                    self._ListadoLibros.remove(libro)
                    print("Libro eliminado con exito \n")
                    return self._ListadoLibros
        except Exception as e:
            print(f"Error al eliminar libro: {e}\n")
    def modificar_libro(self,id):
        """
        Proporciona un menú interactivo para modificar un libro según su ID.

        :param id: ID del libro a modificar
        :return: Lista actualizada de libros en la biblioteca
        """
        try:
            while True:
                print("Que deseas modificar: ")
                print("1.- Título")
                print("2.- Autor")
                print("3.- Anno de Publicacion")
                print("0.- Salir \n")
                condc = int(input())

                if(condc == 1):
                    nuevo_titulo = input("Indicame el Titulo nuevo: ")
                    for libro in self._ListadoLibros:
                        if (libro._id == id):
                            libro.modificar_titulo(nuevo_titulo)
                elif(condc == 2):
                    nuevo_autor = input("Indicame el autor nuevo: ")
                    for libro in self._ListadoLibros:
                        if (libro._id == id):
                            libro.modificar_autor(nuevo_autor)
                elif(condc == 3):
                    nuevo_anno_publicacion = input("Indicame el nuevo anno de publicacion: ")
                    for libro in self._ListadoLibros:
                        if (libro._id == id):
                            libro.modificar_anno_publicacion(nuevo_anno_publicacion)
                elif(condc == 0):
                    print("Has salido de modificar el libro\n")
                    return self._ListadoLibros
                    break
                else:
                    print("Opción no válida. Por favor, elige una opción válida.\n")
        except Exception as e:
            print(f"Error al modificar libro: {e}\n")
    def buscar_libro(self,id):
        """
        Busca un libro en la biblioteca según su ID y devuelve el objeto Libro correspondiente.

        :param id: ID del libro a buscar
        :return: Objeto Libro si se encuentra, None si no se encuentra
        """
        try:
            for libro in self._ListadoLibros:
                if (libro._id == id):
                    print(f"Libro encontrado: {libro}")
                    return libro
        except Exception as e:
            print(f"Error al buscar libro: {e}\n")
            return None

    def __str__(self):
        """
        Devuelve una representación en cadena de la biblioteca.

        :return: Cadena que representa los libros en la biblioteca
        """

        libros_str = ""

        for libro in self._ListadoLibros:
            # El metodo str() llama al metodo __str__
            libros_str += str(libro) + "\n"

        return libros_str