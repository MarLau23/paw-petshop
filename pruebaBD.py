
import mysql.connector


class Catalogo:
    
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host, 
            user=user, 
            password=password, 
            database=database 
        )
        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
            codigo INT,
            nombre VARCHAR(255) NOT NULL,
            descripcion VARCHAR(1000) NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            tamanio VARCHAR(10),
            stock INT NOT NULL,
            imagen_url VARCHAR(255),
            marca VARCHAR(255))''')
        self.conn.commit()

    #agregar prod
    def agregar_producto(self, codigo, nomb, desc, precio, tam, stock, img, marca):
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo ={codigo}")
        producto_existe = self.cursor.fetchone()
        if producto_existe:
            return False
        
        sql = f"INSERT INTO productos \
            (codigo, nombre, descripcion,precio, tamanio, stock,  imagen_url, marca) \
            VALUES \
            ({codigo}, '{nomb}', '{desc}', {precio}, '{tam}', {stock},  '{img}', '{marca}')"
        self.cursor.execute(sql)
        self.conn.commit()
        return True      

        # #crear diccionario si no existe algun prod con ese codigo
        # producto = {
        #     'codigo': codigo, #int
        #     'nombre': nomb, #str
        #     'descripcion': desc, #str
        #     'precio': precio, #float
        #     'tamanio': tam, #str
        #     'stock': stock, #int
        #     'imagen': img, #str
        #     'marca': marca #str
        # }
        # #se almacena el prod en el arreglo
        # self.productos.append(producto)
        # return True #devuelve true si se agregó

    #consultar prod por codigo
    def consultar_producto(self, codigo):
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        return self.cursor.fetchone()

    #modificar prod por codigo

    def modificar_producto(self, codigo, nuevo_nombre, nueva_descripcion, nuevo_precio, nuevo_tamanio, nuevo_stock, nueva_imagen, nueva_marca):
        # for producto in self.productos:
        #     if producto['codigo'] == codigo:
        #         producto['nombre'] = nuevo_nombre
        #         producto['descripcion'] = nueva_descripcion
        #         producto['precio'] = nuevo_precio
        #         producto['tamanio'] = nuevo_tamanio
        #         producto['stock'] = nuevo_stock
        #         producto['imagen'] = nueva_imagen
        #         producto['marca'] = nueva_marca
        #         return True
        # return False
        sql = f"UPDATE productos SET \
            nombre = '{nuevo_nombre}', \
            descripcion = '{nueva_descripcion}', \
            precio = '{nuevo_precio}', \
            tamanio = '{nuevo_tamanio}', \
            stock = '{nuevo_stock}', \
            imagen_url = '{nueva_imagen}', \
            marca ='{nueva_marca}', \
            WHERE codigo = {codigo}"
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.rowcount > 0
#--------------------------------------------------------------------------------------------
    #eliminar prod por codigo
    def eliminar_producto(self, codigo):
        # for producto in self.productos:
        #     if producto['codigo'] == codigo:
        #         self.productos.remove(producto)
        #         return True
        # return False
        self.cursor.execute(f"DELETE FROM productos WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0
#--------------------------------------------------------------------------------------------
    #listar prod
    def listar_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        productos = self.cursor.fetchall()
        print('-'*20)
        for producto in productos:
            print(f"Código: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Precio: {producto['precio']}")
            print(f"Tamaño: {producto['tamanio']}")
            print(f"Stock: {producto['stock']}")
            print(f"Imagen: {producto['imagen']}")
            print(f"Marca: {producto['marca']}")
            print("-" * 20)
#--------------------------------------------------------------------------------------------
    #mostrar prod
    def mostrar_producto(self, codigo):
        producto = self.consultar_producto(codigo)
        if producto:
            print('-'*20)
            print(f"Código: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Precio: {producto['precio']}")
            print(f"Tamaño: {producto['tamanio']}")
            print(f"Stock: {producto['stock']}")
            print(f"Imagen: {producto['imagen']}")
            print(f"Marca: {producto['marca']}")
            print("-" * 20)
        else:
            print("Producto no encontrado.")


catalogo = Catalogo(host='localhost', user='root', password='', database='productospetshop')

catalogo.agregar_producto(2, 'alimento', 'alimento perros', 12222, '123gr', 12, 'alimento.png', 'pedigree')
catalogo.listar_productos()