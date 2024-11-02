"""
Programming Language
Estimate: 30 minutes
Start Time: 1255
Actual: 32 minutes
Finish Time: 1327
"""

class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance with name, typing, reflection, and year fields."""

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """ Return True if the language is dynamically typed """

        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of the ProgrammingLanguage object."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"