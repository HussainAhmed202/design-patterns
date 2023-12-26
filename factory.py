from abc import ABC


# create an interface
class Shape(ABC):
    def draw() -> None:
        pass


# create the concreate classes that implement the interface
class Rectangle(Shape):
    def draw() -> None:
        print("Inside rectangle draw method")


class Circle(Shape):
    def draw() -> None:
        print("Inside cicle draw method")


class Square(Shape):
    def draw() -> None:
        print("Inside square draw method")


# create shape factory to generate the concreate class objects
class ShapeFactory:
    def get_shape(shape_type: str) -> object:
        if shape_type is None:
            return None
        if shape_type.lower() == "circle":
            return Circle
        elif shape_type.lower() == "rect":
            return Rectangle
        elif shape_type.lower() == "sqr":
            return Square
        return None


def main() -> None:
    shape1 = ShapeFactory.get_shape("circle")
    shape1.draw()


if __name__ == "__main__":
    main()
