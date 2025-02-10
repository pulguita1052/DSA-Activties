#Este código lo voy a hacer sin abstracción

#Clase rectangulo, tiene atributos ancho y alto
class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    #metodo pal area base x altura
    def area(self):
        return self.width * self.height

    #metdo pal perimetro 2 veces la susma de ancho y alto
    def perimeter(self):
        return 2 * (self.width + self.height)


rectangleA = Rectangle(5, 12)

rectangleB = Rectangle(4, 18)

print("El area es", rectangleA.area())
print("El perimetro es", rectangleA.perimeter())

