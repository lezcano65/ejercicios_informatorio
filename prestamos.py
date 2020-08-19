import pymysql
from bdprestamos import*

def crear_instancia_cuota_prestamo():
    print('datos de cuota de un prestamo ')
    while True:
        try:
            numero_prestamo = int(input('ingrese el numero de prestamo: '))
            if (numero_prestamo != 0):
                break
        except:
            print('intente de nuevo')
    while True:
        try:
            numero_cuota = int(input('ingrese el numero de prestamo: '))
            if (numero_cuota != 0) and (numero_cuota < 7):
                break
        except:
            print('intente de nuevo')
    fecha = input('ingrese la fecha del pago: ')
    while True:
        try:
            precio = int(input('ingrese el numero de prestamo: '))
            if (precio > 0):
                break
        except:
            print('intente de nuevo')

    return pago_coutas(numero_prestamo, numero_cuota, fecha, precio)

def crear_instancia_prestamos():
    print('datos del prestamo ')
    while True:
        try:
            numero_prestamo = int(input('ingrese el numero de prestamo: '))
            if (numero_prestamo != 0):
                break
        except:
            print('intente de nuevo')
    while True:
        try:
            dni_cliente = int(input('ingrese el dni del cliente: '))
            if (dni_cliente > 0):
                break
        except:
            print('intente de nuevo')
    fecha_autorizacion = input('ingrese  la fecha de autorizacion: ')
    while True:
        try:
            monto = int(input('ingrese el monto del prestamo: '))
            if (monto > 0):
                break
        except:
            print('intente de nuevo')
    while True:
        try:
            cantidad_cuotas = int(input('ingrese la cantidad de cuotas del prestamo: '))
            if (cantidad_cuotas < 7) and (cantidad_cuotas > 0):
                break
        except:
            print('intente de nuevo')
    while True:
        try:
            precio_cuota = int(input('ingrese el precio de las cuotas: '))
            if (precio_cuota > 0):
                break
        except:
            print('intente de nuevo')
    fecha_tentativa = input('ingrese la fecha tentativa: ')
    fecha_entrega = input('ingrese la fecha de entrega: ')
    return prestamos(numero_prestamo, fecha_autorizacion, monto, cantidad_cuotas, precio_cuota, fecha_tentativa, fecha_entrega)

def crear_instancia_empleados():
    print('datos del empleado ')
    nombre = input('ingrese el nombre: ')
    while True:
        try:
            cuil = int(input('ingrese cuil: '))
            break
        except:
            print('intente de nuevo')
    return empleados(nombre, cuil)

def crear_instancia_clientes():
    print('datos del cliente ')
    while True:
        try:
            dni = int(input('ingrese dni: '))
            break
        except:
            print('intente de nuevo')
    nombres = input('ingrese nombre/s: ')
    apellidos = input ('ingrese apellido/s: ')
    while True:
        try:
            telefono = int(input('ingrese telefono: '))
            break
        except:
            print('intente de nuevo')
    while True:
        try:
            celular = int(input('ingrese celular: '))
            break
        except:
            print('intente de nuevo')
    clientes(dni, nombres, apellidos,telefono,celular)
    return clientes(dni, nombres, apellidos,telefono,celular)

class sistema:
    def __init__(self):
        connect()
        create_tablas()
    def menu(self):
        print()
        menu = [
            ['sistema de prestamos'],
            ['1. Añadir cliente'],
            ['2. Lista de clientes'],
            ['3. Buscar cliente'],
            ['4. Editar cliente'],
            ['5. Salir del sistema']
        ]
        for x in range(6):
            print(menu[x])
        while True:
            try:    
                opcion = int(input("Introduzca la opción deseada: "))
                break
            except:
                print('intente de nuevo')
        if opcion == 1:
            print()
        elif opcion == 2:
            print()
        elif opcion == 3:
            print()
        elif opcion == 4:
            print()
        elif opcion == 5:
            print("Saliendo del sistema ...")
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
        print('')

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