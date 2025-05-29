#!/usr/bin/env python3
"""
Module that defines an abstract Animal class and its subclasses.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method to return the sound of the animal."""
        pass


class Dog(Animal):
    """Dog class that implements sound method."""

    def sound(self):
        """Return dog's sound."""
        return "Bark"


class Cat(Animal):
    """Cat class that implements sound method."""

    def sound(self):
        """Return cat's sound."""
        return "Meow"
