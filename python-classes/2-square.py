#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        # Validate that size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # Validate that size is >= 0
        if size < 0:
            raise ValueError("size must be >= 0")
        # Private attribute
        self.__size = size
