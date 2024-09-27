#!/usr/bin/python3
"""
Create a class
"""


class BaseGeometry():
    """
    class BaseGeometry
    """
    pass

    def area(self):
        """
        That raises an Exception with a message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value
        """
        if isinstance(value, int) is False:
            raise TypeError("{} must be an integer". format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0". format(name))
