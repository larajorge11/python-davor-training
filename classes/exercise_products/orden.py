from product import Product


class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '|'
        return f'Orden: {self._id_orden}, Productos: {productos_str}'


if __name__ == '__main__':
    producto1 = Product(nombre='camisa', precio=100.00)
    producto2 = Product(nombre='pantalon', precio=150.00)

    productos = [producto1, producto2]
    orden1 = Orden(productos=productos)
    print(orden1)

