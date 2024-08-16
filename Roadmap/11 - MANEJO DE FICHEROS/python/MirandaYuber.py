import os

print("""
MANEJO DE FICHEROS
""")

# print("""
# MODOS DISPONIBLES
# """)
# print('Read ("r") (Leer)')
# print('Append ("a") (Agregar)')
# print('Write ("w") (Escribir)')
# print('Create ("x") (Crear)')
#
# print("""
# LEER UN ARCHIVO ("r")
# """)
#
# # Un objeto que expone una API orientada a archivos (con métodos como read() o write()) al objeto subyacente.
# file = open('file.txt', 'r')
# print(type(file))
#
# print("""
# ATRIBUTOS DEL OBJETO ARCHIVO
# """)
# print(f'name: el nombre del archivo ({file.name})')
# print(f'closed: True si el archivo está cerrado. False si está abierto ({file.closed})')
# print(f'mode: el modo usado para abrir el archivo ({file.mode})')
#
# print("""
# METODOS PARA LEER UN ARCHIVO
# """)
# print('read()')
# content = file.read()
# print(content)
#
# print('readline()')
# print(file.readline())
#
# print('readlines()')
# print(file.readlines())
#
# print('close()')
# file.close()
# print(file.closed)
#
# # print("""
# # CREAR UN ARCHIVO ("x")
# # """)
# # new_file = open('new_file.txt', 'x')
# # print(f'Archivo {new_file.name} creado,')
# # print(f'Modo usado para crear el archivo ({new_file.mode})')
# # new_file.close()
#
# print("""
# MODIFICAR UN ARCHIVO ("a")
# """)
# print('Agrega contenido al final del contenido existente')
# file = open('file.txt', 'a')
# file.write('\nNueva linea')
# file.close()
#
# print("""
# MODIFICAR UN ARCHIVO ("w")
# """)
# print('Elimina el contenido anterior y agrega el nuevo contenido')
# file = open('file.txt', 'w')
# file.write('Contenido nuevo')  # Agrega una linea
# file.writelines(['\nYuber', '\nMiranda'])  # Agrega varias lineas a partir de una lista
# file.close()
#
# print("""
# LEER Y MODIFICAR UN ARCHIVO ("w+", "a+", "r+")
# """)
# # file = open('file.txt', 'w+')  # Leer y escribir
# # file_2 = open('file.txt', 'a+')  # Leer y agregar al final
# # file_3 = open('file.txt', 'r+')  # Leer y escribir
#
# # print("""
# # ELIMINAR ARCHIVOS
# # """)
# # os.remove('new_file.txt')
#
# print("""
# GESTORES DE CONTEXTO
# """)
# with open('file.txt', 'r+') as content_file:
#     print(content_file.read())
#
# print("""
# EXCEPCIONES AL TRABAJAR CON ARCHIVOS
# """)
# try:
#     file = open('prueba.txt', 'r')
# except FileNotFoundError as error:
#     print(f'{type(error).__name__}: El archivo no existe.')
#
# try:
#     file = open('python', 'r')
#     file.write('\nPython')
# except IsADirectoryError as error:
#     print(f'{type(error).__name__}: Es un directorio.')

my_file = open('MirandaYuber.txt', 'x')
my_file.writelines(['Yuber Miranda\n', '22\n', 'Python\n'])
my_file.close()

content_file = open('MirandaYuber.txt', 'r')
print(f'El contenido del archivo es:')
print(content_file.read())

os.remove('MirandaYuber.txt')

print("""
EXTRA
""")


