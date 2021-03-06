#!/usr/bin/python3
"""
    First rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor

        Args:
            width (int): rectangle width
            height (int): rectangle height
            x (int): x coordinate
            y (int): y coordinate
            id (int): identifier
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if not isinstance(x, int):
            raise TypeError("x must be an integer")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        if height <= 0:
            raise ValueError("height must be > 0")

        if x < 0:
            raise ValueError("x must be >= 0")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        """area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """prints the rectangle instance
        """
        for i in range(self.__y):
            print()

        for i in range(self.height):
            for i in range(self.__x):
                    print(" ", end="")
            for i in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """custom print
        """
        cl = "[" + self.__class__.__name__ + "] "
        id = "(" + str(self.id) + ") "
        xy = str(self.__x) + "/" + str(self.__y) + " - "
        wh = str(self.__width) + "/" + str(self.__height)
        return cl + id + xy + wh

    def update(self, *args):
        """assign an argument to each attribute
        """
        if args is not None or len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
