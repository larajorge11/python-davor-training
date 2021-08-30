class Product:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Product.contador_productos += 1
        self._id_producto = Product.contador_productos
        self._nombre = nombre
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    def __str__(self):
        return f'Id producto: {self._id_producto}, nombre: {self._nombre}, precio: {self._precio}'


if __name__ == '__main__':
    producto1 = Product(nombre='camisa', precio=100.00)
    print(producto1)
    producto2 = Product(nombre='pantalon', precio=150.00)
