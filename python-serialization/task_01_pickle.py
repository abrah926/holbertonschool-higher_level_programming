#!/usr/bin/env python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Attributes:
        - name: The name of the person (string).
        - age: The age of the person (integer).
        - is_student: Whether the person is a student (boolean).
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
       Display the object's attributes in a formatted way.
       """
        print(f"Name: {self.name}, Age: {self.age}, Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object and save it to a file using pickle.

        Parameters:
        - filename: The name of the file where the object will be serialized and saved.
        """
        try:
            with open(filename, wb) as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
       Deserialize and load an instance of CustomObject from a file using pickle.

       Parameters:
       - filename: The name of the file from which the object will be loaded.

       Returns:
       An instance of CustomObject or None if an error occurs.
       """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError) as e:
            print(f"Error deserializing object: {e}")
            return None
