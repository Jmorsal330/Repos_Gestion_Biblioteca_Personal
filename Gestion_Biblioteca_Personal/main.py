from controller.Controlador_Biblioteca import Controlador_Biblioteca
from view.Vista_Biblioteca import Vista_Biblioteca

if __name__ == '__main__':
    """
        Metodo de inicio de el proyecto
        
        version: 1.0
        autor: Javier Moreno Salas
    """

    vista = Vista_Biblioteca()
    vista.menu()
    vista.opcion_usuario()

