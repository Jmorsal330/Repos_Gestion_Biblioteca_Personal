import json

class Controlador_Json:
    """
    Clase que actúa como controlador para manipular operaciones relacionadas con archivos JSON.

    Métodos:
    - __init__(): Constructor de la clase que inicializa la creación de un nuevo archivo JSON.
    - agregar_libro_fichero(libro): Agrega la representación JSON de un libro al archivo JSON de la biblioteca.
    - eliminar_libro(Listado_Libros): Elimina los contenidos existentes del archivo JSON y agrega los libros proporcionados.
    - modificar_libro(Listado_Libros): Vacía el archivo JSON y agrega los libros proporcionados.
    - vaciar_fichero(): Vacia el contenido del archivo JSON.

    Atributos:
    - No hay atributos de instancia en esta clase.
    """

    def __init__(self):
        """
        Constructor de la clase Controlador_Json.

        Inicializa la creación de un nuevo archivo JSON ("Biblioteca.json").
        """
        self.vaciar_fichero()

    def agregar_libro_fichero(self, libro):
        """
        Agrega la representación JSON de un libro al archivo JSON de la biblioteca.

        :param libro: Libro a agregar al archivo JSON.
        """
        try:
            with open("Biblioteca.json", "a") as fichero:
                json.dump(libro.__dict__(), fichero, indent=2)
        except FileNotFoundError as e:
            print(f"Error: fichero no encontrado: {e}")

    def eliminar_libro(self, Listado_Libros):
        """
        Elimina los contenidos existentes del archivo JSON y agrega los libros proporcionados.

        :param Listado_Libros: Lista de libros para agregar al archivo JSON.
        """
        self.vaciar_fichero()

        for libro in Listado_Libros:
            self.agregar_libro_fichero(libro)

    def modificar_libro(self, Listado_Libros):
        """
        Vacía el archivo JSON y agrega los libros proporcionados.

        :param Listado_Libros: Lista de libros para agregar al archivo JSON.
        """
        self.vaciar_fichero()

        for libro in Listado_Libros:
            self.agregar_libro_fichero(libro)

    def vaciar_fichero(self):
        """
        Vacia el contenido del archivo JSON ("Biblioteca.json").
        """
        with open("Biblioteca.json", "w") as fichero:
            fichero.write(" ")
