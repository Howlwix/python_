class Shape:
    def area(self):
        return self.area
    def perimeter(self):
        return self.perimeter
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width + self.height) * 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius**2 * 3.14
    def perimeter(self):
        return (self.radius * 2) * 3.14
shape = [Rectangle(2, 4), Circle(44)]
for shape in shape:
    print(shape.area())
    print(shape.perimeter())