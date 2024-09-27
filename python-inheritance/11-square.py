#!/usr/bin/python3
"""
Create a subclass
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Subclass Rectangle inheritated of BaseGometry
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        """
        Return the following rectangle description:
        [Rectangle] <width>/<height>
        """
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
