from model.Biblioteca import Biblioteca

class Controlador_Biblioteca():
    from model.Biblioteca import Biblioteca

    class Controlador_Biblioteca():
        """
        Clase que actúa como controlador para manipular una instancia de la clase Biblioteca.

        Métodos:
        - __init__(): Constructor de la clase que inicializa una instancia de Biblioteca.
        - agregar_libro(titulo, autor, anno_publicacion): Agrega un nuevo libro a la biblioteca mediante el controlador.
        - eliminar_libro(id): Elimina un libro de la biblioteca mediante el controlador según su ID.
        - modificar_libro(id): Proporciona un menú interactivo para modificar un libro de la biblioteca mediante el controlador.
        - buscar_libro(id): Busca un libro en la biblioteca mediante el controlador según su ID.
        - __str__(): Devuelve una representación en cadena del estado actual de la biblioteca.

        Atributos:
        - biblioteca: Instancia de la clase Biblioteca que es manipulada por el controlador.
        """

        def __init__(self):
            """
            Constructor de la clase Controlador_Biblioteca.

            Inicializa la instancia de Biblioteca como un atributo.
            """
            self.biblioteca = Biblioteca()

        def agregar_libro(self, titulo, autor, anno_publicacion):
            """
            Agrega un nuevo libro a la biblioteca mediante el controlador.

            :param titulo: Título del libro.
            :param autor: Autor del libro.
            :param anno_publicacion: Año de publicación del libro.
            """
            self.biblioteca.agregar_libro(titulo, autor, anno_publicacion)

        def eliminar_libro(self, id):
            """
            Elimina un libro de la biblioteca mediante el controlador según su ID.

            :param id: ID del libro a eliminar.
            """
            self.biblioteca.eliminar_libro(id)

        def modificar_libro(self, id):
            """
            Proporciona un menú interactivo para modificar un libro de la biblioteca mediante el controlador.

            :param id: ID del libro a modificar.
            """
            self.biblioteca.modificar_libro(id)

        def buscar_libro(self, id):
            """
            Busca un libro en la biblioteca mediante el controlador según su ID.

            :param id: ID del libro a buscar.
            :return: Objeto Libro si se encuentra, None si no se encuentra.
            """
            return self.biblioteca.buscar_libro(id)

        def __str__(self):
            """
            Devuelve una representación en cadena del estado actual de la biblioteca.

            :return: Cadena que representa los libros en la biblioteca.
            """
            return str(self.biblioteca)
