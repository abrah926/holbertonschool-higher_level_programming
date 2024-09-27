from abc import ABC, abstractmethod


class Animal(ABC):
    """An abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return 'Bark'


class Cat(Animal):
    def sound(self):
        return 'Meow'
