import tkinter as tk

#importar los modulos restantes de tkinter

from tkinter import *

from tkinter import ttk
from tkinter import messagebox
from conexion import *
from CRUDcatalogo import *
from CRUDpersonas import *


class CatalogoLibros:

    global groupbox
    groupbox=None

    global textBoxISBN
    textBoxISBN = None

    global textBoxNombre
    textBoxNombre = None

    global textBoxAutor
    textBoxAutor = None

    global textBoxGenero
    textBoxGenero = None

    global textBoxEditorial
    textBoxEditorial = None

    global textBoxAño
    textBoxAño = None

    global interfazCatalogo
    interfazCatalogo = None

    global tree
    tree = None


def Catalogo():

    try:
        interfazCatalogo = Tk()
        interfazCatalogo.geometry("1920x1080")
        interfazCatalogo.title("Catalogo de libros")

        groupbox = LabelFrame(interfazCatalogo,text="Ingresar datos", padx=8,pady=8)
        groupbox.grid(row=0,column=0,padx=10,pady=10, sticky="ew", columnspan=3)

        labelISBN=Label(groupbox,text="ISBN:", width=13, font=("Arial",12)).grid(row=0,column=0)
        textBoxISBN=Entry(groupbox)
        textBoxISBN.grid(row=0,column=1)

        labelNombre=Label(groupbox,text="Nombre:", width=13, font=("Arial",12)).grid(row=1,column=0)
        textBoxNombre=Entry(groupbox)
        textBoxNombre.grid(row=1,column=1)
        
        labelAutor=Label(groupbox,text="Autor:", width=13, font=("Arial",12)).grid(row=2,column=0)
        textBoxAutor=Entry(groupbox)
        textBoxAutor.grid(row=2,column=1)

        labelGenero=Label(groupbox,text="Genero:", width=13, font=("Arial",12)).grid(row=3,column=0)
        textBoxGenero=Entry(groupbox)
        textBoxGenero.grid(row=3,column=1)

        labelEditorial=Label(groupbox,text="Editorial:", width=13, font=("Arial",12)).grid(row=4,column=0)
        textBoxEditorial=Entry(groupbox)
        textBoxEditorial.grid(row=4,column=1)

        labelAño=Label(groupbox,text="Año de Publicacion:", width=17, font=("Arial",12)).grid(row=5,column=0)
        textBoxAño=Entry(groupbox)
        textBoxAño.grid(row=5,column=1)

        Button(groupbox,text="Guardar", width=10,).grid(row=6,column=0)
        Button(groupbox,text="Modificar", width=10,).grid(row=6,column=1)
        Button(groupbox,text="Eliminar", width=10,).grid(row=6,column=2)

        catalogo_frame = ttk.LabelFrame(interfazCatalogo, text="Información Personal", padding=(20, 10))
        catalogo_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        tree = ttk.Treeview(catalogo_frame, columns=("ISBN","Nombre","Autor","Genero", "Editorial", "Año de publicación"), show='headings', height=6)

        tree.column("# 1",anchor=CENTER)
        tree.heading("# 1", text="ISBN")

        tree.column("# 2",anchor=CENTER)
        tree.heading("# 2", text="Nombre")
        
        tree.column("# 3",anchor=CENTER)
        tree.heading("# 3", text="Autor")

        tree.column("# 4",anchor=CENTER)
        tree.heading("# 4", text="Genero")

        tree.column("# 5",anchor=CENTER)
        tree.heading("# 5", text="Editorial")

        tree.column("# 6",anchor=CENTER)
        tree.heading("# 6", text="Año de publicación")

        for row in CClientes.mostrarClientes():
            tree.insert("", "end", values=row)

        #Ejecutar la funcion al hacer click y mostrar el resultado en los entry
        tree.bind("<<TreeviewSelect>>")

        tree.pack() 
            
        interfazCatalogo.mainloop()

    except ValueError as error:
        print("Error al ingresar los datos, error: {}".format(error))

def guardarRegistros():
    
    global groupbox,textBoxNombre, textBoxISBN, textBoxAutor, textBoxGenero, textBoxEditorial, textBoxAño

    try:
         #verificar si los widgets estan inicializados
         if textBoxISBN is None or textBoxNombre is None or textBoxAutor is None or textBoxGenero is None or textBoxEditorial is None or textBoxAño is None:
             print("Los widgets no han sido inicializados")
             return
         ISBN = textBoxISBN.get()
         nombre = textBoxNombre.get()
         autor = textBoxAutor.get()
         genero = textBoxGenero.get()
         editorial = textBoxEditorial.get()
         año = textBoxAño.get()

         CClientes.ingresarClientes(ISBN, nombre, autor, genero, editorial, año)
         messagebox.showinfo("Informacion", "Registro ingresado correctamente")

         actualizarTreeView()
        
            #limpiamos los campos
         textBoxISBN.delete(0,END)
         textBoxNombre.delete(0,END)
         textBoxAutor.delete(0,END)
         textBoxGenero.delete(0,END)
         textBoxEditorial.delete(0,END)
         textBoxAño.delete(0,END)

    except ValueError as error:
         print("Error al ingresar los datos, error: {}".format(error))

def actualizarTreeView():
    global tree

    try:
        #borrar todos los elementos actuales del treeview a mano
        tree.delete(*tree.get_children())

        #obtener los nuevos datos que deseamos mostrar

        datos = CClientes.mostrarClientes()

        #Insertar los nuevos datos en el treeview

        for row in CClientes.mostrarClientes():
            tree.insert("", "end", values=row)

    except ValueError as error:
        print("Error al actualizar el treeview, error: {}".format(error))


def seleccionarRegistro(event):
    try:
        itemSeleccionado = tree.focus()

        if itemSeleccionado:
            #obtener los valores por columna
            values = tree.item(itemSeleccionado)["values"]

            #Establecer los valores en los widgets

            textBoxISBN.delete(0,END)
            textBoxISBN.insert(0,values[0])

            textBoxNombre.delete(0,END)
            textBoxNombre.insert(0,values[1])

            textBoxAutor.delete(0,END)
            textBoxAutor.insert(0,values[2])

            textBoxGenero.delete(0,END)
            textBoxGenero.insert(0,values[3])

            textBoxEditorial.delete(0,END)
            textBoxEditorial.insert(0,values[4])

            textBoxAño.delete(0,END)
            textBoxAño.insert(0,values[5])

    except ValueError as error:
        print("Error al seleccionar el registro, error: {}".format(error))


Catalogo()
