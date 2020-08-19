import pymysql
def create_tablas():
    '''Creación de las tablas de Base de datos'''
    conexion = pymysql.connect(host='localhost', 
                                user='root',      
                                password='lezcano65',
                                db='prestamosdb')
    consulta = conexion.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS clientes(dni INTEGER PRIMARY KEY NOT NULL, nombres VARCHAR(30) NOT NULL, apellidos VARCHAR(30) NOT NULL, telefono VARCHAR(14) NOT NULL, celular VARCHAR(14) NOT NULL)'
    try:
        consulta.execute(sql)
        print('La tabla clientes fue creada con éxito')
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("No se pudo crear la tabla clientes: ", e)
    #crear tabla prestamos
        '''KEY dnisolicitante_dni_clientes_00_idx (dni_cliente), CONSTRAINT dnisolicitante_dni_clientes_00 FOREIGN KEY (dni_cliente) REFERENCES clientes (dni)
        KEY `dnisolicitante_dni_clientes_00_idx` (`dni_cliente`),
    CONSTRAINT `dnisolicitante_dni_clientes_00` 
    FOREIGN KEY (`dni_cliente`) REFERENCES `clientes` (`dni`) '''
    sql = 'CREATE TABLE IF NOT EXISTS prestamos(numero_prestamo INTEGER PRIMARY KEY NOT NULL, dni_cliente INTEGER NOT NULL, fecha_autorizacion DATETIME NOT NULL, fecha_tentativa DATETIME NOT NULL, cantidad_de_cuotas INTEGER NOT NULL, monto_prestamo INTEGER NOT NULL, precio_cuota INTEGER NOT NULL, fecha_entrega DATETIME NOT NULL, KEY dnisolicitante_dni_clientes_00_idx (dni_cliente), CONSTRAINT dnisolicitante_dni_clientes_00 FOREIGN KEY (dni_cliente) REFERENCES clientes (dni))'
    try:
        consulta.execute(sql)
        print('La tabla prestamos fue creada con éxito')
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("No se pudo crear la tabla prestamos: ", e)
    #crear tabla empleados
    sql = 'CREATE TABLE IF NOT EXISTS empleados(numero_prestamo INTEGER PRIMARY KEY NOT NULL, nombre VARCHAR(30) NOT NULL, cuil integer NOT NULL,KEY numero_prestamo_empleados_nro_prestamo_prestamos_01_idx (numero_prestamo), CONSTRAINT numero_prestamo_empleados_nro_prestamo_prestamos_01 FOREIGN KEY (numero_prestamo) REFERENCES prestamos (numero_prestamo))'
    try:
        consulta.execute(sql)
        print('La tabla empleados fue creada con éxito')
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("No se pudo crear la tabla empleados: ", e)
    #crear tabla cuotas_prestamos 
    sql = 'CREATE TABLE IF NOT EXISTS cuotas_prestamos(numero_prestamo INTEGER NOT NULL, numero_cuota INTEGER NOT NULL, fecha DATETIME NOT NULL, precio_pagado INTEGER NOT NULL, PRIMARY KEY (numero_prestamo, numero_cuota),KEY numerp_prestamo_couta_prestamo_numero_prestamo_prestamo_02_idx (numero_prestamo), CONSTRAINT numerp_prestamo_couta_prestamo_numero_prestamo_prestamo_02 FOREIGN KEY (numero_prestamo) REFERENCES prestamos (numero_prestamo))'
    try:
        consulta.execute(sql)
        print('La tabla cuotas_prestamos fue creada con éxito')
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("No se pudo crear la tabla cuotas_prestamos: ", e)
    conexion.close()

def connect():
    try:
        conexion = pymysql.connect(host='localhost',
                                    user='root',
                                    password='lezcano65',
                                    db='prestamosdb')
        print("Conexión correcta")
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        #consulta.execute('CREATE SCHEMA prestamosdb')

'''
def insert_data(nombre, apellidos, telefono, email):
    Agregar datos en la Base de Datos

    conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='lezcano65',
                                db='prestamosdb')

    consulta = conexion.cursor()

    datos = (nombre, apellidos, telefono, email)
    sql = 'INSERT INTO contactos(nombre,apellidos,telefono,email) VALUES (%s,%s,%s,%s)'

    try:
        consulta.execute(sql, datos)
        print("Datos guardados con exito")
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al intentar guardar los datos: ", e)
    conexion.commit()
    conexion.close()

def update_data(nombre, apellidos, telefono, email, nom_buscado):
    # Falta Try-Except
    conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='lezcano65',
                                db='prestamosdb')
    consulta = conexion.cursor()
    #UPDATE `prestamosdb`.`contactos` SET `nombre` = 'jorge', `apellidos` = 'lopez', `telefono` = '37845783', `email` = 'jorgelopez@gmail.com' WHERE (`id` = '2');
    #consulta.execute('UPDATE contactos SET nombre = %s ,apellidos = %s,telefono = %s,email = %s WHERE nombre= %s',nom_buscado)
    
    sql='UPDATE contactos SET nombre = %s ,apellidos = %s,telefono = %s,email = %s WHERE nombre= %s'
    try:
        consulta.execute(sql, nom_buscado)
        print("Datos guardados con exito")
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al intentar guardar los datos: ", e)

    consulta.close()
    conexion.commit()
    conexion.close()

def delete_data(nombre, apellidos, telefono, email, nom_buscado):
    # Falta Try-Except
    conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='lezcano65',
                                db='prestamosdb')
    consulta = conexion.cursor()
    consulta.execute('DELETE FROM contactos WHERE nombre= %s',nom_buscado)
    consulta.close()
    conexion.commit()
    conexion.close()

def get_all_data():
    try:
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='lezcano65',
                                    db='prestamosdb')

        sql_select_Query = "select * from contactos"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        for row in records:
            if row=='':
                print("No hay contactos...")
            else:
                print('[+]ID:',row[0],'\n[+]Nombres:',row[1],'\n[+]Apellidos:',row[2],'\n[+]Telefono:',row[3],'\n[+]E-mail:',row[4],"\n----------")  #Mostramos La lista)

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error reading data from MySQL table", e)
    finally:
        connection.close()
        cursor.close()
        print("MySQL connection is closed")

def get_data(nombre):
    try:
        conexion = pymysql.connect(host='localhost',
                                    user='root',
                                    password='lezcano65',
                                    db='prestamosdb')
        try:
            #cursor=conexion.cursor()
            with conexion.cursor() as cursor:
                consulta = 'SELECT * FROM contactos WHERE nombre = %s'
                cursor.execute(consulta, nombre)
                lista_contactos = cursor.fetchall()
                for lista in lista_contactos:
                    print(lista)
        finally:
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error consultando la tabla:", e)'''
