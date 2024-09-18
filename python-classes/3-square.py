#!/usr/bin/python3
class Square:
    """A class that defines a square."""
    
    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the square (must be an integer).
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
