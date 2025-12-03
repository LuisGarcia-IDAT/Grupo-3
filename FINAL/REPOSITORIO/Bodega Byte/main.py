import sys
import hashlib
import os
import webbrowser
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem



# ------------------- Función SHA256 -------------------
def encriptar_sha256(texto):
    return hashlib.sha256(texto.encode('utf-8')).hexdigest()

# ------------------- Clase principal -------------------
class SistemaBodegaByte(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login = uic.loadUi("Ui/LOGIN.ui")
        self.login.show()
        

        # Ocultar caracteres de la contraseña
        self.login.txtContrasena.setEchoMode(2)

        # Botones y Enter
        self.login.btnIngresar.clicked.connect(self.validar_login)
        self.login.txtContrasena.returnPressed.connect(self.validar_login)
        self.login.txtUsuario.returnPressed.connect(self.validar_login)

        # Usuario válido
        self.usuario_registrado = "ADMINISTRADOR"
        self.hash_guardado = encriptar_sha256("1234")

        # Listas temporales
        self.clientes_registrados = []
        self.productos_registrados = []
        self.proveedores_registrados = []
        self.inventario_registrado = []

    # ===================== LOGIN =====================
    def validar_login(self):
        usuario = self.login.txtUsuario.text()
        contrasena = self.login.txtContrasena.text()
        hash_contra = encriptar_sha256(contrasena)
        sha_valida = encriptar_sha256("1234")

        if usuario == "ADMINISTRADOR" and hash_contra == sha_valida:
            QMessageBox.information(self, "Acceso permitido", "Bienvenido al sistema, Administrador.")
            self.abrir_menu_sistema()
        else:
            QMessageBox.warning(self, "Acceso denegado", "Usuario o contraseña incorrectos.")

    # ===================== MENÚ PRINCIPAL =====================
    def abrir_menu_sistema(self):
        self.menu = uic.loadUi("Ui/MENU_SISTEMA.ui")
        self.menu.show()
        self.login.close()

        self.menu.btnRegresarMenu.clicked.connect(self.regresar_login)
        self.menu.btnComprobante.clicked.connect(self.abrir_comprobante)
        self.menu.btnConsultaCliente.clicked.connect(self.abrir_consulta_cliente)
        self.menu.btnInventario.clicked.connect(self.abrir_inventario)
        self.menu.btnVerCliente.clicked.connect(self.abrir_ver_cliente)
        self.menu.btnRegistroProducto.clicked.connect(self.abrir_registro_producto)
        self.menu.btnConsultaProveedores.clicked.connect(self.abrir_consulta_proveedores)

    def regresar_login(self):
        self.menu.close()
        self.login.show()

    # ===================== COMPROBANTE =====================
    def abrir_comprobante(self):
        self.comprobante = uic.loadUi("Ui/COMPROBANTE_PAGO.ui")
        self.comprobante.show()
        self.menu.close()

        self.comprobante.btnRegresarComprobante.clicked.connect(self.regresar_menu_desde_comprobante)
        self.comprobante.btnGuardar.clicked.connect(self.guardar_comprobante)

    def guardar_comprobante(self):
        QMessageBox.information(self, "Comprobante", "Comprobante guardado correctamente.")

    def regresar_menu_desde_comprobante(self):
        self.comprobante.close()
        self.abrir_menu_sistema()

    # ===================== CONSULTA CLIENTE =====================
    def abrir_consulta_cliente(self):
        self.consulta = uic.loadUi("Ui/CONSULTA_CLIENTE.ui")
        self.consulta.show()
        self.menu.close()

        self.consulta.btnRegresarCliente.clicked.connect(self.regresar_menu_desde_consulta)
        self.consulta.btnAgregarCliente.clicked.connect(self.abrir_form_cliente)

    def abrir_form_cliente(self):
        self.form_cliente = uic.loadUi("Ui/FORM_CLIENTE.ui")
        self.form_cliente.show()
        self.form_cliente.btnGuardarCliente.clicked.connect(self.guardar_cliente_desde_form)
        self.form_cliente.btnCancelar.clicked.connect(self.cancelar_form_cliente)

    def guardar_cliente_desde_form(self):
        # Obtener los datos del form
        codigo = self.form_cliente.txtCodigo.text()
        nombre = self.form_cliente.txtNombre.text()
        dni = self.form_cliente.txtDNI.text()
        direccion = self.form_cliente.txtDireccion.text()
        telefono = self.form_cliente.txtTelefono.text()
        correo = self.form_cliente.txtCorreo.text()
        fecha_registro = self.form_cliente.txtFecha.text()
        estado = self.form_cliente.txtEstado.text()

        # Validar campos obligatorios
        if codigo == "" or nombre == "":
            QMessageBox.warning(self.form_cliente, "Error", "Debe ingresar al menos código y nombre.")
            return

        # Agregar a la tabla
        fila = self.consulta.tblClientes.rowCount()
        self.consulta.tblClientes.insertRow(fila)
        self.consulta.tblClientes.setItem(fila, 0, QTableWidgetItem(codigo))
        self.consulta.tblClientes.setItem(fila, 1, QTableWidgetItem(nombre))
        self.consulta.tblClientes.setItem(fila, 2, QTableWidgetItem(dni))
        self.consulta.tblClientes.setItem(fila, 3, QTableWidgetItem(direccion))
        self.consulta.tblClientes.setItem(fila, 4, QTableWidgetItem(telefono))
        self.consulta.tblClientes.setItem(fila, 5, QTableWidgetItem(correo))
        self.consulta.tblClientes.setItem(fila, 6, QTableWidgetItem(fecha_registro))
        self.consulta.tblClientes.setItem(fila, 7, QTableWidgetItem(estado))

        # Limpiar el formulario
        self.form_cliente.txtNombre.clear()
        self.form_cliente.txtDNI.clear()
        self.form_cliente.txtDireccion.clear()
        self.form_cliente.txtTelefono.clear()
        self.form_cliente.txtCorreo.clear()
        self.form_cliente.txtFecha.clear()
        self.form_cliente.txtEstado.clear()

        QMessageBox.information(self.form_cliente, "Éxito", "Cliente agregado correctamente.")

    def cancelar_form_cliente(self):
        self.form_cliente.close()     # Cierra el formulario cliente
        self.consulta.show()          # Vuelve a mostrar la tabla de clientes

    def regresar_menu_desde_consulta(self):
        self.consulta.close()
        self.abrir_menu_sistema()

    # ===================== CONSULTA PROVEEDORES =====================
    def abrir_consulta_proveedores(self):
        self.consulta_proveedores = uic.loadUi("Ui/CONSULTA_PROVEEDORES.ui")
        self.consulta_proveedores.show()
        self.menu.close()

        self.consulta_proveedores.btnRegresarProveedor.clicked.connect(self.regresar_menu_desde_consulta_proveedores)
        self.consulta_proveedores.btnAgregarProveedor.clicked.connect(self.agregar_proveedor_tabla)
        self.consulta_proveedores.btnEditarProveedor.clicked.connect(self.editar_proveedor_tabla)
        self.consulta_proveedores.btnEliminarProveedor.clicked.connect(self.eliminar_proveedor_tabla)

    def regresar_menu_desde_consulta_proveedores(self):
        self.consulta_proveedores.close()
        self.abrir_menu_sistema()

    def agregar_proveedor_tabla(self):
        fila = self.consulta_proveedores.tblProveedores.rowCount()
        self.consulta_proveedores.tblProveedores.insertRow(fila)
        QMessageBox.information(self.consulta_proveedores, "Proveedor agregado", "Nuevo proveedor agregado a la tabla.")

    def editar_proveedor_tabla(self):
        QMessageBox.information(self.consulta_proveedores, "Editar proveedor", "Función de editar proveedor aún no implementada.")

    def eliminar_proveedor_tabla(self):
        QMessageBox.information(self.consulta_proveedores, "Eliminar proveedor", "Función de eliminar proveedor aún no implementada.")

    # ===================== INVENTARIO =====================
    def abrir_inventario(self):
        self.inventario = uic.loadUi("Ui/INVENTARIO_OP.ui")
        self.inventario.show()
        self.menu.close()

        self.inventario.btnRegresarInventario.clicked.connect(self.regresar_menu_desde_inventario)
        self.inventario.btnSalidaDeInventario.clicked.connect(self.abrir_salida_inventario)
        self.inventario.btnListaDeInventario.clicked.connect(self.abrir_lista_inventario)

    def regresar_menu_desde_inventario(self):
        self.inventario.close()
        self.abrir_menu_sistema()

    # ----------------- SALIDA DE INVENTARIO -----------------
    def abrir_salida_inventario(self):
        self.salida_inventario = uic.loadUi("Ui/SALIDA_INVENTARIO.ui")
        self.salida_inventario.show()
        self.inventario.close()
        self.salida_inventario.btnRegresarSalida.clicked.connect(self.regresar_inventario_desde_salida)

    def regresar_inventario_desde_salida(self):
        self.salida_inventario.close()
        self.abrir_inventario()

    # ----------------- LISTA DE INVENTARIO -----------------
    def abrir_lista_inventario(self):
        self.lista_inventario = uic.loadUi("Ui/LISTA_INVENTARIO.ui")
        self.lista_inventario.show()
        self.inventario.close()
        self.lista_inventario.btnRegresarLista.clicked.connect(self.regresar_inventario_desde_lista)

    def regresar_inventario_desde_lista(self):
        self.lista_inventario.close()
        self.abrir_inventario()

    # ===================== REGISTRO PRODUCTO =====================
    def abrir_registro_producto(self):
        self.registro_producto = uic.loadUi("Ui/REGISTRO_PRODUCTO.ui")
        self.registro_producto.show()
        self.menu.close()

        self.registro_producto.btnRegresarProducto.clicked.connect(self.regresar_menu_desde_registro_producto)
        self.registro_producto.btnGuardar.clicked.connect(self.guardar_producto)

    def regresar_menu_desde_registro_producto(self):
        self.registro_producto.close()
        self.abrir_menu_sistema()

    def guardar_producto(self):
        nombre = self.registro_producto.txtNombreProducto.text()
        codigo = self.registro_producto.txtCodigo.text()
        categoria = self.registro_producto.txtCategoria.text()
        marca = self.registro_producto.txtMarca.text()
        unidad = self.registro_producto.txtUMedida.text()
        estado = self.registro_producto.txtEstado.text()
        fecha = self.registro_producto.txtFecha.text()
        precio_costo = self.registro_producto.txtPrecioCosto.text()
        igv = self.registro_producto.txtIGV.text()
        precio_venta = self.registro_producto.txtPrecioVenta.text()
        stock_inicial = self.registro_producto.txtStockInicial.text()
        stock_minimo = self.registro_producto.txtStockMinimo.text()
        stock_actual = self.registro_producto.txtStockActual.text()
        descripcion = self.registro_producto.txtDescripcion.toPlainText()

        if codigo == "" or nombre == "" or categoria == "":
            QMessageBox.warning(self.registro_producto, "Error", "Debe ingresar al menos nombre, código y categoría.")
            return

        producto = {
            "nombre": nombre,
            "codigo": codigo,
            "categoria": categoria,
            "marca": marca,
            "unidad": unidad,
            "estado": estado,
            "fecha": fecha,
            "precio_costo": precio_costo,
            "igv": igv,
            "precio_venta": precio_venta,
            "stock_inicial": stock_inicial,
            "stock_minimo": stock_minimo,
            "stock_actual": stock_actual,
            "descripcion": descripcion
        }

        self.productos_registrados.append(producto)
        QMessageBox.information(self.registro_producto, "Guardado", "Producto registrado correctamente.")

        # Limpiar campos
        self.registro_producto.txtNombreProducto.clear()
        self.registro_producto.txtCodigo.clear()
        self.registro_producto.txtCategoria.clear()
        self.registro_producto.txtMarca.clear()
        self.registro_producto.txtUMedida.clear()
        self.registro_producto.txtEstado.clear()
        self.registro_producto.txtFecha.clear()
        self.registro_producto.txtPrecioCosto.clear()
        self.registro_producto.txtIGV.clear()
        self.registro_producto.txtPrecioVenta.clear()
        self.registro_producto.txtStockInicial.clear()
        self.registro_producto.txtStockMinimo.clear()
        self.registro_producto.txtStockActual.clear()
        self.registro_producto.txtDescripcion.clear()

    # ===================== VER CLIENTE =====================
    def abrir_ver_cliente(self):
        self.ver_cliente = uic.loadUi("Ui/VER_CLIENTE.ui")
        self.ver_cliente.show()
        self.menu.close()

        self.ver_cliente.btnRegresarCliente.clicked.connect(self.regresar_menu_desde_ver_cliente)
        self.ver_cliente.btnCatalogo.clicked.connect(self.abrir_catalogo)

    def regresar_menu_desde_ver_cliente(self):
        self.ver_cliente.close()
        self.abrir_menu_sistema()

    def abrir_catalogo(self):
        # Abrir link de Google Drive
        url = "https://drive.google.com/file/d/1KraI0pksaovDd8a_5MLmQg8y5HsCTE73/view"
        webbrowser.open(url)


# ===================== EJECUCIÓN =====================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = SistemaBodegaByte()
    sys.exit(app.exec_())
