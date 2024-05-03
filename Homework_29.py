import math


class Shape:

    def __init__(self):
        pass

    def perimetr(self):
        pass

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('Radius mast be positive')
        self.radius = radius

    def perimetr(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, w, h):
        if w <= 0 and h <= 0:
            raise ValueError("Parametr must be positive")
        self.w = w
        self.h = h

    def perimetr(self):
        return 2 * (self.h + self.w)

    def area(self):
        return self.w * self.h


class Triangle(Shape):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Parametr must be positive")
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        p = self.a + self.b + self.c
        return p

    def area(self):
        p = self.a + self.b + self.c
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


k1 = Circle(3)
k2 = Triangle(-1, 2, 3)
k3 = Rectangle(2, 4)
print(k1.area())
print(k1.perimetr())
print(k2.perimetr())
print(k2.area())
print(k3.area())
print(k3.perimetr())
