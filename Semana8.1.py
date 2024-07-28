import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Configuración de la conexión a MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="semana8"
)
cursor = conexion.cursor()

# Función para obtener datos de las entradas
def obtener_datos():
    return (entry_id.get(), entry_nombre.get(), entry_habitat.get(), entry_estado.get(), entry_region.get())

# Función para mostrar mensajes de error
def mostrar_error(mensaje):
    messagebox.showerror("Error", mensaje)

# Funciones para las operaciones CRUD
def agregar():
    try:
        id, nombre, habitat, estado, region = obtener_datos()
        if not id or not nombre or not habitat or not estado or not region:
            mostrar_error("Todos los campos son obligatorios")
            return
        cursor.execute("INSERT INTO FaunaFlora (ID, NombreCientifico, Habitat, EstadoConservacion, RegionGeografica) VALUES (%s, %s, %s, %s, %s)",
                       (id, nombre, habitat, estado, region))
        conexion.commit()
        messagebox.showinfo("Información", "Registro agregado con éxito")
        mostrar()
    except mysql.connector.Error as err:
        mostrar_error(f"Error al agregar registro: {err}")

def mostrar():
    try:
        cursor.execute("SELECT * FROM FaunaFlora")
        registros = cursor.fetchall()
        lista.delete(0, tk.END)
        for registro in registros:
            formatted_record = f"ID: {registro[0]}, Nombre: {registro[1]}, Hábitat: {registro[2]}, Estado: {registro[3]}, Región: {registro[4]}"
            lista.insert(tk.END, formatted_record)
    except mysql.connector.Error as err:
        mostrar_error(f"Error al mostrar registros: {err}")

def borrar():
    try:
        id = entry_id.get()
        if not id:
            mostrar_error("El campo ID es obligatorio para borrar un registro")
            return
        cursor.execute("DELETE FROM FaunaFlora WHERE ID = %s", (id,))
        conexion.commit()
        messagebox.showinfo("Información", "Registro borrado con éxito")
        mostrar()
    except mysql.connector.Error as err:
        mostrar_error(f"Error al borrar registro: {err}")

def actualizar():
    try:
        id, nombre, habitat, estado, region = obtener_datos()
        if not id or not nombre or not habitat or not estado or not region:
            mostrar_error("Todos los campos son obligatorios")
            return
        cursor.execute("UPDATE FaunaFlora SET NombreCientifico = %s, Habitat = %s, EstadoConservacion = %s, RegionGeografica = %s WHERE ID = %s",
                       (nombre, habitat, estado, region, id))
        conexion.commit()
        messagebox.showinfo("Información", "Registro actualizado con éxito")
        mostrar()
    except mysql.connector.Error as err:
        mostrar_error(f"Error al actualizar registro: {err}")

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de Fauna y Flora")

# Etiquetas y campos de entrada
tk.Label(root, text="ID").grid(row=0, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)

tk.Label(root, text="Nombre Científico").grid(row=1, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=1, column=1)

tk.Label(root, text="Hábitat").grid(row=2, column=0)
entry_habitat = tk.Entry(root)
entry_habitat.grid(row=2, column=1)

tk.Label(root, text="Estado de Conservación").grid(row=3, column=0)
entry_estado = tk.Entry(root)
entry_estado.grid(row=3, column=1)

tk.Label(root, text="Región Geográfica").grid(row=4, column=0)
entry_region = tk.Entry(root)
entry_region.grid(row=4, column=1)

# Botones
tk.Button(root, text="Agregar", command=agregar).grid(row=5, column=0)
tk.Button(root, text="Mostrar", command=mostrar).grid(row=5, column=1)
tk.Button(root, text="Borrar", command=borrar).grid(row=5, column=2)
tk.Button(root, text="Actualizar", command=actualizar).grid(row=5, column=3)

# Lista para mostrar los registros
lista = tk.Listbox(root, width=100)
lista.grid(row=6, column=0, columnspan=4)

# Ejecutar la aplicación
try:
    root.mainloop()
finally:
    conexion.close()


