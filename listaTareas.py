import tkinter as tk

# Funcion agregar tarea

def agregarTarea():
    tarea = entradaTarea.get()
    if tarea:
        listaTareas.insert(tk.END, tarea)
        entradaTarea.delete(0, tk.END)

# Funcion Eliminar tarea

def eliminiarTarea():
    seleccion = listaTareas.curselection()
    if seleccion:
        listaTareas.delete(seleccion)

# Crear la ventana principal 

ventana = tk.Tk()
ventana.title("Lista de Tareas")

# Crear un textbox para ingresar las tareas
entradaTarea = tk.Entry(ventana)
entradaTarea.pack()

# Crear una lista de tareas
listaTareas = tk.Listbox(ventana)
listaTareas.pack()

# Crear un boton para agregar
botonAgregar = tk.Button(ventana, text="Agregar Tarea", command=agregarTarea)
botonAgregar.pack()

# Crear un boton para eliminar la tarea
botonEliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminiarTarea)
botonEliminar.pack()


ventana.mainloop()