#!/usr/bin/python3
""" Module that defines the class Student
"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Method that returns directory description """
        return self.__dict__
