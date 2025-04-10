# este modulo se encargara de exportar los datos a un archivo excel

import pandas as pd
from database import obtener_equipos
from tkinter import messagebox

def exportar_a_excel():
    equipos = obtener_equipos()
    columnas = ["ID", "Nombre", "Tipo", "Marca", "Modelo", "N° Serie", "Estado"]
    df = pd.DataFrame(equipos, columns=columnas)
    try:
        df.to_excel("InventarioExportado.xlsx", index=False)
        messagebox.showinfo("Exportación exitosa", "Archivo 'InventarioExportado.xlsx' creado correctamente.")
    except Exception as e:
        messagebox.showerror("Error de exportación", str(e))
