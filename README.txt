# 📦 Aplicación de Inventario de equipos TI

Esta aplicación de escritorio desarrollada en **Python (PyQt5)** para la gestión de inventarios tecnológicos en la empresa **Zeuss**. Diseñada con una interfaz moderna, responsiva y personalizada con los colores institucionales, esta herramienta permite llevar un control eficiente de los equipos registrados en una base de datos SQL Server.

---

## 🚀 Funcionalidades principales

- 🧾 **Agregar equipos** con campos como nombre, tipo, marca, modelo, número de serie y estado.
- ✏️ **Editar registros** directamente desde la tabla principal.
- ❌ **Eliminar equipos** de forma rápida y segura.
- 🔍 **Búsqueda** por nombre, tipo o número de serie.
- 📊 **Filtrar por estado** (Activo, Inactivo, En reparación, etc.).
- 📤 **Exportar datos** a archivos Excel o CSV.
- 🖼️ **Interfaz personalizada** con imagen de fondo, diseño limpio y estilos aplicados.
- 🗃️ **Consulta de registros** directamente desde la base de datos SQL Server.

---

## 🗄️ Relación con SQL Server

La aplicación se conecta a una instancia local de **SQL Server** utilizando `pyodbc`. Todos los registros del inventario se almacenan en la base de datos `ProyectosAlfonso` en la tabla `InventarioEquipos`.

### 📌 Estructura de la tabla:

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
