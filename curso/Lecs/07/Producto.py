class Producto:
    contador_productos = 0
    def __init__(self, nombre, precio):
        Producto.contador_productos +=1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio
        

    def __str__(self):
        return f'Id Producto: {self._id_producto}, Nombre Producto: {self._nombre}, Precio Producto: {self._precio} '
    
if __name__ ==  '__main__':
    producto1 = Producto('camisa', 100)
    print(producto1)
    producto2 = Producto('pantalon', 200)
    print(producto2)