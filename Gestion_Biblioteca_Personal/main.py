from model.Libro import Libro

if __name__ == '__main__':
    """
        Metodo de inicio de el proyecto
        
        version: 0.1
        autor: Javier Moreno Salas
    """
    print("version 0.1")

    libro1 = Libro(titulo="Las aventuras",autor="jhon",anno_publicacion="10-10-2014")

    print(libro1)

    libro1.modificar_autor(nuevo_autor="Pepe")

    print(libro1)

    libro2 = Libro(titulo="Las aventuras 2",autor="jhon",anno_publicacion="10-10-2014")

    print(libro2)

