
![banner](https://github.com/user-attachments/assets/00326303-a0ca-4b33-a3ee-a6426263917f)

# Inventario de Equipos TI - InvenSotf

Este proyecto nació como una idea durante mi experiencia en soporte técnico en Zeuss SAS. Hoy, lo he desarrollado de forma independiente como una solución moderna y adaptable para la gestión de inventario en cualquier empresa. Se trata de una aplicación de escritorio desarrollada en Python con PyQt5, conectada a una base de datos SQL Server para el almacenamiento y manejo eficiente de la información.

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
- Estilo visual minimalista con colores corporativos.
- Tipografías modernas y botones estilizados.
- Soporte para imagen de fondo institucional.
- Componentes personalizados con una paleta de colores profesional.

---
![Screenshot_1](https://github.com/user-attachments/assets/eae122fd-e360-493a-82f2-3fcfb628c728)
---

## Estructura del Proyecto

```
Inventario_equipos_TI/
│
├── main.py                # Archivo principal de la aplicación
├── database.py            # Lógica de conexión y consultas SQL Server
├── styles.py              # Estilos personalizados con PyQt5
├── export.py              # Funciones para exportar datos a Excel o CSV
├── utils.py               # Funciones auxiliares
├── config.py              # Configuración global de la app
├── iconoInvenSoft.ico     # Ícono de la aplicación
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
![Screenshot_2](https://github.com/user-attachments/assets/abd51b12-080b-4b8d-805a-5877862d5abd)
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
