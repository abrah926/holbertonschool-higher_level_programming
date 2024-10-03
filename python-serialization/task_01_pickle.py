import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(
            f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as f:  # Corrected 'wb' mode for binary write
                pickle.dump(self, f)
            print(f"Object serialized and saved to {filename}.")
        except Exception as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as f:  # Corrected 'rb' mode for binary read
                return pickle.load(f)
        except FileNotFoundError:
            print(f"Error deserializing object: File '{filename}' not found.")
            return None
        except Exception as e:
            print(f"Error deserializing object: {e}")
            return None
