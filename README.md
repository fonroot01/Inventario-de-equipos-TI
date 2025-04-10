# Inventario de Equipos TI - Zeuss

Este proyecto es una aplicación de escritorio desarrollada en Python con PyQt5, diseñada para gestionar el inventario de equipos tecnológicos de la empresa Zeuss. Permite registrar, editar, eliminar y consultar información sobre equipos de manera visual, rápida y eficiente.

---

## Funcionalidades Principales

### Gestión de Inventario
- Registro de equipos con los campos: Nombre, Tipo, Marca, Modelo, N° Serie, Estado.
- Edición de información de equipos existentes.
- Eliminación de registros desde la interfaz.
- Visualización de equipos en una tabla organizada y moderna.
- Filtro por estado del equipo (Operativo, En reparación, Dañado, etc.).
- Búsqueda por nombre, tipo o número de serie.

### Exportación de Datos
- Exportación de los registros a formato Excel (.xlsx) y CSV (.csv).

### Búsqueda y Filtros
- Búsqueda inteligente en tiempo real.
- Filtro por estado desde una lista desplegable.

### Interfaz Gráfica
- Estilo visual minimalista con colores corporativos de Zeuss Los Búcaros.
- Tipografías modernas y botones estilizados.
- Soporte para imagen de fondo institucional.
- Componentes personalizados con una paleta de colores profesional.

---

## Estructura del Proyecto

```
Inventario_equipos_Zeuss/
│
├── main.py                # Archivo principal de la aplicación
├── database.py            # Lógica de conexión y consultas SQL Server
├── styles.py              # Estilos personalizados con PyQt5
├── export.py              # Funciones para exportar datos a Excel o CSV
├── utils.py               # Funciones auxiliares
├── config.py              # Configuración global de la app
├── iconozeuss.ico         # Ícono de la aplicación
├── README.md              # Documentación del proyecto
└── requirements.txt       # Lista de dependencias
```

---

## Conexión a la Base de Datos

La aplicación se conecta a una base de datos SQL Server usando el driver ODBC:

```python
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=ALFONSO;'
    'DATABASE=ProyectosAlfonso;'
    'Trusted_Connection=yes;'
)
```

La tabla utilizada es `InventarioEquipos`, la cual se crea automáticamente si no existe:

```sql
CREATE TABLE InventarioEquipos (
    ID INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100),
    Tipo NVARCHAR(50),
    Marca NVARCHAR(50),
    Modelo NVARCHAR(50),
    NumeroSerie NVARCHAR(100),
    Estado NVARCHAR(50)
);
```

---

## Requisitos

- Python 3.9 o superior
- SQL Server (instalado y en funcionamiento)
- Dependencias de Python (instalables con pip):

```
pyqt5
pyodbc
pandas
openpyxl
```

---

## Instalación y Ejecución

1. Clonar el repositorio:
```bash
git clone https://github.com/fonroot01/Inventario-de-equipos-TI.git
cd Inventario-de-equipos-TI
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Verificar que SQL Server esté activo.

4. Ejecutar la aplicación:
```bash
python main.py
```

---

## Licencia

Este proyecto está bajo la Licencia Apache 2.0. Consulta el archivo `LICENSE` para más información.

---

## Autor

Alfonso Mosquera  
Correo: alfomosque22@gmail.com
