import math
class Shape:
    def __init__(self, name):
        self._name = name 

    def area(self):
        raise NotImplementedError("Subclasses must implement area method.")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter method.")

    def __str__(self):
        return f"{self._name} Shape"

    def __repr__(self):
        return f"Shape(name='{self._name}')"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.__radius = radius  

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius

    def get_radius(self):
        return self.__radius

    def __str__(self):
        return f"{self._name} with radius {self.__radius}"

    def __repr__(self):
        return f"Circle(radius={self.__radius})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.__radius + other.__radius)
        return NotImplemented


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.__width = width      
        self.__height = height    
    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        return f"{self._name} with width {self.__width} and height {self.__height}"

    def __repr__(self):
        return f"Rectangle(width={self.__width}, height={self.__height})"



def print_shape_info(shape):
  
    print(f"🔷 {shape}")
    print(f"   Area: {shape.area():.2f}")
    print(f"   Perimeter: {shape.perimeter():.2f}")
    print()



def main():
   
    c1 = Circle(5)
    c2 = Circle(3)
    r1 = Rectangle(4, 6)

    print("🔶 Shape Information:")
    for shape in [c1, c2, r1]:
        print_shape_info(shape)


    print("🔐 Encapsulation Test:")
    print(f"Circle 1 Radius (accessed via getter): {c1.get_radius()}")
    


    print("➕ Adding two circles (c1 + c2):")
    c3 = c1 + c2
    print(f"New Circle (c3): {c3}")
    print_shape_info(c3)


    print("🪞 Object Representations:")
    print(f"repr(c1): {repr(c1)}")
    print(f"repr(r1): {repr(r1)}")


if __name__ == "__main__":
    main()
