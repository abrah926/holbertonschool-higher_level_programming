#!/usr/bin/python3


"""Module defining the MyList class, inheriting from list."""


class MyList(list):
    """A subclass of list with an additional method to print a sorted list."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying the original list."""
        print(sorted(self))
