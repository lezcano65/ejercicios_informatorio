'''from tkinter import*
def operar():
    global funcion_operacion
    try:
        if (funcion_operacion != ''):        
            segundo_numero=int(entrada.get())
            entrada.delete(0,END)
            if funcion_operacion == 'sumar':
                entrada.insert(0,int(primerNumero) + segundo_numero)
            elif funcion_operacion == 'division':
                entrada.insert(0,int(primerNumero) // segundo_numero)
            elif funcion_operacion == 'multiplicar':
                entrada.insert(0,int(primerNumero) * segundo_numero)
            elif funcion_operacion == 'restar':
                entrada.insert(0,int(primerNumero) - segundo_numero)
            funcion_operacion=''
    except:
        entrada.insert(0,'Syntax ErRoR')
    return
def button_add(numero):
    try:
        global limpiar
        global primerNumero
        if limpiar:
            primerNumero=entrada.get()
            entrada.delete(0,END)
            limpiar=False
        global result
        anterior = entrada.get()
        entrada.delete(0,END)
        entrada.insert(0, str(anterior)+ str(numero))
        result=int(entrada.get())
    except:
        entrada.insert(0,'Syntax ErRoR')
    return
def clear_boton():
    global primerNumero,segundo_numero,auxiliar,limpiar,result,funcion_operacion
    primerNumero=0
    segundo_numero=0
    auxiliar=0
    limpiar=True
    result=0
    funcion_operacion=''
    entrada.delete(0, END)
    return
def suma_boton():
    try:
        global funcion_operacion
        if primerNumero!=result:
            operar()
        global limpiar
        limpiar=True
        funcion_operacion='sumar'
    except:
        entrada.insert(0,'Syntax ErRoR')

    return
def division_boton():
    try:
        if primerNumero!=result:
            operar()
        global limpiar
        limpiar=True
        global funcion_operacion
        funcion_operacion='division'
    except:
        entrada.insert(0,'Syntax ErRoR')
    return
def restar_boton():
    try:
        if primerNumero!=result:
            operar()
        global limpiar
        limpiar=True
        global funcion_operacion
        funcion_operacion='restar'
    except:
        entrada.insert(0,'Syntax ErRoR')    
    return
def multiplicacion_boton():
    try:
        global limpiar
        if primerNumero!=result:
            operar()
        limpiar=True
        global funcion_operacion
        funcion_operacion='multiplicar'
    except:
        entrada.insert(0,'Syntax ErRoR')
    return
def igual_boton():
    global result
    global primerNumero
    global funcion_operacion
    global auxiliar
    segundo_numero=result
    try:
        if (type(segundo_numero)==str):
            segundo_numero=int(segundo_numero)
        if (type(primerNumero)==str):
            primerNumero=int(primerNumero)
        entrada.delete(0,END)
        if funcion_operacion == 'sumar':
            entrada.insert(0,primerNumero + segundo_numero)
            primerNumero=primerNumero + segundo_numero
        elif funcion_operacion == 'division':
            entrada.insert(0,primerNumero // segundo_numero)
            primerNumero=primerNumero // segundo_numero
        elif funcion_operacion == 'multiplicar':
            entrada.insert(0,primerNumero * segundo_numero)
            primerNumero=primerNumero * segundo_numero
        elif funcion_operacion == 'restar':
            entrada.insert(0,primerNumero - segundo_numero)
            primerNumero=primerNumero - segundo_numero
    except:
        entrada.insert(0,'Syntax ErRoR')
    return 
def botones0_9():
    button_0 = Button(ventana,text='0',padx=40,pady=20,command=lambda: button_add(0))
    button_1 = Button(ventana,text='1',padx=40,pady=20,command=lambda: button_add(1))
    button_2 = Button(ventana,text='2',padx=40,pady=20,command=lambda: button_add(2))
    button_3 = Button(ventana,text='3',padx=40,pady=20,command=lambda: button_add(3))
    button_4 = Button(ventana,text='4',padx=40,pady=20,command=lambda: button_add(4))
    button_5 = Button(ventana,text='5',padx=40,pady=20,command=lambda: button_add(5))
    button_6 = Button(ventana,text='6',padx=40,pady=20,command=lambda: button_add(6))
    button_7 = Button(ventana,text='7',padx=40,pady=20,command=lambda: button_add(7))
    button_8 = Button(ventana,text='8',padx=40,pady=20,command=lambda: button_add(8))
    button_9 = Button(ventana,text='9',padx=40,pady=20,command=lambda: button_add(9))
    button_0.grid(row=4,column=1)
    button_1.grid(row=3,column=0)
    button_2.grid(row=3,column=1)
    button_3.grid(row=3,column=2)
    button_4.grid(row=2,column=0)
    button_5.grid(row=2,column=1)
    button_6.grid(row=2,column=2)
    button_7.grid(row=1,column=0)
    button_8.grid(row=1,column=1)
    button_9.grid(row=1,column=2)
ventana = Tk()
auxiliar=0
limpiar=True
result=0
primerNumero=0
funcion_operacion=''
ventana.title('CALCULADORA')
entrada = Entry(ventana,width=38,font='Helvatica 12')
entrada.grid(row=0,column=0,columnspan=4,padx=20,pady=10)
botones0_9()
suma_boton = Button(ventana,text='+',padx=39,pady=20,command=suma_boton)
restar_boton = Button(ventana,text='-',padx=39,pady=20,command=restar_boton)
division_boton = Button(ventana,text='/',padx=39,pady=20,command=division_boton)
multiplicacion_boton = Button(ventana,text='*',padx=39,pady=20,command=multiplicacion_boton)
igual_boton = Button(ventana,text='=',padx=39,pady=20,command=igual_boton)
clear_boton = Button(ventana,text='clear',padx=30,pady=20,command=clear_boton,bg="red")
suma_boton.grid(row=1,column=3)
restar_boton.grid(row=2,column=3)
division_boton.grid(row=3,column=3)
multiplicacion_boton.grid(row=4,column=3)
clear_boton.grid(row=4,column=0)
igual_boton.grid(row=4,column=2)
resultado= entrada.get()
ventana.mainloop()

input()

'''

