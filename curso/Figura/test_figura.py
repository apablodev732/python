from FiguraGeometrica import FiguraGeometrica
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo



print(' Cuadrado '.center(30,'-'))
cuadrado1 = Cuadrado(lado=5, color='rojo')
cuadrado1.alto = -10
print(cuadrado1.calcular_area())
print(cuadrado1)

print(' Rectangulo '.center(30,'-'))
rectangulo1 = Rectangulo(ancho=9, alto=8, color='verde')
rectangulo1.ancho = 15
print(rectangulo1.calcular_area())
print(rectangulo1)
