import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class ClienteNoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui/clientenocliente.ui", self)

        # Conexiones de botones
        self.btnCliente.clicked.connect(self.abrirCliente)
        self.btnNocli.clicked.connect(self.abrirNoCliente)

    def abrirCliente(self):
        from Vista.verCliente import verClienteApp
        self.ventanaCliente = verClienteApp()
        self.ventanaCliente.show()
        self.close()

    def abrirNoCliente(self):
        from Vista.CuadroNo import CuadroNoApp
        self.ventanaNoCliente = CuadroNoApp()
        self.ventanaNoCliente.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ClienteNoApp()
    ventana.show()
    sys.exit(app.exec_())
