# modulo de funciones de utilidad para el proyecto
from tkinter import messagebox

def mostrar_mensaje_guardado(nombre_equipo):
    messagebox.showinfo("Guardado", f"Equipo '{nombre_equipo}' guardado con éxito.")

def cargar_datos_en_campos(valores, campos):
    etiquetas = ["ID", "Nombre", "Tipo", "Marca", "Modelo", "N° Serie", "Estado"]
    for i, key in enumerate(etiquetas):
        if key in campos:
            campos[key].delete(0, "end")
            campos[key].insert(0, valores[i])

def limpiar_equipo(equipo):
    """
    Limpia los campos del equipo para evitar errores en Treeview.
    Reemplaza comas y comillas dobles que puedan generar problemas.
    """
    return tuple(str(x).replace(",", " ").replace('"', "'") for x in equipo)
