import tkinter
from tkinter import *
from tkinter import messagebox
from conexion import *
from bibliotecario import *

import pymysql

def main_menu():
    global screen
    screen = Tk()
    screen.geometry("300x400")
    screen.title("Inicio de Sesión")

    Label(text="Acceso al sistema", fg="black", width="300", height="3", font=("Calibri",15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesión", height="3", width="30",command=login).pack()
    Label(text="").pack()
    Button(text="Registrar", height="3", width="30",command=register).pack()

    screen.mainloop()

def login():

    global screen1

    screen1 = Toplevel(screen)
    screen1.geometry("300x400")
    screen1.title("Inicio de sesión")
    
    Label(screen1, text="Ingrese su usuario y contraseña").pack()
    Label(screen1, text="")

    global l_user_verify
    global l_pass_verify

    l_user_verify = StringVar()
    l_pass_verify = StringVar()

    global l_user_entry
    global l_pass_entry

    Label(screen1, text="Usuario").pack()
    l_user_entry = Entry(screen1, textvariable= l_user_verify)
    l_user_entry.pack()
    Label(screen1).pack()


    Label(screen1, text="Contraseña").pack() 
    l_pass_entry = Entry(screen1, textvariable= l_pass_verify, show='*')
    l_pass_entry.pack()
    Label(screen1).pack()

    Button(screen1, text="Iniciar sesión", command=validate_data).pack()

def register():

    global screen3
    screen3 = Toplevel(screen)
    screen3.geometry("300x400")
    screen3.title("Registro")

    global r_user_entry
    global r_pass_entry

    r_user_entry = StringVar()
    r_pass_entry = StringVar()

    Label(screen3, text="Ingrese datos para su registro").pack()
    Label(screen3, text="").pack()

    Label(screen3, text="Usuario").pack()
    r_user_entry = Entry(screen3)
    r_user_entry.pack()
    Label(screen3).pack()

    Label(screen3, text="Contraseña").pack()
    r_pass_entry = Entry(screen3, show='*')
    r_pass_entry.pack()
    Label(screen3).pack()

    Button(screen3, text="Registrarse", command=insert_data).pack()

    
def insert_data():
    bd = pymysql.connect(
        host="b1yuhymgnump7qdljjoe-mysql.services.clever-cloud.com",
        user="uj6mkddz7d4eaxis",
        passwd="1w7I0nvVdbHlTym1JSEz",
        db="b1yuhymgnump7qdljjoe",
        port=3306
        )

    fcursor = bd.cursor()
    sql = "INSERT INTO login_data (usuario, clave) VALUES ('{0}','{1}')".format(r_user_entry.get(), r_pass_entry.get())

    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="No Registrado", title="Aviso")


def validate_data():
    bd = pymysql.connect(
        host="b1yuhymgnump7qdljjoe-mysql.services.clever-cloud.com",
        user="uj6mkddz7d4eaxis",
        passwd="1w7I0nvVdbHlTym1JSEz",
        db="b1yuhymgnump7qdljjoe",
        port=3306
        )
    
    fcursor = bd.cursor()
    fcursor.execute("SELECT clave FROM login_data WHERE usuario='"+l_user_verify.get()+"' AND clave='"+l_pass_verify.get()+"'")

#   BIBLIOTECARIO
    if l_user_verify.get()=="Felipe" and l_pass_verify.get()=="Barroso@76":
        messagebox.showinfo(title="Inicio de sesion correcto", message="Usuario y Contraseña correcta\nBibliotecario Identificado")   
        InterfazBibliotecario()


#   ALUMNO
    elif fcursor.fetchall():
        messagebox.showinfo(title="Inicio de sesion correcto", message="Usuario y Contraseña correcta")

    else:
        messagebox.showinfo(title="Inicio de sesion Incorrecto", message="Usuario y Contraseña incorrecta")
    
    bd.close()

main_menu()