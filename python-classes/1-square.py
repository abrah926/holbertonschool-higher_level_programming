#!/usr/bin/python3
'''This module defines a class Square with a private instance attribute'''

class Square:
    '''
    A class that defines a square by its size

    Attributes:
        __size (int): The size of the square (private).
    '''

    def __init__(self, size):
        '''
        Initializes the square with a private size.
        '''
        self.__size = size
