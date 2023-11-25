from model.Libro import Libro
from model.Biblioteca import Biblioteca

if __name__ == '__main__':
    """
        Metodo de inicio de el proyecto
        
        version: 0.1
        autor: Javier Moreno Salas
    """

    biblioteca = Biblioteca()

    biblioteca.agregar_libro(titulo="a",autor="a",anno_publicacion="a")
    biblioteca.agregar_libro(titulo="b",autor="b",anno_publicacion="b")
    biblioteca.agregar_libro(titulo="c",autor="c",anno_publicacion="c")

    biblioteca.eliminar_libro_id(1)
    print(biblioteca)


