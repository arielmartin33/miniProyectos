from listaTareas import *
from tkinter import *
from tkinter import messagebox

#configuración General

root = Tk()

menuBar = Menu(root)
root.config(menu=menuBar)


def version():
    messagebox.showinfo("Version", message="Version 1.0")



archivoMenu = Menu(menuBar, tearoff=0)

archivoMenu.add_command(label="Reloj")
archivoMenu.add_command(label="Calculadora")
archivoMenu.add_command(label="Lista de Tareas" command=)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=root.quit)

ayudaMenu = Menu(menuBar, tearoff=0)

ayudaMenu.add_command(label="Version", command=version)


menuBar.add_cascade(label="Menu", menu=archivoMenu)
menuBar.add_cascade(label="Ayuda", menu=ayudaMenu)





root.mainloop()