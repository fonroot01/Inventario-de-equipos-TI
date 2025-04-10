# Este desarrollo es para una aplicación de inventario de equipos
# de TI, utilizando PyQt5 y SQL Server como base de datos.
# Realizado por Alfonso Mosquera 

import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QHBoxLayout, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox
)
from PyQt5.QtGui import QPixmap, QColor, QBrush, QIcon, QPainter
from PyQt5.QtCore import Qt

from styles import aplicar_estilos
from config import CONFIG
from database import crear_tabla, insertar_equipo, obtener_equipos, eliminar_equipo, editar_equipo, buscar_equipos, filtrar_por_estado
from export import exportar_a_excel
from utils import mostrar_mensaje_guardado, cargar_datos_en_campos, limpiar_equipo

class InventarioApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"Inventario de equipos TI - {CONFIG['empresa']}")
        self.setFixedSize(1000, 600)
        self.setWindowIcon(QIcon(CONFIG['icono']))

        # Verificar si la imagen de fondo existe
        self.fondo = None
        if os.path.exists(CONFIG['fondo']):
            self.fondo = QPixmap(CONFIG['fondo'])

        self.setAutoFillBackground(True)  # Hacer que el fondo se rellene automáticamente
        self.init_ui()
        crear_tabla()
        self.actualizar_tabla()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.fondo:
            painter = QPainter(self)
            painter.drawPixmap(self.rect(), self.fondo)  # Establecer la imagen de fondo

    def init_ui(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        form_layout = QVBoxLayout()
        self.campos = {}
        etiquetas = ["ID", "Nombre", "Tipo", "Marca", "Modelo", "N° Serie", "Estado"]
        for etiqueta in etiquetas:
            fila = QHBoxLayout()
            label = QLabel(f"{etiqueta}:")
            # **** AGREGANDO LA PROPIEDAD "for" PARA APLICAR ESTILOS ****
            label.setProperty("for", etiqueta)
            label.setObjectName(f"{etiqueta.lower()}_label")
            campo = QLineEdit() if etiqueta != "Estado" else QComboBox()
            campo.setFixedWidth(250)
            if etiqueta == "Estado":
                campo.setObjectName("estado_combo")
                campo.addItems(["Activo", "En reparación", "Dado de baja"])
            label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            fila.addWidget(label)
            fila.addWidget(campo)
            self.campos[etiqueta] = campo
            form_layout.addLayout(fila)
        main_layout.addLayout(form_layout)

        filtros_layout = QHBoxLayout()
        self.entrada_busqueda = QLineEdit()
        self.entrada_busqueda.setPlaceholderText("Buscar por nombre, tipo, etc.")
        self.entrada_busqueda.setFixedWidth(300)
        self.boton_buscar = QPushButton("Buscar")
        self.boton_buscar.clicked.connect(self.buscar)

        self.filtro_estado = QComboBox()
        self.filtro_estado.addItems(["Todos", "Activo", "En reparación", "Dado de baja"])
        self.filtro_estado.currentIndexChanged.connect(self.aplicar_filtro_estado)

        filtros_layout.addWidget(self.entrada_busqueda)
        filtros_layout.addWidget(self.boton_buscar)
        filtros_layout.addWidget(self.filtro_estado)
        filtros_layout.addStretch()
        main_layout.addLayout(filtros_layout)

        botones_layout = QHBoxLayout()
        self.boton_guardar = QPushButton("Guardar")
        self.boton_editar = QPushButton("Editar")
        self.boton_eliminar = QPushButton("Eliminar")
        self.boton_exportar = QPushButton("Exportar")
        self.boton_consultar = QPushButton("Consultar")
        self.boton_consultar.clicked.connect(self.actualizar_tabla)

        botones = [self.boton_guardar, self.boton_editar, self.boton_eliminar, self.boton_exportar, self.boton_consultar]
        for btn in botones:
            botones_layout.addWidget(btn)
        botones_layout.addStretch()
        main_layout.addLayout(botones_layout)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(7)
        self.tabla.setHorizontalHeaderLabels(etiquetas)
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla.setSelectionBehavior(QTableWidget.SelectRows)
        self.tabla.setSelectionMode(QTableWidget.SingleSelection)
        self.tabla.setStyleSheet("QTableWidget::item:selected { background-color: #004080; color: white; }")
        self.tabla.cellClicked.connect(self.seleccionar_registro)
        main_layout.addWidget(self.tabla)

        self.boton_guardar.clicked.connect(self.guardar)
        self.boton_editar.clicked.connect(self.editar)
        self.boton_eliminar.clicked.connect(self.eliminar)
        self.boton_exportar.clicked.connect(lambda: self.ejecutar_seguro(exportar_a_excel))

    def ejecutar_seguro(self, funcion, *args, **kwargs):
        try:
            funcion(*args, **kwargs)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error: {e}")

    def guardar(self):
        try:
            datos = {k: self.campos[k].text() if not isinstance(self.campos[k], QComboBox) else self.campos[k].currentText() for k in self.campos if k != "ID"}
            insertar_equipo(datos)
            mostrar_mensaje_guardado(datos["Nombre"])
            self.actualizar_tabla()
        except Exception as e:
            QMessageBox.critical(self, "Error al guardar", f"Ocurrió un error al guardar: {e}")

    def actualizar_tabla(self):
        try:
            self.tabla.setRowCount(0)
            for equipo in obtener_equipos():
                fila = self.tabla.rowCount()
                self.tabla.insertRow(fila)
                for i, valor in enumerate(limpiar_equipo(equipo)):
                    item = QTableWidgetItem(str(valor))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.tabla.setItem(fila, i, item)
        except Exception as e:
            QMessageBox.critical(self, "Error al cargar datos", f"No se pudo actualizar la tabla: {e}")

    def eliminar(self):
        try:
            fila = self.tabla.currentRow()
            if fila != -1:
                item = self.tabla.item(fila, 0)
                if item:
                    id_ = item.text()
                    eliminar_equipo(id_)
                    self.actualizar_tabla()
        except Exception as e:
            QMessageBox.critical(self, "Error al eliminar", f"No se pudo eliminar el registro: {e}")

    def editar(self):
        try:
            id_ = self.campos["ID"].text()
            if id_:
                datos = {k: self.campos[k].text() if not isinstance(self.campos[k], QComboBox) else self.campos[k].currentText() for k in self.campos if k != "ID"}
                editar_equipo(id_, datos)
                self.actualizar_tabla()
        except Exception as e:
            QMessageBox.critical(self, "Error al editar", f"No se pudo editar el registro: {e}")

    def buscar(self):
        try:
            termino = self.entrada_busqueda.text()
            resultados = buscar_equipos(termino)
            self.tabla.setRowCount(0)
            for equipo in resultados:
                fila = self.tabla.rowCount()
                self.tabla.insertRow(fila)
                for i, valor in enumerate(limpiar_equipo(equipo)):
                    item = QTableWidgetItem(str(valor))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.tabla.setItem(fila, i, item)
        except Exception as e:
            QMessageBox.critical(self, "Error en búsqueda", f"No se pudo realizar la búsqueda: {e}")

    def aplicar_filtro_estado(self):
        try:
            estado = self.filtro_estado.currentText()
            if estado == "Todos":
                self.actualizar_tabla()
            else:
                resultados = filtrar_por_estado(estado)
                self.tabla.setRowCount(0)
                for equipo in resultados:
                    fila = self.tabla.rowCount()
                    self.tabla.insertRow(fila)
                    for i, valor in enumerate(limpiar_equipo(equipo)):
                        item = QTableWidgetItem(str(valor))
                        item.setTextAlignment(Qt.AlignCenter)
                        self.tabla.setItem(fila, i, item)
        except Exception as e:
            QMessageBox.critical(self, "Error al filtrar", f"No se pudo aplicar el filtro: {e}")

    def seleccionar_registro(self, row, _):
        valores = []
        for col in range(self.tabla.columnCount()):
            item = self.tabla.item(row, col)
            valores.append(item.text() if item is not None else "")
        try:
            cargar_datos_en_campos(valores, self.campos)
        except Exception:
            pass

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    aplicar_estilos(app)
    ventana = InventarioApp()
    ventana.show()
    sys.exit(app.exec_())