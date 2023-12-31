class Libro:
    """
    Clase que representa un libro con un ID único, título, autor y año de publicación.

    Métodos:
    - __init__(titulo, autor, anno_publicacion): Constructor de la clase que inicializa un libro con información dada.
    - modificar_titulo(nuevo_titulo): Modifica el título del libro.
    - modificar_autor(nuevo_autor): Modifica el autor del libro.
    - modificar_anno_publicacion(nuevo_anno_publicacion): Modifica el año de publicación del libro.
    - __str__(): Devuelve una representación en cadena del contenido del libro.
    - __dict__(): Método que devuelve un diccionario que representa el libro.


    Atributos:
    - id: Variable de clase para asignar un ID único a cada libro.
    - _id: Variable de instancia que almacena el ID único del libro.
    - _titulo: Variable de instancia que almacena el título del libro.
    - _autor: Variable de instancia que almacena el autor del libro.
    - _anno_publicacion: Variable de instancia que almacena el año de publicación del libro.
    """
    id = 0

    def __init__(self, titulo, autor, anno_publicacion):
        """
        Constructor de la clase Libro.

        :param titulo: Título del libro
        :param autor: Autor del libro
        :param anno_publicacion: Año de publicación del libro
        """
        Libro.id += 1
        self._id = Libro.id
        self.titulo = titulo
        self.autor = autor
        self.anno_publicacion = anno_publicacion

    @property
    def titulo(self):
        """
        Método get para obtener el título del libro.

        :return: Título del libro.
        """
        # El _ en las variables indica que estan protegidas, ademas hace que no confundan cuales son las llamadas a los get y set
        return self._titulo
    @titulo.setter
    def titulo(self, nuevo_titulo):
        """
        Método set para modificar el título del libro.

        :param nuevo_titulo: Nuevo título del libro
        """
        # Este if hace que si no es una istancia de str el nuevo_titulo, lanza true y entra
        if not isinstance(nuevo_titulo, str):
            # raise lanza una excepcion
            raise ValueError("El título debe ser una cadena de caracteres.")
        self._titulo = nuevo_titulo

    @property
    def autor(self):
        """
        Método get para obtener el autor del libro.

        :return: Autor del libro
        """
        return self._autor
    @autor.setter
    def autor(self,nuevo_autor):
        """
        Método set para modificar el autor del libro.

        :param nuevo_autor: Nuevo autor del libro
        """
        if not isinstance(nuevo_autor, str):
            raise ValueError("El autor debe ser una cadena de caracteres.")
        self._autor = nuevo_autor

    @property
    def anno_publicacion(self):
        """
        Método get para obtener el año de publicación del libro.

        :return: Año de publicación del libro
        """
        return self._anno_publicacion
    @anno_publicacion.setter
    def anno_publicacion(self, nuevo_anno_publicacion):
        """
        Método set para modificar el año de publicación del libro.

        :param nuevo_anno_publicacion: Nuevo año de publicación del libro
        """
        if not isinstance(nuevo_anno_publicacion, str):
            raise ValueError("El año de publicación debe ser una cadena de caracteres.")
        self._anno_publicacion = nuevo_anno_publicacion

    def modificar_titulo(self,nuevo_titulo):
        """
        Método para modificar el título del libro.

        :param nuevo_titulo: Nuevo título del libro
        """
        try:
            self.titulo = nuevo_titulo
            print("Título modificado con éxito.")
        except ValueError as e:
            print(f"Error al modificar título: {e}")

    def modificar_autor(self,nuevo_autor):
        """
        Método para modificar el autor del libro.

        :param nuevo_autor:  Nuevo autor del libro
        """
        try:
            self.autor = nuevo_autor
            print("Autor modificado con éxito.")
        except ValueError as e:
            print(f"Error al modificar autor: {e}")

    def modificar_anno_publicacion(self,nuevo_anno_publicacion):
        """
        Método para modificar el año de publicación del libro.

        :param nuevo_anno_publicacion:  Nuevo año de publicación del libro
        """
        try:
            self.anno_publicacion = nuevo_anno_publicacion
            print("Año de publicación modificado con éxito.")
        except ValueError as e:
            print(f"Error al modificar año de publicación: {e}")


    def __str__(self):
        """
        Método que devuelve una representación en cadena del contenido del libro.

        :return: Cadena que representa el contenido del libro
        """
        return (f'id= {self._id} \ntitulo= {self.titulo} \nautor= {self.autor} \naño de publicación= {self.anno_publicacion} \n')


    def __dict__(self):
        """
        Método que devuelve un diccionario que representa el libro.

        :return: Diccionario con las propiedades del libro
        """
        # __dict__ indica como debe ser el json de libro
        return {
            'id':self._id,
            'titulo': self.titulo,
            'autor': self.autor,
            'anno_publicacion': self.anno_publicacion
        },