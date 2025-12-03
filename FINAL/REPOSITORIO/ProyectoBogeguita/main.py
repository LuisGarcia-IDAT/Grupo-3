import sys
from PyQt5.QtWidgets import QApplication
from Vista.clienteNo import ClienteNoApp   # ← ¡importa desde la carpeta Vista!

def main():
    app = QApplication(sys.argv)
    ventana = ClienteNoApp()   # abre el menú principal
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


