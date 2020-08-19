import pymysql
def connect():
    conexion = pymysql.connect(host='localhost', 
                                user='root',      
                                password='lezcano65',
                                db='prestamosdb')
    consulta = conexion.cursor()

def create_tablas():
    #crear base de datos
    conexion = pymysql.connect(host='localhost', 
                                user='root',      
                                password='lezcano65')
    consulta = conexion.cursor()
    try:
        with conexion.cursor() as cursor:
            cursor.execute('CREATE DATABASE IF NOT EXISTS prestamosdb')
            print('la base de datos prestamosdb se encuentra disponible')
    finally:
        conexion.close()
    conexion = pymysql.connect(host='localhost', 
                                user='root',      
                                password='lezcano65',
                                db='prestamosdb')
    consulta = conexion.cursor()
    #crear tabla clientes
    sql = 'CREATE TABLE IF NOT EXISTS clientes(dni INTEGER PRIMARY KEY NOT NULL, nombres VARCHAR(30) NOT NULL, apellidos VARCHAR(30) NOT NULL, telefono VARCHAR(14) NOT NULL, celular VARCHAR(14) NOT NULL)'
    try:
        consulta.execute(sql)
        print('La tabla clientes se encuentra disponible')
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("No se pudo crear la tabla clientes: ", e)
    #crear tabla prestamos
    sql = 'CREATE TABLE IF NOT EXISTS prestamos(numero_prestamo INTEGER PRIMARY KEY NOT NULL, dni_cliente INTEGER NOT NULL, fecha_autorizacion DATETIME NOT NULL, fecha_tentativa DATETIME NOT NULL, cantidad_de_cuotas INTEGER NOT NULL, monto_prestamo INTEGER NOT NULL, precio_cuota INTEGER NOT NULL, fecha_entrega DATETIME NOT NULL, KEY dnisolicitante_dni_clientes_00_idx (dni_cliente), CONSTRAINT dnisolicitante_dni_clientes_00 FOREIGN KEY (dni_cliente) REFERENCES clientes (dni))'
    try:
        consulta.execute(sql)
        print('La tabla prestamos se encuentra disponible')
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("No se pudo crear la tabla prestamos: ", e)
    #crear tabla empleados
    sql = 'CREATE TABLE IF NOT EXISTS empleados(numero_prestamo INTEGER PRIMARY KEY NOT NULL, nombre VARCHAR(30) NOT NULL, cuil integer NOT NULL,KEY numero_prestamo_empleados_nro_prestamo_prestamos_01_idx (numero_prestamo), CONSTRAINT numero_prestamo_empleados_nro_prestamo_prestamos_01 FOREIGN KEY (numero_prestamo) REFERENCES prestamos (numero_prestamo))'
    try:
        consulta.execute(sql)
        print('La tabla empleados se encuentra disponible')
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("No se pudo crear la tabla empleados: ", e)
    #crear tabla cuotas_prestamos 
    sql = 'CREATE TABLE IF NOT EXISTS cuotas_prestamos(numero_prestamo INTEGER NOT NULL, numero_cuota INTEGER NOT NULL, fecha DATETIME NOT NULL, precio_pagado INTEGER NOT NULL, PRIMARY KEY (numero_prestamo, numero_cuota),KEY numerp_prestamo_couta_prestamo_numero_prestamo_prestamo_02_idx (numero_prestamo), CONSTRAINT numerp_prestamo_couta_prestamo_numero_prestamo_prestamo_02 FOREIGN KEY (numero_prestamo) REFERENCES prestamos (numero_prestamo))'
    try:
        consulta.execute(sql)
        print('La tabla cuotas_prestamos se encuentra disponible')
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("No se pudo crear la tabla cuotas_prestamos: ", e)
    conexion.close()

def get_all_data_clientes():
    try:
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='lezcano65',
                                    db='prestamosdb')
        sql_select_Query = "select * from clientes"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            if row=='':
                print("No hay contactos...")
            else:
                print('[+]dni:',row[0],'\n[+]nombres:',row[1],'\n[+]apellidos:',row[2],'\n[+]telefono:',row[3],'\n[+]celular:',row[3],"\n----------") 
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error reading data from MySQL table", e)
    finally:
        connection.close()
        cursor.close()
