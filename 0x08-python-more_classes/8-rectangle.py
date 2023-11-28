#!/usr/bin/python3
"""class Rectangle that defines a rectangle by: (based on 2-rectangle.py)"""


class Rectangle:
    """Defines a rectangle with configurable width and height."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with optional width and height."""
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height
        self.print_symbol = Rectangle.print_symbol

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle,
         or 0 if width or height is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join([symbol * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """ Return the 'official' string representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area,
        or rect_1 if both are equal."""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __del__(self):
        """Destructor for a Rectangle instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
