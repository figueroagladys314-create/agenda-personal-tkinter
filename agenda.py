import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # instalar con: pip install tkcalendar

# ---------------------------
# FUNCIONES
# ---------------------------

def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_desc.get()

    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))
        limpiar_campos()
    else:
        messagebox.showwarning("Campos vacíos", "Completa todos los campos")

def eliminar_evento():
    seleccion = tree.selection()
    if seleccion:
        confirmacion = messagebox.askyesno("Confirmar", "¿Eliminar evento?")
        if confirmacion:
            tree.delete(seleccion)
    else:
        messagebox.showwarning("Sin selección", "Selecciona un evento")

def limpiar_campos():
    entry_hora.delete(0, tk.END)
    entry_desc.delete(0, tk.END)

def salir():
    ventana.quit()

# ---------------------------
# VENTANA PRINCIPAL
# ---------------------------

ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("600x400")

# ---------------------------
# CONTENEDORES (FRAMES)
# ---------------------------

frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=10)

frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

# ---------------------------
# TREEVIEW (LISTA DE EVENTOS)
# ---------------------------

tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")

tree.pack()

# ---------------------------
# CAMPOS DE ENTRADA
# ---------------------------

tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0)
entry_fecha = DateEntry(frame_entrada)
entry_fecha.grid(row=0, column=1)

tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1)

tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0)
entry_desc = tk.Entry(frame_entrada)
entry_desc.grid(row=2, column=1)

# ---------------------------
# BOTONES
# ---------------------------

tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento).grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="Salir", command=salir).grid(row=0, column=2, padx=5)

# ---------------------------
# EJECUCIÓN
# ---------------------------

ventana.mainloop()