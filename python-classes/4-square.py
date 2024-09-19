#!/usr/bin/python3
"""Define a Square class."""


class Square:
    """Class Square with a size attribute."""
    def __init__(self, size=0):
        """
            Initialize a new instance of the Square class.
            size (int): The size of the square.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
            Initialize a new instance of the square class.
            the current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
            Initialize a new instance of the Square class.
            size (int): The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            Initialize a new instance of the Square class.
            size (int): The size of the square.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value