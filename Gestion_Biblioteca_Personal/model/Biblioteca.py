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
        :return:
        """

        libro = Libro(titulo=titulo, autor=autor, anno_publicacion=anno_publicacion)

        self._ListadoLibros.append(libro)

    def eliminar_libro_id(self,id):
        """
        Elimina un libro de la biblioteca según su ID.

        :param id: ID del libro a eliminar
        """
        for libro in self._ListadoLibros:
            if(libro._id == id):
                self._ListadoLibros.remove(libro)

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