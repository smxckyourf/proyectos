import tkinter as tk

#importar los modulos restantes de tkinter

from tkinter import *

from tkinter import ttk
from tkinter import messagebox
from clientes import *
from conexion import *


class CatalogoLibros:



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
        tree.bind("<<TreeviewSelect>>", seleccionarRegistro)

        tree.pack() 
            
        interfazCatalogo.mainloop()

    except ValueError as error:
        print("Error al ingresar los datos, error: {}".format(error))
