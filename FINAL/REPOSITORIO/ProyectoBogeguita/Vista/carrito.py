import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QTableWidgetItem, QMessageBox
)
from PyQt5.QtGui import QPixmap


class CarritoComprasApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui/carritoCompras.ui", self)
        self.setWindowTitle("🛒 Carrito de Compras - Bodega Byte")

        # 📂 Ruta de las imágenes
        self.ruta_imagenes = os.path.join(os.path.dirname(__file__), "Imagenes")

        # BOTÓN REGRESAR
        self.btnRegresar.clicked.connect(self.Regresar)

        # Navegación
        self.btn1.clicked.connect(lambda: self.cambiarPagina(0))
        self.btn2.clicked.connect(lambda: self.cambiarPagina(1))
        self.btn3.clicked.connect(lambda: self.cambiarPagina(2))
        self.btnAnterior.clicked.connect(self.paginaAnterior)
        self.btnSiguiente.clicked.connect(self.paginaSiguiente)

        # Botones carrito
        self.btnAgregar.clicked.connect(self.agregarProducto)
        self.btnQuitar.clicked.connect(self.quitarProducto)
        self.btnFC.clicked.connect(self.finalizarCompra)

        # =============================
        # CONFIGURAR TABLA tblValores
        # =============================
        self.tblValores.setColumnCount(6)
        self.tblValores.setHorizontalHeaderLabels([
            "Producto", "Precio Unitario", "Cantidad",
            "SubTotal", "IGV", "Total Pagar"
        ])

        self.tblValores.setColumnWidth(0, 200)
        self.tblValores.setColumnWidth(1, 100)
        self.tblValores.setColumnWidth(2, 80)
        self.tblValores.setColumnWidth(3, 120)
        self.tblValores.setColumnWidth(4, 80)
        self.tblValores.setColumnWidth(5, 120)

        # ===== Datos de productos =====
        self.paginas = [
            [
                ("ChokoSoda Field", 1.50, "img05", "sp05"),
                ("Leche Gloria", 2.50, "img06", "sp06"),
                ("Mantequilla Gloria", 3.00, "img07", "sp07"),
                ("Yogurt Gloria", 8.00, "img08", "sp08"),
            ],
            [
                ("Pan Bimbo Molde", 5.00, "img09", "sp09"),
                ("Inka Kola 3L", 12.00, "img10", "sp10"),
                ("Aceite Cocinero", 7.00, "img11", "sp11"),
                ("Coka Kola 3L", 11.50, "img12", "sp12"),
            ],
            [
                ("Leche Entera Laive", 5.00, "img01", "sp01"),
                ("Chips Ahoy", 2.00, "img02", "sp02"),
                ("Oreos Mini", 3.50, "img03", "sp03"),
                ("Chocolate Sublime", 2.00, "img04", "sp04"),
            ],
        ]

        # Página inicial
        self.stackedProductos.setCurrentIndex(0)
        self.cargarImagenes(0)

    # =============================
    # Navegación
    # =============================
    def cambiarPagina(self, index):
        self.stackedProductos.setCurrentIndex(index)
        self.cargarImagenes(index)

    def paginaAnterior(self):
        index = self.stackedProductos.currentIndex()
        if index > 0:
            self.cambiarPagina(index - 1)

    def paginaSiguiente(self):
        index = self.stackedProductos.currentIndex()
        if index < self.stackedProductos.count() - 1:
            self.cambiarPagina(index + 1)

    # =============================
    # Cargar imágenes
    # =============================
    def cargarImagenes(self, index):
        grupos = [
            ["img05.jpg", "img06.jpg", "img07.jpg", "img08.jpg"],
            ["img09.jpg", "img10.jpg", "img11.jpg", "img12.jpg"],
            ["img01.jpg", "img02.jpg", "img03.jpg", "img04.jpg"],
        ]

        pagina = self.stackedProductos.widget(index)

        for archivo in grupos[index]:
            label_name = archivo.split(".")[0]
            label = pagina.findChild(QLabel, label_name)

            if label:
                ruta = os.path.join(self.ruta_imagenes, archivo)
                if os.path.exists(ruta):
                    pixmap = QPixmap(ruta)
                    label.setPixmap(pixmap)
                    label.setScaledContents(True)

    # =============================
    # AGREGAR PRODUCTOS
    # =============================
    def agregarProducto(self):
        pagina_actual = self.stackedProductos.currentIndex()
        productos = self.paginas[pagina_actual]
        agregado = False

        for nombre, precio, _, spin_name in productos:
            spin = getattr(self, spin_name)
            cantidad = spin.value()

            if cantidad > 0:
                subtotal = precio * cantidad
                igv = subtotal * 0.18
                total_pagar = subtotal + igv

                fila = self.tblValores.rowCount()
                self.tblValores.insertRow(fila)

                self.tblValores.setItem(fila, 0, QTableWidgetItem(nombre))
                self.tblValores.setItem(fila, 1, QTableWidgetItem(f"S/. {precio:.2f}"))
                self.tblValores.setItem(fila, 2, QTableWidgetItem(str(cantidad)))
                self.tblValores.setItem(fila, 3, QTableWidgetItem(f"S/. {subtotal:.2f}"))
                self.tblValores.setItem(fila, 4, QTableWidgetItem(f"S/. {igv:.2f}"))
                self.tblValores.setItem(fila, 5, QTableWidgetItem(f"S/. {total_pagar:.2f}"))

                spin.setValue(0)
                agregado = True

        if not agregado:
            QMessageBox.warning(self, "Aviso", "Seleccione al menos un producto.")

    # =============================
    # QUITAR PRODUCTO
    # =============================
    def quitarProducto(self):
        fila = self.tblValores.currentRow()
        if fila >= 0:
            self.tblValores.removeRow(fila)
        else:
            QMessageBox.warning(self, "Error", "Seleccione un producto para quitar.")

    # =============================
    # FINALIZAR COMPRA
    # =============================
    def finalizarCompra(self):
        if self.tblValores.rowCount() == 0:
            QMessageBox.warning(self, "Vacío", "No hay productos en el carrito.")
            return

        QMessageBox.information(self, "Compra finalizada", "Gracias por su compra.")
        self.tblValores.setRowCount(0)

    # =============================
    # REGRESAR
    # =============================
    def Regresar(self):
        from Vista.CuadroNo import CuadroNoApp
        self.ventanaNoCliente = CuadroNoApp()
        self.ventanaNoCliente.show()
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = CarritoComprasApp()
    ventana.show()
    sys.exit(app.exec_())
