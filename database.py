# Este módulo maneja toda la lógica de base de datos en (SQL Server)

import pyodbc

# Conexión única
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=ALFONSO;'
    'DATABASE=ProyectosAlfonso;'
    'Trusted_Connection=yes;'
)

def crear_tabla():
    try:
        with conn.cursor() as cursor:
            cursor.execute('''
                IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='InventarioEquipos' AND xtype='U')
                CREATE TABLE InventarioEquipos (
                    ID INT PRIMARY KEY IDENTITY(1,1),
                    Nombre NVARCHAR(100),
                    Tipo NVARCHAR(50),
                    Marca NVARCHAR(50),
                    Modelo NVARCHAR(50),
                    NumeroSerie NVARCHAR(100),
                    Estado NVARCHAR(50)
                )
            ''')
            conn.commit()
    except Exception as e:
        print(f"Error creando la tabla: {e}")

def insertar_equipo(datos):
    try:
        with conn.cursor() as cursor:
            cursor.execute('''
                INSERT INTO InventarioEquipos (Nombre, Tipo, Marca, Modelo, NumeroSerie, Estado)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                datos["Nombre"],
                datos["Tipo"],
                datos["Marca"],
                datos["Modelo"],
                datos["N° Serie"],
                datos["Estado"]
            ))
            conn.commit()
    except Exception as e:
        print(f"Error insertando equipo: {e}")

def obtener_equipos():
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM InventarioEquipos")
            return cursor.fetchall()
    except Exception as e:
        print(f"Error obteniendo equipos: {e}")
        return []

def eliminar_equipo(id_):
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM InventarioEquipos WHERE ID = ?", (id_,))
            conn.commit()
    except Exception as e:
        print(f"Error eliminando equipo: {e}")

def editar_equipo(id_, datos):
    try:
        with conn.cursor() as cursor:
            cursor.execute('''
                UPDATE InventarioEquipos SET
                    Nombre = ?, Tipo = ?, Marca = ?, Modelo = ?, NumeroSerie = ?, Estado = ?
                WHERE ID = ?
            ''', (
                datos["Nombre"],
                datos["Tipo"],
                datos["Marca"],
                datos["Modelo"],
                datos["N° Serie"],
                datos["Estado"],
                id_
            ))
            conn.commit()
    except Exception as e:
        print(f"Error editando equipo: {e}")

def buscar_equipos(termino):
    try:
        with conn.cursor() as cursor:
            cursor.execute('''
                SELECT * FROM InventarioEquipos
                WHERE Nombre LIKE ? OR Tipo LIKE ? OR NumeroSerie LIKE ?
            ''', (f'%{termino}%', f'%{termino}%', f'%{termino}%'))
            return cursor.fetchall()
    except Exception as e:
        print(f"Error buscando equipos: {e}")
        return []

def filtrar_por_estado(estado):
    try:
        if estado == "Todos":
            return obtener_equipos()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM InventarioEquipos WHERE Estado = ?", (estado,))
            return cursor.fetchall()
    except Exception as e:
        print(f"Error filtrando por estado: {e}")
        return []
