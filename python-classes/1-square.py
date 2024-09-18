#!/usr/bin/python3
"""
shapes.py

This module contains classes for different geometric shapes.
"""

class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int): The size of the square's sides.
    """

    def __init__(self, size):
        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square's sides.
        """
        self.__size = size