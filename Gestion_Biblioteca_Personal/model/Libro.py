class Libro:
    """
    Clase Libro formada por un id, un titulo, un autor y su anno de publicacion.

    Su funcion principal es la de poder crear y modificar libros
    """

    id = 0

    def __init__(self, titulo, autor, anno_publicacion):
        """
        Metodo constructor de la clase Libro

        :param titulo: Es el nombre que recibe el libro
        :param autor: Es el nombre del escritor del libro
        :param anno_publicacion: Es la fecha de publicacion del libro
        """
        Libro.id += 1
        self.id = Libro.id
        self.titulo = titulo
        self.autor = autor
        self.anno_publicacion = anno_publicacion

    @property
    def titulo(self):
        """
        Metodo get de titulo

        :return: devuelve el nombre del titulo actual
        """
        return self.titulo
    @titulo.setter
    def titulo(self, nuevo_titulo):
        """
        Metodo set de titulo

        :param nuevo_titulo: Es el nuevo nombre que recibe el libro
        """
        self.titulo = nuevo_titulo

    @property
    def autor(self):
        """
        Metodo get de autor

        :return: devuelve el nombre del autor actual
        """
        return self.autor
    @autor.setter
    def autor(self,nuevo_autor):
        """
        Metodo set de autor

        :param nuevo_autor: Es el nuevo nombre que recibe el autor del libro
        """
        self.autor = nuevo_autor

    @property
    def anno_publicacion(self):
        """
        Metodo get de anno_publicacion

        :return: devuele el anno de publicación actual
        """
        return self.anno_publicacion
    @anno_publicacion.setter
    def anno_publicacion(self, nuevo_anno_publicacion):
        """
        Metodo set de anno_publicacion

        :param nuevo_anno_publicacion: Es el nuevo anno de publicacion del libro
        """
        self.anno_publicacion = nuevo_anno_publicacion

    def modificar_titulo(self,nuevo_titulo):
        """
        Metodo para modificar el titulo

        :param nuevo_titulo: es el nuevo titulo del libro
        """
        self.titulo = nuevo_titulo

    def modificar_autor(self,nuevo_autor):
        """
        Metodo para modificar el autor

        :param nuevo_autor: es el nuevo autor
        """
        self.autor = nuevo_autor

    def modificar_anno_publicacion(self,nuevo_anno_publicacion):
        """
        Metodo para modificar el anno de publicacion

        :param nuevo_anno_publicacion: es el nuevo anno de publicacion
        """
        self.anno_publicacion = nuevo_anno_publicacion


    def __str__(self):
        """
        Metodo str, muestra el contenido de libro

        :return: devuelve un resumen del contenido del libro
        """
        return (f'id= {self.id} \ntitulo= {self.titulo} \nautor= {self.autor} \naño de publicación= {self.anno_publicacion} \n')