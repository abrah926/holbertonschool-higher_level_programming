#!/usr/bin/python3


class Square:
    '''Class that defines a square and the size of its sides'''
    
    def __init__(self, size=0):
        '''
        Initializes the square size to zero

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size isnt an integer.
            ValueError: If size is less than zero. 
        '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be greater than 0")
    
    self.__size = size
