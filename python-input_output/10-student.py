#!/usr/bin/python3
"""
This module defines the Student class.
"""


class Student:
    """
    Defines a student with attributes first_name, last_name, and age.

    Methods:
        to_json: Retrieves the dictionary representation of the Student instance.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves the dictionary representation of the Student instance.

        Args:
            attrs (list): A list of strings representing attribute names to retrieve.

        Returns:
            dict: The dictionary containing the specified attributes.
                  If attrs is None, all attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        else:
            return self.__dict__