def ingresar():
    while True:
        try:
            valor = int(input("Ingrese un numero:\n"))
            break
        except ValueError:
            print('El valor ingresado no es correcto intente de nuevo\n')
    return valor
def sumador():
    valor=ingresar()
    valor+=resultado
    return valor
def restar():
    valor=ingresar()
    valor=resultado-valor
    return valor
def multiplicar(resul):
    valor=ingresar()
    valor=resul*valor
    return valor
def dividir():
    valor=ingresar()
    valor=resultado//valor
    return valor
def operar(op,x):
    if (op=='sumar'):
        x = sumador()
    elif (op=='restar'):
        x = restar()
    elif (op=='multiplicar'):
        x = multiplicar(x)
    elif (op=='dividir'):
        x = dividir()
    return x

calculadora=True
operacion='0'
resultado=ingresar()
while calculadora:
    operacion=str(input('elija operacion (sumar)(restar)(multiplicar)(dividir) o (salir)\n'))
    if (operacion=='salir'):
        calculadora=False
    else:
        resultado=operar(operacion,resultado)
        print('el resultado es',resultado)
input()
'''
import random
def nuevaPalabra():
    palabras={}
    ingresar = True
    while ingresar:
        item=str(input(f'Ingrese una palabra o el valor "0" para terminar\n'))
        if item == '0':
            ingresar=False
            break
        else:
            valor=[]
            for x in item:
                valor.append(x)
            print(valor)
            palabras[item]=valor 
            print(palabras)
    return palabras
palabras=nuevaPalabra()
print(palabras)
opcion='1'
cosas=list(palabras.keys())
print(cosas)
ingresar = True
while ingresar:
    if opcion=='0':
        ingresar=False
        break
    else:
        resultado = list(random.choice(cosas))
        total=len(resultado)
        salida=[]
        for x in range(0,total):
            salida.append('_')
        salida[0]= resultado[0]
        salida[-1]= resultado[-1]
        resultado[0]=[]
        resultado[-1]=[]
        total-=2
        x=10
        while (x > 0):
            print(salida)
            print(f'quedan {x} intentos')
            letra=input('ponga una letra\n ')
            if letra in resultado:
                print('correcto \n')
                pos=resultado.index(letra)
                salida[pos]=resultado[pos]
                resultado[pos]=[]
                total-=1
                if total==0:
                    break
            else:
                x-=1
        print(salida)
        if total==0:
            print('gano el juego \n')
        opcion=input('para terminar (0) de lo contrario jagara de nuevo\n')
input()
'''