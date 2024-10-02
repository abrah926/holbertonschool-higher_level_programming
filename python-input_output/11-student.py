#!/usr/bin/python3
class Student:
    """Class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved. Otherwise, all attributes must
        be retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance based on a JSON dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
