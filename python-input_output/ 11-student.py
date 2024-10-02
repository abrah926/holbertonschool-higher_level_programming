#!/usr/bin/python3
class Student:
    """
    A class that defines a student with first name, last name, and age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only retrieve those attributes
        """

        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """
      Replaces all attributes of the Student instance using the provided dictionary
      """
    for key, value in json.items():
        setattr(self, key, value)
