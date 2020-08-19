import pymysql
from bdprestamos import*

class Agenda:
    # Iniciamos nuestra clase
    def __init__(self):
        # rearemos una lista donde guardaremos los datos de nuestra agenda
        #self.contactos = []
        connect()
        create_tablas()

    # Menu del programa
    def menu(self):
        print()
        menu = [
            ['Agenda Personal'],
            ['1. Añadir Contacto', "anadir"],
            ['2. Lista de contactos'],
            ['3. Buscar contacto'],
            ['4. Editar contacto'],
            ['5. Cerrar agenda']
        ]
        

        for x in range(6):
            print(menu[x][0])

        opcion = int(input("Introduzca la opción deseada: "))
        if opcion == 1:
            print()
        elif opcion == 2:
            print()
        elif opcion == 3:
            print()
        elif opcion == 4:
            print()
        elif opcion == 5:
            print("Saliendo de la agenda ...")
            exit()
        # Volvemos a llamar al menú
        self.menu()
agenda = Agenda()
agenda.menu()