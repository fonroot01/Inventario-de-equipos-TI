import os
from PyQt5.QtGui import QPalette, QColor, QFont, QBrush, QPixmap
from PyQt5.QtWidgets import QApplication, QStyleFactory

from config import CONFIG  # Importar configuración global

def aplicar_estilos(app: QApplication):
    app.setStyle(QStyleFactory.create("Fusion"))

    # Paleta de colores minimalista en tonos azules (ajustado para Zeuss)
    color_fondo_app = QColor(240, 248, 255)      # Un azul muy claro (AliceBlue)
    color_fondo_widgets = QColor(255, 255, 255)  # Blanco
    color_primario = QColor(0, 51, 102)       # Azul oscuro principal de Zeuss (aproximado)
    color_secundario = QColor(173, 216, 230)    # Un azul claro (LightBlue)
    color_texto_principal = QColor(30, 30, 30)   # Gris muy oscuro
    color_texto_resaltado = QColor(50, 50, 50)   # Gris oscuro para etiquetas importantes
    color_borde = QColor(220, 220, 220)        # Gris claro para bordes
    color_hover = QColor(51, 102, 153)        # Un azul ligeramente más claro para hover

    # Configuración de la paleta de colores
    palette = QPalette()
    palette.setColor(QPalette.Window, color_fondo_app)
    palette.setColor(QPalette.Base, color_fondo_widgets)
    palette.setColor(QPalette.AlternateBase, color_fondo_app.lighter(105))
    palette.setColor(QPalette.Text, color_texto_principal)
    palette.setColor(QPalette.Button, color_primario)
    palette.setColor(QPalette.ButtonText, QColor("white"))
    palette.setColor(QPalette.Highlight, color_hover)
    palette.setColor(QPalette.HighlightedText, color_texto_principal) # Texto resaltado más oscuro
    app.setPalette(palette)

    # Fuente para la aplicación
    fuente = QFont("Open Sans", 10)
    app.setFont(fuente)

    # Estilo de la aplicación
    app.setStyleSheet(f"""
        QWidget {{
            font-family: 'Open Sans', sans-serif;
            font-size: 10pt;
            background-color: {color_fondo_app.name()};
            margin: 0;
            padding: 0;
        }}
        QLabel {{
            background-color: transparent;
            color: {color_texto_principal.name()};
            font-size: 10pt;
            margin-right: 7px;
        }}
        QLabel[for="Estado"], QLabel[for="ID"], QLabel[for="Nombre"],
        QLabel[for="Tipo"], QLabel[for="Marca"], QLabel[for="Modelo"],
        QLabel[for="N° Serie"] {{
            font-family: 'Open Sans', sans-serif;
            font-weight: bold;
            font-size: 11pt;
            color: {color_texto_resaltado.name()};
        }}
        QLineEdit, QComboBox {{
            background-color: {color_fondo_widgets.name()};
            color: {color_texto_principal.name()};
            border: 1px solid {color_borde.name()};
            border-radius: 5px;
            padding: 6px;
            selection-background-color: {color_hover.name()};
            selection-color: {color_texto_principal.name()};
        }}
        QPushButton {{
            background-color: {color_primario.name()};
            color: white;
            border: none;
            border-radius: 5px;
            padding: 8px 16px;
            font-weight: normal;
        }}
        QPushButton:hover {{
            background-color: {color_hover.name()};
            color: white; /* Texto del botón en hover blanco para mantener contraste */
        }}
        QTableWidget {{
            background-color: {color_fondo_widgets.name()};
            color: {color_texto_principal.name()};
            border: 1px solid {color_borde.name()};
            border-radius: 5px;
            gridline-color: {color_borde.name()};
            selection-background-color: {color_hover.name()};
            selection-color: {color_texto_principal.name()};
        }}
        QHeaderView::section {{
            background-color: {color_primario.name()};
            color: white;
            padding: 6px;
            border: none;
            font-weight: bold;
        }}
        QScrollBar:vertical {{
            background: {color_fondo_app.lighter(110).name()};
            width: 12px;
            margin: 0px;
        }}
        QScrollBar::handle:vertical {{
            background: {color_primario.lighter(120).name()};
            min-height: 20px;
            border-radius: 6px;
        }}
        QWidget > QVBoxLayout > QHBoxLayout {{
            margin-left: 20px;
            margin-right: 20px;
            margin-top: 10px;
            margin-bottom: 10px;
        }}
    """)

    # Aplicar imagen de fondo a la ventana principal si existe
    fondo_imagen = CONFIG['fondo']
    if os.path.exists(fondo_imagen):
        pixmap = QPixmap(fondo_imagen)
        brush = QBrush(pixmap)
        palette.setBrush(QPalette.Background, brush)
        app.setPalette(palette)