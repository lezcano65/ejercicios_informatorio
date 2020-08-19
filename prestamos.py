import pymysql
from bdprestamos import*
class sistema:
    def __init__(self):
        connect()
        create_tablas()
    def menu(self):
        print()
        menu = [
            ['sistema de prestamos'],
            ['1. Añadir cliente'],
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
        self.menu()
class pago_coutas:
    def __init__(self,numero_prestamo,numero_cuota,fecha_pago,montopagado):
        self.numero_prestamo = numero_prestamo
        self.numero_cuota = numero_cuota
        self.fecha_pago = fecha_pago
        self.montopagado = montopagado
    def registrar_pago(self):
        print()
class clientes:
    def __init__(self,dni,nombres,apellidos,telefono,celular):
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono
        self.celular = celular
    def registrar_cliente(self):
        pass
class empleados:
    def __init__(self,nombre,cuil):
class empleados:
    def __init__(self,nombre,cuil):
        self.nombre = nombre
        self.cuil = cuil
class prestamos:
    def __init__(self, numero_prestamo, fecha_autorizacion, monto, cantidad_cuotas, precio_cuota, fecha_tentativa, fecha_entrega):
        self.numero_prestamo = numero_prestamo
        self.fecha_autorizacion = fecha_autorizacion
        self.monto = monto
        self.cantidad_cuotas = cantidad_cuotas
        self.precio_cuota = precio_cuota
        self.fecha_tentativa = fecha_tentativa
        self.fecha_entrega = fecha_entrega
    def verificar_monto(self):
        pass
    def registrar_prestamo(self):
        pass
    def modificar(self):
        pass 
    def calcular_fechapago(self):
        pass 
    def calcular_fechatentativa(self):
        pass 
    def autorizar_prestamo(self):
        pass 
    def calcular_fechaentrega(self):
        pass 
    def consultar_cliente(self):
        pass 

sistemaprestamo = sistema()
sistemaprestamo.menu()