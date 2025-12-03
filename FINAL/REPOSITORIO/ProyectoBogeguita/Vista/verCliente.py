from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

class verClienteApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargamos el diseño directamente desde tu carpeta Ui
        uic.loadUi("Ui/vercliente.ui", self)

        # Título de la ventana
        self.setWindowTitle("Ver Cliente - Bodega Byte")

        # Conectamos los botones a sus funciones
        self.btnRegresar.clicked.connect(self.volver)

        # (Opcional) Conexión de otros botones del menú
        self.btnSoporte.clicked.connect(self.soporte)
        self.btnCatalogo.clicked.connect(self.catalogo)
        self.btnManual.clicked.connect(self.manual)
        self.btnCyS.clicked.connect(self.comentarios)
        self.btnCarrito.clicked.connect(self.carrito)



    # -----------------------------
    # FUNCIONES DE LOS BOTONES
    # -----------------------------

    def volver(self):
        from Vista.clienteNo import ClienteNoApp
        self.ventanaPrincipal = ClienteNoApp()
        self.ventanaPrincipal.show()
        self.close()

    def soporte(self):
        numero = "51900499583"
        mensaje = "Hola, necesito soporte con Bodega Byte."
        url = f"https://wa.me/{numero}?text={mensaje.replace(' ', '%20')}"
        QDesktopServices.openUrl(QUrl(url))


    def catalogo(self):
        # Enlace público directo al PDF en Google Drive
        ruta_pdf = "https://drive.google.com/file/d/1KraI0pksaovDd8a_5MLmQg8y5HsCTE73/view?usp=sharing"
        QDesktopServices.openUrl(QUrl(ruta_pdf))

    def manual(self):
        ruta_manual = "https://drive.google.com/file/d/1hBLB72Ex2yAQY2wMIdJ-rQVkxVvYzmf0/view?usp=sharing"  # 🔁 Cambia esta ruta si deseas
        QDesktopServices.openUrl(QUrl(ruta_manual))

    def comentarios(self):
        numero = "51993431336"
        mensaje = "Hola, quiero brindar una sugerencia para mejorar el servicio o la aplicación Bodega Byte."
        url = f"https://wa.me/{numero}?text={mensaje.replace(' ', '%20')}"
        QDesktopServices.openUrl(QUrl(url))

    def carrito(self):
        from Vista.carrito import CarritoComprasApp
        self.ventanaCarrito = CarritoComprasApp()
        self.ventanaCarrito.show()
        self.close()
