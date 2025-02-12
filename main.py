from tkinter import *
from tkinter import messagebox
import re

def email_valido(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

def edad_valida(edad):
    if not edad.isdigit():
        return False
    edad = int(edad)
    return 1 <= edad <= 120

def validar_edad(number):
    return number.isdigit() or number == ""

def send_data():
    usuario_data = usuario.get()
    contraseña_data = str(contraseña.get())
    nombre_data = nombre.get()
    edad_data = str(edad.get())

    if not email_valido(usuario_data):
        messagebox.showerror(
            "Error de Validación", 
            "❌ El email ingresado no es válido.\n\n"
            "⚠️ Asegúrate de usar el formato correcto:\n"
            "   ejemplo@dominio.com"
            )
        return
    
    if not edad_valida(edad_data):
        messagebox.showerror(
            "Error de Validación", 
            "❌ La edad ingresada no es válida.\n\n"
            "⚠️ Debe ser un número entre 1 y 120."
        )
        return

    print(usuario_data, '\t', contraseña_data, '\t', nombre_data, '\t', edad_data)

    archivo = open('registro.txt', 'a')
    archivo.write(usuario_data)
    archivo.write('\t')
    archivo.write(contraseña_data)
    archivo.write('\t')
    archivo.write(nombre_data)
    archivo.write('\t')
    archivo.write(edad_data)
    archivo.write('\n')
    archivo.close()
    print('Nuevo usuario registrado. Usuario:{} | Nombre:{} '.format(usuario_data, nombre_data))

    usuario_entrar.delete(0, END)
    contraseña_entrar.delete(0, END)
    nombre_entrar.delete(0, END)
    edad_entrar.delete(0, END)

    messagebox.showinfo('Exito', ' ✅ Datos enviados correctamente.')


    def calcular():
        try: 
            equilmensual = float(equilmensual_entrar.get())
            diasalmes = float(diasalmes_entrar.get())
            horasaldia = float(horasaldia_entrar.get())
            calculo = equilmensual / (diasalmes * horasaldia)
            calculo_label.config(text=f'El monto de operación por hora es: : {calculo}')
        except ValueError:
            calculo_label.config(text='Error. Ingrese numeros validos')

    mywindow.destroy()
    root = Tk()
    root.geometry('500x400')
    root.title('Form principal')
    root.config(bg='#FFEEDD')

    Label(root, text='Ingrese el P. EQUILIBRIO MENSUAL: ', bg='#FFEEDD').pack(padx=10, pady=5)
    equilmensual_entrar = Entry(root, width='5')
    equilmensual_entrar.pack(padx=10, pady=10)

    Label(root, text='Ingrese la cantidad a usarse: ', bg='#FFEEDD').pack(padx=20, pady=5)
    diasalmes_entrar = Entry(root, width='5')
    diasalmes_entrar.pack(padx=20, pady=10)
    
    Label(root, text='Ingrese la cantidad de aplicaciones: ', bg='#FFEEDD').pack(padx=30, pady=5)
    horasaldia_entrar = Entry(root, width='5')
    horasaldia_entrar.pack(padx=30, pady=10)

    Button(root, text='Calcular: ', command=calcular, bg='green', fg='white').pack(pady=10)

    calculo_label = Label(root, text="El monto de operación por hora es: ", bg='#FFEEDD', font=('Arial', 12))
    calculo_label.pack (pady=10)

    root.mainloop()


mywindow = Tk()
mywindow.geometry('650x550')
mywindow.title('Registration form | Python + Tkinter')
mywindow.resizable(False, False)
mywindow.config(background = '#213141')
main_title = Label (text='Formulario de registro Python | Fab', font = ('times', 13), bg = '#56CD63', fg = 'white', width = '550', height = '2' )
main_title.pack()

usuario_label = Label (text='Usuario', bg = '#FFEEDD')
usuario_label.place(x=22, y=70)
contra_label = Label (text='Contraseña', bg = '#FFEEDD')
contra_label.place(x=22, y=130)
nombre_label = Label (text='Nombre', bg = '#FFEEDD')
nombre_label.place(x=22, y=190)
edad_label = Label (text='Edad', bg = '#FFEEDD')
edad_label.place(x=22, y=250)

usuario = StringVar()
contraseña = StringVar()
nombre = StringVar()
edad = StringVar()

usuario_entrar = Entry(textvariable=usuario, width='40')
contraseña_entrar = Entry(textvariable=contraseña, width='40', show='*')
nombre_entrar = Entry(textvariable=nombre, width='40')
'''Validar que edad sea un numero'''
valida_numero = mywindow.register(validar_edad)
edad_entrar = Entry(textvariable=edad, width='40', validate='key', validatecommand=(valida_numero, '%P'))

usuario_entrar.place(x=22, y=100)
contraseña_entrar.place(x=22, y=160)
nombre_entrar.place(x=22, y=220)
edad_entrar.place(x=22, y=280)

enviar_boton = Button(mywindow, text='Enviar info', command=send_data, width='30', height='2', bg='#00CD63')
enviar_boton.place (x=22, y=320)

mywindow.mainloop()


