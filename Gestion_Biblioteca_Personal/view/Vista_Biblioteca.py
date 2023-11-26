from controller.Controlador_Biblioteca import Controlador_Biblioteca
class Vista_Biblioteca():
    """
    Clase que representa la vista para interactuar con la biblioteca.
    """

    def __init__(self):
        """
        Inicializa la vista creando una instancia del Controlador_Biblioteca.
        """
        self.controlador = Controlador_Biblioteca()

    def menu(self):
        """
        Muestra el menú principal de la aplicación.
        """
        print("\n------ Menú Principal ------")
        print("1. Agregar Libro")
        print("2. Eliminar Libro")
        print("3. Modificar Libro")
        print("4. Buscar Libro")
        print("5. Mostrar Biblioteca")
        print("0. Salir")

    def opcion_usuario(self):
        """
        Maneja las opciones ingresadas por el usuario y realiza las acciones correspondientes.
        """
        while True:

            self.menu()

            try:
                opc = int(input("\nIndicame una Opcion: \n"))

                if opc == 1:
                    t = input("Indicame el titulo: ")
                    a = input("Indicame el autor: ")
                    anno = input("Indicame el anno de publicacion: ")
                    self.controlador.agregar_libro(t, a, anno)
                elif opc == 2:
                    id = int(input("Indicame el id del libro a eliminar: "))
                    self.controlador.eliminar_libro(id)
                elif opc == 3:
                    id = int(input("Indicame el id del libro a modificar: "))
                    self.controlador.modificar_libro(id)
                elif opc == 4:
                    id = int(input("Indicame el id del libro a buscar: \n"))
                elif opc == 5:
                    print(self.controlador)
                elif opc == 0:
                    print("Has salido con exito\n")
                    break
                else:
                    print("Opción no válida. Por favor, elige una opción válida.")

            except ValueError:
                print("Error: Ingresa un número entero válido.")

