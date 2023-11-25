class Libro:

    id = 0

    def __init__(self, titulo, autor, anno_publicacion):
        Libro.id += 1
        self.id = Libro.id
        self.titulo = titulo
        self.autor = autor
        self.anno_publicacion = anno_publicacion

    def modificar_titulo(self,nuevo_titulo):
        self.titulo = nuevo_titulo
    def modificar_autor(self,nuevo_autor):
        self.autor = nuevo_autor

    def modificar_anno_publicacion(self,nuevo_anno_publicacion):
        self.anno_publicacion = nuevo_anno_publicacion

    def __str__(self):
        return (f'id= {self.id} \ntitulo= {self.titulo} \nautor= {self.autor} \naño de publicación= {self.anno_publicacion} \n')