class GestionVentas:
    def __init__(self):
        self.productos = {}
        self.crear_archivo()

    def crear_archivo(self):
        try:
            archivo = open('gestion_ventas.txt', 'x')
            archivo.close()
        except FileExistsError:
            self.eliminar_archivo()
            self.crear_archivo()

    @staticmethod
    def eliminar_archivo():
        if os.path.exists('gestion_ventas.txt'):
            os.remove('gestion_ventas.txt')

    def añadir_producto(self, nombre_producto: str, cantidad_vendida: int, precio: int):
        self.productos[nombre_producto] = {
            'cantidad_vendida': cantidad_vendida,
            'precio': precio
        }
        with open('gestion_ventas.txt', 'a') as file:
            file.write(f'{nombre_producto}, {cantidad_vendida}, {precio}\n')

        print(f'\n\tProducto ({nombre_producto}) agregado a la venta.\n')

    @staticmethod
    def consultar_productos():
        with open('gestion_ventas.txt', 'r') as file:
            print("\tLista de productos:\n"
                  f"\t{file.read()}"
                  )

    def actualizar_producto(self, nombre_producto: str, cantidad_vendida: int, precio: int):
        if nombre_producto in self.productos.keys():
            self.productos[nombre_producto] = {
                'cantidad_vendida': cantidad_vendida,
                'precio': precio
            }

            with open('gestion_ventas.txt', 'w') as file:
                for clave, valor in self.productos.items():
                    file.write(f'{clave}, {valor["cantidad_vendida"]}, {valor["precio"]}\n')

            print(f'\tProducto {nombre_producto} actualizado.')
        else:
            print(f'\n\tEl producto {nombre_producto} no se encuentra todavia en la venta.')

    def eliminar_producto(self, nombre_producto: str):
        if nombre_producto in self.productos:
            del self.productos[nombre_producto]
            with open('gestion_ventas.txt', 'w') as file:
                for clave, valor in self.productos:
                    file.write(f'{clave}, {valor["cantidad_vendida"]}, {valor["precio"]}\n')

            print(f'\tProducto {nombre_producto} eliminado.')
        else:
            print(f'\tEl producto {nombre_producto} no se encuentra en los productos de la venta')

    def calcular_venta_total(self):
        total_venta = 0

        for producto in self.productos.values():
            total_venta += producto['precio'] * producto['cantidad_vendida']

        print(f'\n\tEl precio total de la venta es de ${total_venta}')

    def calcular_venta_por_producto(self, nombre_producto: str):
        if nombre_producto in self.productos.keys():
            total_venta = 0

            for clave, valor in self.productos.items():
                if clave == nombre_producto:
                    total_venta += valor['precio'] * valor['cantidad_vendida']

            print(f'\n\tEl precio total de la venta or el producto {nombre_producto} es de ${total_venta}')
        else:
            print(f'\n\tEl producto {nombre_producto} no se encuentra en la venta.')

    def salir(self):
        print('\n\tPrograma terminado 👋.')
        self.eliminar_archivo()


gestion_ventas = GestionVentas()
print('\tSistemas de Gestión de Ventas')
while True:
    print("\n\tMenú:\n"
          "\t1) Añadir producto\n"
          "\t2) Consultar productos agregados a la venta\n"
          "\t3) Actualizar producto\n"
          "\t4) Eliminar producto\n"
          "\t5) Consultar venta total\n"
          "\t6) Consultar venta por producto\n"
          "\t7) Salir de la aplicación\n"
          )
    opcion = int(input('\tIngrese la opción que desea realizar: '))

    match opcion:
        case 1:
            nombre_producto = input('\tIngrese el nombre del producto: ')
            cantidad_producto = int(input('\tIngrese la cantidad del producto: '))
            precio_producto = int(input('\tIngrese el precio del producto: '))

            gestion_ventas.añadir_producto(
                nombre_producto, cantidad_producto, precio_producto
            )

        case 2:
            gestion_ventas.consultar_productos()

        case 3:
            nombre_producto = input('\tIngrese el nombre del producto que desea actualizar: ')
            cantidad_producto = int(input('\tIngrese la cantidad del producto que desea actualizar: '))
            precio_producto = int(input('\tIngrese el precio del producto que desea actualizar: '))
            gestion_ventas.actualizar_producto(nombre_producto, cantidad_producto, precio_producto)

        case 4:
            nombre_producto = input('\tIngrese el nombre del producto que desea eliminar: ')
            gestion_ventas.eliminar_producto(nombre_producto)

        case 5:
            gestion_ventas.calcular_venta_total()

        case 6:
            nombre_producto = input('\tIngrese el nombre del producto que desea calcular el valor de la venta: ')
            gestion_ventas.calcular_venta_por_producto(nombre_producto)

        case 7:
            gestion_ventas.salir()
            break

        case _:
            print('\n\tEl valor ingresado no se encuentra en el menú.')
            pass
