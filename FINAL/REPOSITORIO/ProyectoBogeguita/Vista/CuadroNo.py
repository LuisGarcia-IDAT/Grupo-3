from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

class CuadroNoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui/cuadronocliente.ui", self)

        # Configuración general
        self.setWindowTitle("No Cliente - Bodega Byte")

        # 🎯 Conexiones de los botones
        self.btnRegresar.clicked.connect(self.salir)
        self.btnCatalogo.clicked.connect(self.abrirCatalogo)
        self.btnManual.clicked.connect(self.abrirManual)
        self.btnSoporte.clicked.connect(self.abrirSoporte)
        self.btnCyS.clicked.connect(self.abrirComentarios)
        self.btnCarrito.clicked.connect(self.abrirCarrito)
        self.btnRegistrarse.clicked.connect(self.registrarse)


    # --------------------------------------------------------
    # 🔁 FUNCIÓN SALIR
    # --------------------------------------------------------
    def salir(self):
        from Vista.clienteNo import ClienteNoApp
        self.ventanaPrincipal = ClienteNoApp()
        self.ventanaPrincipal.show()
        self.close()

    # --------------------------------------------------------
    #  FUNCIONES DE BOTONES
    # --------------------------------------------------------
    def abrirCatalogo(self):
    # Enlace público directo al PDF en Google Drive
        ruta_pdf = "https://drive.google.com/file/d/1KraI0pksaovDd8a_5MLmQg8y5HsCTE73/view?usp=sharing"
        QDesktopServices.openUrl(QUrl(ruta_pdf))



    def abrirManual(self):
        ruta_manual = "https://drive.google.com/file/d/1hBLB72Ex2yAQY2wMIdJ-rQVkxVvYzmf0/view?usp=sharing"  # 🔁 Cambia esta ruta si deseas
        QDesktopServices.openUrl(QUrl(ruta_manual))

    def abrirSoporte(self):
        numero = "51900499583"
        mensaje = "Hola, necesito soporte con Bodega Byte."
        url = f"https://wa.me/{numero}?text={mensaje.replace(' ', '%20')}"
        QDesktopServices.openUrl(QUrl(url))



    def abrirComentarios(self):
        numero = "51993431336"
        mensaje = "Hola, quiero brindar una sugerencia para mejorar el servicio o la aplicación Bodega Byte."

        url = f"https://wa.me/{numero}?text={mensaje.replace(' ', '%20')}"
        QDesktopServices.openUrl(QUrl(url))
        
    def abrirCarrito(self):
        from Vista.carrito import CarritoComprasApp
        self.ventanaCarrito = CarritoComprasApp()
        self.ventanaCarrito.show()
        self.close()


    def registrarse(self):
        print("🟣 Redirigiendo a registro de usuario...")
